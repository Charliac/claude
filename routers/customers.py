from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from database import get_db
from models.customer import Customer
from schemas.customer import CustomerCreate, CustomerUpdate, CustomerOut
from schemas.order import OrderOut

router = APIRouter(prefix="/customers", tags=["Clientes"])


@router.get("/", response_model=list[CustomerOut])
def list_customers(
    search: str | None = Query(None, description="Buscar por nombre o teléfono"),
    department: str | None = None,
    db: Session = Depends(get_db),
):
    q = db.query(Customer)
    if department:
        q = q.filter(Customer.department == department)
    if search:
        q = q.filter(
            Customer.full_name.ilike(f"%{search}%") | Customer.phone.ilike(f"%{search}%")
        )
    return q.order_by(Customer.full_name).all()


@router.post("/", response_model=CustomerOut, status_code=status.HTTP_201_CREATED)
def create_customer(data: CustomerCreate, db: Session = Depends(get_db)):
    customer = Customer(**data.model_dump())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


@router.get("/{customer_id}", response_model=CustomerOut)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return customer


@router.get("/{customer_id}/orders", response_model=list[OrderOut])
def get_customer_orders(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return customer.orders


@router.patch("/{customer_id}", response_model=CustomerOut)
def update_customer(customer_id: int, data: CustomerUpdate, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    for field, value in data.model_dump(exclude_none=True).items():
        setattr(customer, field, value)
    db.commit()
    db.refresh(customer)
    return customer


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    if customer.orders:
        raise HTTPException(
            status_code=400,
            detail="No se puede eliminar un cliente con pedidos registrados"
        )
    db.delete(customer)
    db.commit()
