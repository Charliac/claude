from datetime import datetime
from sqlalchemy import String, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

# Departamentos de Bolivia
BOLIVIA_DEPARTMENTS = [
    "La Paz", "Santa Cruz", "Cochabamba", "Oruro", "Potosí",
    "Chuquisaca", "Tarija", "Beni", "Pando"
]


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(200), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    phone_alt: Mapped[str | None] = mapped_column(String(20))
    email: Mapped[str | None] = mapped_column(String(200), index=True)
    department: Mapped[str] = mapped_column(String(50), nullable=False)  # departamento Bolivia
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    address: Mapped[str] = mapped_column(Text, nullable=False)
    reference: Mapped[str | None] = mapped_column(Text)                  # referencia de ubicación
    notes: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    orders: Mapped[list["Order"]] = relationship("Order", back_populates="customer")
