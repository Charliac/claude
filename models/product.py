from datetime import datetime
from sqlalchemy import String, Text, Float, Integer, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    sku: Mapped[str | None] = mapped_column(String(50), unique=True, index=True)
    description: Mapped[str | None] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float, nullable=False)          # precio venta en BOB
    cost: Mapped[float | None] = mapped_column(Float)                    # precio costo en BOB
    stock: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    stock_minimum: Mapped[int] = mapped_column(Integer, default=5)       # alerta stock bajo
    unit: Mapped[str] = mapped_column(String(20), default="unidad")      # unidad, kg, litro, etc.
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    category: Mapped["Category | None"] = relationship("Category", back_populates="products")
    order_items: Mapped[list["OrderItem"]] = relationship("OrderItem", back_populates="product")

    @property
    def low_stock(self) -> bool:
        return self.stock <= self.stock_minimum
