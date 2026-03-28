from datetime import datetime
from enum import Enum as PyEnum
from sqlalchemy import String, Text, Float, Integer, ForeignKey, DateTime, Enum, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class OrderStatus(str, PyEnum):
    PENDIENTE = "pendiente"           # recién creado, sin confirmar
    CONFIRMADO = "confirmado"         # confirmado con el cliente por teléfono
    EN_PREPARACION = "en_preparacion" # preparando el paquete
    EN_CAMINO = "en_camino"           # despachado al mensajero/courier
    ENTREGADO = "entregado"           # entregado y cobrado
    RECHAZADO = "rechazado"           # cliente rechazó en la puerta
    DEVUELTO = "devuelto"             # devuelto al almacén
    CANCELADO = "cancelado"           # cancelado antes del despacho


class PaymentStatus(str, PyEnum):
    PENDIENTE = "pendiente"           # aún no cobrado (contra entrega)
    COBRADO = "cobrado"               # cobrado exitosamente
    NO_COBRADO = "no_cobrado"         # rechazado/no se pudo cobrar


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_number: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"), nullable=False)

    # Dirección de entrega (puede diferir de la del cliente)
    delivery_department: Mapped[str] = mapped_column(String(50), nullable=False)
    delivery_city: Mapped[str] = mapped_column(String(100), nullable=False)
    delivery_address: Mapped[str] = mapped_column(Text, nullable=False)
    delivery_reference: Mapped[str | None] = mapped_column(Text)

    # Courier/mensajero
    courier_name: Mapped[str | None] = mapped_column(String(200))
    courier_phone: Mapped[str | None] = mapped_column(String(20))
    tracking_code: Mapped[str | None] = mapped_column(String(100))

    # Totales en BOB
    subtotal: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    delivery_cost: Mapped[float] = mapped_column(Float, default=0.0)
    discount: Mapped[float] = mapped_column(Float, default=0.0)
    total: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)

    # Estado
    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus), default=OrderStatus.PENDIENTE
    )
    payment_status: Mapped[PaymentStatus] = mapped_column(
        Enum(PaymentStatus), default=PaymentStatus.PENDIENTE
    )

    notes: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
    delivered_at: Mapped[datetime | None] = mapped_column(DateTime)

    customer: Mapped["Customer"] = relationship("Customer", back_populates="orders")
    items: Mapped[list["OrderItem"]] = relationship(
        "OrderItem", back_populates="order", cascade="all, delete-orphan"
    )


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)     # precio al momento de la venta
    subtotal: Mapped[float] = mapped_column(Float, nullable=False)

    order: Mapped["Order"] = relationship("Order", back_populates="items")
    product: Mapped["Product"] = relationship("Product", back_populates="order_items")
