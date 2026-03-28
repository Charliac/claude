from datetime import date, datetime, timedelta, timezone
from fastapi import APIRouter, Depends, Query
from sqlalchemy import func, and_
from sqlalchemy.orm import Session
from database import get_db
from models.order import Order, OrderItem, OrderStatus, PaymentStatus
from models.product import Product
from models.customer import Customer

router = APIRouter(prefix="/reports", tags=["Reportes"])


def _date_range(since: date | None, until: date | None):
    """Retorna filtros de fecha para aplicar a Order.created_at."""
    filters = []
    if since:
        filters.append(Order.created_at >= datetime(since.year, since.month, since.day))
    if until:
        end = datetime(until.year, until.month, until.day, 23, 59, 59)
        filters.append(Order.created_at <= end)
    return filters


@router.get("/dashboard")
def dashboard(
    since: date | None = Query(None, description="Fecha inicio (YYYY-MM-DD)"),
    until: date | None = Query(None, description="Fecha fin (YYYY-MM-DD)"),
    db: Session = Depends(get_db),
):
    """Resumen general de ventas en BOB."""
    date_filters = _date_range(since, until)

    delivered_filter = [Order.status == OrderStatus.ENTREGADO] + date_filters
    cobrado_filter = [
        Order.status == OrderStatus.ENTREGADO,
        Order.payment_status == PaymentStatus.COBRADO,
    ] + date_filters

    total_orders = db.query(func.count(Order.id)).filter(*date_filters).scalar() or 0
    delivered = db.query(func.count(Order.id)).filter(*delivered_filter).scalar() or 0
    rejected = (
        db.query(func.count(Order.id))
        .filter(Order.status == OrderStatus.RECHAZADO, *date_filters)
        .scalar() or 0
    )
    revenue = db.query(func.sum(Order.total)).filter(*cobrado_filter).scalar() or 0.0

    pending = (
        db.query(func.count(Order.id))
        .filter(Order.status == OrderStatus.PENDIENTE, *date_filters)
        .scalar() or 0
    )
    in_transit = (
        db.query(func.count(Order.id))
        .filter(Order.status == OrderStatus.EN_CAMINO, *date_filters)
        .scalar() or 0
    )

    delivery_rate = round(delivered / total_orders * 100, 1) if total_orders else 0.0
    rejection_rate = round(rejected / total_orders * 100, 1) if total_orders else 0.0

    low_stock_count = (
        db.query(func.count(Product.id))
        .filter(Product.is_active == True, Product.stock <= Product.stock_minimum)
        .scalar() or 0
    )

    return {
        "periodo": {
            "desde": since.isoformat() if since else "todos",
            "hasta": until.isoformat() if until else "todos",
        },
        "pedidos": {
            "total": total_orders,
            "pendientes": pending,
            "en_camino": in_transit,
            "entregados": delivered,
            "rechazados": rejected,
        },
        "ventas": {
            "ingresos_bob": round(revenue, 2),
            "tasa_entrega_pct": delivery_rate,
            "tasa_rechazo_pct": rejection_rate,
        },
        "inventario": {
            "productos_stock_bajo": low_stock_count,
        },
    }


@router.get("/top-products")
def top_products(
    limit: int = Query(10, ge=1, le=50),
    since: date | None = None,
    until: date | None = None,
    db: Session = Depends(get_db),
):
    """Productos más vendidos por cantidad de unidades entregadas."""
    date_filters = _date_range(since, until)
    delivered_filter = [Order.status == OrderStatus.ENTREGADO] + date_filters

    rows = (
        db.query(
            Product.id,
            Product.name,
            Product.sku,
            func.sum(OrderItem.quantity).label("units_sold"),
            func.sum(OrderItem.subtotal).label("revenue_bob"),
        )
        .join(OrderItem, OrderItem.product_id == Product.id)
        .join(Order, Order.id == OrderItem.order_id)
        .filter(*delivered_filter)
        .group_by(Product.id)
        .order_by(func.sum(OrderItem.quantity).desc())
        .limit(limit)
        .all()
    )

    return [
        {
            "product_id": r.id,
            "name": r.name,
            "sku": r.sku,
            "units_sold": r.units_sold,
            "revenue_bob": round(r.revenue_bob, 2),
        }
        for r in rows
    ]


@router.get("/orders-by-department")
def orders_by_department(
    since: date | None = None,
    until: date | None = None,
    db: Session = Depends(get_db),
):
    """Pedidos agrupados por departamento de Bolivia."""
    date_filters = _date_range(since, until)

    all_orders = db.query(Order).filter(*date_filters).all()

    summary: dict[str, dict] = {}
    for order in all_orders:
        dept = order.delivery_department
        if dept not in summary:
            summary[dept] = {"total_orders": 0, "delivered": 0, "revenue_bob": 0.0}
        summary[dept]["total_orders"] += 1
        if order.status == OrderStatus.ENTREGADO:
            summary[dept]["delivered"] += 1
            summary[dept]["revenue_bob"] += order.total

    return [
        {
            "department": dept,
            "total_orders": data["total_orders"],
            "delivered": data["delivered"],
            "revenue_bob": round(data["revenue_bob"], 2),
        }
        for dept, data in sorted(summary.items(), key=lambda x: -x[1]["total_orders"])
    ]


@router.get("/sales-by-day")
def sales_by_day(
    days: int = Query(30, ge=1, le=365, description="Últimos N días"),
    db: Session = Depends(get_db),
):
    """Ventas diarias (pedidos entregados) de los últimos N días."""
    since = datetime.now(timezone.utc) - timedelta(days=days)

    rows = (
        db.query(
            func.date(Order.delivered_at).label("day"),
            func.count(Order.id).label("orders"),
            func.sum(Order.total).label("revenue_bob"),
        )
        .filter(
            Order.status == OrderStatus.ENTREGADO,
            Order.delivered_at >= since,
        )
        .group_by(func.date(Order.delivered_at))
        .order_by(func.date(Order.delivered_at))
        .all()
    )

    return [
        {
            "date": str(r.day),
            "orders": r.orders,
            "revenue_bob": round(r.revenue_bob or 0, 2),
        }
        for r in rows
    ]


@router.get("/customers/top")
def top_customers(
    limit: int = Query(10, ge=1, le=50),
    since: date | None = None,
    until: date | None = None,
    db: Session = Depends(get_db),
):
    """Clientes con más pedidos entregados."""
    date_filters = _date_range(since, until)
    delivered_filter = [Order.status == OrderStatus.ENTREGADO] + date_filters

    rows = (
        db.query(
            Customer.id,
            Customer.full_name,
            Customer.phone,
            Customer.department,
            func.count(Order.id).label("total_orders"),
            func.sum(Order.total).label("total_spent_bob"),
        )
        .join(Order, Order.customer_id == Customer.id)
        .filter(*delivered_filter)
        .group_by(Customer.id)
        .order_by(func.sum(Order.total).desc())
        .limit(limit)
        .all()
    )

    return [
        {
            "customer_id": r.id,
            "full_name": r.full_name,
            "phone": r.phone,
            "department": r.department,
            "total_orders": r.total_orders,
            "total_spent_bob": round(r.total_spent_bob or 0, 2),
        }
        for r in rows
    ]
