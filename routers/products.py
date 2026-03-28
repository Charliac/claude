from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from database import get_db
from models.product import Product
from models.category import Category
from schemas.product import ProductCreate, ProductUpdate, ProductOut, ProductLowStock, StockAdjust

router = APIRouter(prefix="/products", tags=["Productos"])


@router.get("/", response_model=list[ProductOut])
def list_products(
    search: str | None = Query(None, description="Buscar por nombre o SKU"),
    category_id: int | None = None,
    active_only: bool = True,
    db: Session = Depends(get_db),
):
    q = db.query(Product)
    if active_only:
        q = q.filter(Product.is_active == True)
    if category_id:
        q = q.filter(Product.category_id == category_id)
    if search:
        q = q.filter(
            Product.name.ilike(f"%{search}%") | Product.sku.ilike(f"%{search}%")
        )
    return q.order_by(Product.name).all()


@router.get("/low-stock", response_model=list[ProductLowStock])
def list_low_stock(db: Session = Depends(get_db)):
    """Productos con stock igual o por debajo del mínimo configurado."""
    products = db.query(Product).filter(
        Product.is_active == True,
        Product.stock <= Product.stock_minimum,
    ).order_by(Product.stock).all()
    return products


@router.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    if data.sku:
        existing = db.query(Product).filter(Product.sku == data.sku).first()
        if existing:
            raise HTTPException(status_code=400, detail="Ya existe un producto con ese SKU")
    if data.category_id:
        if not db.query(Category).filter(Category.id == data.category_id).first():
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
    product = Product(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product


@router.patch("/{product_id}", response_model=ProductOut)
def update_product(product_id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    if data.category_id is not None:
        if not db.query(Category).filter(Category.id == data.category_id).first():
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
    for field, value in data.model_dump(exclude_none=True).items():
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    return product


@router.post("/{product_id}/stock/adjust", response_model=ProductOut)
def adjust_stock(product_id: int, data: StockAdjust, db: Session = Depends(get_db)):
    """
    Ajusta el stock del producto. Use cantidad positiva para aumentar
    (entrada de mercadería) y negativa para reducir (baja por daño, etc.).
    """
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    new_stock = product.stock + data.quantity
    if new_stock < 0:
        raise HTTPException(
            status_code=400,
            detail=f"Stock insuficiente. Stock actual: {product.stock}"
        )
    product.stock = new_stock
    db.commit()
    db.refresh(product)
    return product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def deactivate_product(product_id: int, db: Session = Depends(get_db)):
    """Desactiva el producto (soft delete). No se eliminan datos históricos."""
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    product.is_active = False
    db.commit()
