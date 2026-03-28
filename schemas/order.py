from datetime import datetime
from pydantic import BaseModel, ConfigDict, model_validator
from models.order import OrderStatus, PaymentStatus


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    unit_price: float | None = None   # si None, se toma el precio actual del producto


class OrderItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    quantity: int
    unit_price: float
    subtotal: float


class OrderBase(BaseModel):
    customer_id: int
    delivery_department: str
    delivery_city: str
    delivery_address: str
    delivery_reference: str | None = None
    courier_name: str | None = None
    courier_phone: str | None = None
    tracking_code: str | None = None
    delivery_cost: float = 0.0
    discount: float = 0.0
    notes: str | None = None


class OrderCreate(OrderBase):
    items: list[OrderItemCreate]

    @model_validator(mode="after")
    def items_not_empty(self) -> "OrderCreate":
        if not self.items:
            raise ValueError("El pedido debe tener al menos un producto")
        return self


class OrderUpdate(BaseModel):
    delivery_department: str | None = None
    delivery_city: str | None = None
    delivery_address: str | None = None
    delivery_reference: str | None = None
    courier_name: str | None = None
    courier_phone: str | None = None
    tracking_code: str | None = None
    delivery_cost: float | None = None
    discount: float | None = None
    notes: str | None = None


class OrderStatusUpdate(BaseModel):
    status: OrderStatus
    payment_status: PaymentStatus | None = None
    notes: str | None = None


class OrderOut(OrderBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    order_number: str
    subtotal: float
    total: float
    status: OrderStatus
    payment_status: PaymentStatus
    items: list[OrderItemOut]
    created_at: datetime
    updated_at: datetime
    delivered_at: datetime | None
