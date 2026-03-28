from datetime import datetime
from pydantic import BaseModel, ConfigDict

BOLIVIA_DEPARTMENTS = [
    "La Paz", "Santa Cruz", "Cochabamba", "Oruro", "Potosí",
    "Chuquisaca", "Tarija", "Beni", "Pando"
]


class CustomerBase(BaseModel):
    full_name: str
    phone: str
    phone_alt: str | None = None
    email: str | None = None
    department: str
    city: str
    address: str
    reference: str | None = None
    notes: str | None = None


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    full_name: str | None = None
    phone: str | None = None
    phone_alt: str | None = None
    email: str | None = None
    department: str | None = None
    city: str | None = None
    address: str | None = None
    reference: str | None = None
    notes: str | None = None


class CustomerOut(CustomerBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
