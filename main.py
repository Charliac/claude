from fastapi import FastAPI
from database import Base, engine
import models  # noqa: F401 — registra todos los modelos antes de crear tablas
from routers import categories, products, customers, orders, reports

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Inventario y Ventas",
    description=(
        "API para gestión de inventario y pedidos contra entrega en Bolivia. "
        "Moneda: BOB (Bolivianos)."
    ),
    version="1.0.0",
)

app.include_router(categories.router)
app.include_router(products.router)
app.include_router(customers.router)
app.include_router(orders.router)
app.include_router(reports.router)


@app.get("/", tags=["Root"])
def root():
    return {
        "app": "Sistema de Inventario y Ventas",
        "version": "1.0.0",
        "docs": "/docs",
        "moneda": "BOB",
        "pais": "Bolivia",
    }


@app.get("/health", tags=["Root"])
def health():
    return {"status": "ok"}
