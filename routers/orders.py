from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from database import get_db
from models.customer import Customer
from models.order import Order, OrderItem, OrderStatus, PaymentStatus
from models.product import Product
from schemas.order import OrderCreate, OrderUpdate, OrderOut, OrderStatusUpdate

router = APIRouter(prefix="/orders", tags=["Pedidos"])


def _generate_order_number(db: Session) -> str:
    count = db.query(Order).count()
    return f"PE-{count + 1:05d}"


def _build_order(data: OrderCreate, db: Session) -> Order:
    customer = db.query(Customer).filter(Customer.id == data.customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    items = []
    subtotal = 0.0

    for item_data in data.items:
        product = db.query(Product).filter(Product.id == item_data.product_id).first()
        if not product:
            raise HTTPException(
                status_code=404, detail=f"Producto {item_data.product_id} no encontrado"
            )
        if not product.is_active:
            raise HTTPException(
                status_code=400,
                detail=f"El producto '{product.name}' no está disponible"
            )
        if product.stock < item_data.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Stock insuficiente para '{product.name}'. Disponible: {product.stock}"
            )
        unit_price = item_data.unit_price if item_data.unit_price is not None else product.price
        line_subtotal = round(unit_price * item_data.quantity, 2)
        subtotal += line_subtotal
        items.append(OrderItem(
            product_id=product.id,
            quantity=item_data.quantity,
            unit_price=unit_price,
            subtotal=line_subtotal,
        ))
        # Descontar stock
        product.stock -= item_data.quantity

    total = round(subtotal + data.delivery_cost - data.discount, 2)

    order_data = data.model_dump(exclude={"items"})
    order = Order(
        **order_data,
        order_number=_generate_order_number(db),
        subtotal=round(subtotal, 2),
        total=total,
        items=items,
    )
    return order


@router.get("/", response_model=list[OrderOut])
def list_orders(
    status: OrderStatus | None = None,
    payment_status: PaymentStatus | None = None,
    department: str | None = None,
    db: Session = Depends(get_db),
):
    q = db.query(Order)
    if status:
        q = q.filter(Order.status == status)
    if payment_status:
        q = q.filter(Order.payment_status == payment_status)
    if department:
        q = q.filter(Order.delivery_department == department)
    return q.order_by(Order.created_at.desc()).all()


@router.post("/", response_model=OrderOut, status_code=status.HTTP_201_CREATED)
def create_order(data: OrderCreate, db: Session = Depends(get_db)):
    order = _build_order(data, db)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return order


@router.patch("/{order_id}", response_model=OrderOut)
def update_order(order_id: int, data: OrderUpdate, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    if order.status in (OrderStatus.ENTREGADO, OrderStatus.CANCELADO):
        raise HTTPException(
            status_code=400,
            detail="No se puede modificar un pedido entregado o cancelado"
        )
    update_data = data.model_dump(exclude_none=True)
    if "delivery_cost" in update_data or "discount" in update_data:
        delivery_cost = update_data.get("delivery_cost", order.delivery_cost)
        discount = update_data.get("discount", order.discount)
        order.total = round(order.subtotal + delivery_cost - discount, 2)
    for field, value in update_data.items():
        setattr(order, field, value)
    db.commit()
    db.refresh(order)
    return order


@router.patch("/{order_id}/status", response_model=OrderOut)
def update_order_status(order_id: int, data: OrderStatusUpdate, db: Session = Depends(get_db)):
    """Cambia el estado del pedido. Si se marca como ENTREGADO se registra la fecha y hora."""
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    prev_status = order.status
    order.status = data.status

    if data.status == OrderStatus.ENTREGADO:
        order.delivered_at = datetime.now(timezone.utc)
        order.payment_status = PaymentStatus.COBRADO
    elif data.status in (OrderStatus.RECHAZADO, OrderStatus.DEVUELTO):
        order.payment_status = PaymentStatus.NO_COBRADO
        # Devolver stock
        for item in order.items:
            item.product.stock += item.quantity
    elif data.status == OrderStatus.CANCELADO and prev_status not in (
        OrderStatus.ENTREGADO, OrderStatus.RECHAZADO, OrderStatus.DEVUELTO
    ):
        # Devolver stock si no estaba ya devuelto
        for item in order.items:
            item.product.stock += item.quantity

    if data.payment_status:
        order.payment_status = data.payment_status
    if data.notes:
        order.notes = (order.notes or "") + f"\n[{data.status.value.upper()}] {data.notes}"

    db.commit()
    db.refresh(order)
    return order
