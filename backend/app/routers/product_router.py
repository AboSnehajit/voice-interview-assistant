from fastapi import APIRouter
from app.models.product_model import Product

router=APIRouter()

@router.post("/products")
def create_product(product :Product):
    return{
        "message":"Product created successfully",
        "product":product
    }