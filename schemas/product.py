from datetime import datetime
from pydantic import BaseModel, ConfigDict, field_validator


class ProductBase(BaseModel):
    name: str
    sku: str | None = None
    description: str | None = None
    price: float
    cost: float | None = None
    stock: int = 0
    stock_minimum: int = 5
    unit: str = "unidad"
    is_active: bool = True
    category_id: int | None = None

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        return v

    @field_validator("stock", "stock_minimum")
    @classmethod
    def stock_not_negative(cls, v: int) -> int:
        if v < 0:
            raise ValueError("El stock no puede ser negativo")
        return v


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = None
    sku: str | None = None
    description: str | None = None
    price: float | None = None
    cost: float | None = None
    stock: int | None = None
    stock_minimum: int | None = None
    unit: str | None = None
    is_active: bool | None = None
    category_id: int | None = None


class StockAdjust(BaseModel):
    quantity: int
    reason: str | None = None   # "compra", "devolucion", "ajuste", "danio"


class ProductOut(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    low_stock: bool
    created_at: datetime
    updated_at: datetime


class ProductLowStock(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    sku: str | None
    stock: int
    stock_minimum: int
