from fastapi import APIRouter
from src.controllers.product_controller import ProductController
from src.services.product_service import ProductService

router = APIRouter()

# Create an instance of ProductService
product_service = ProductService()

# Pass the product_service instance to ProductController
product_controller = ProductController(product_service)

@router.get("/products")
def get_all_products():
    return product_controller.get_all_products()

@router.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    return product_controller.get_product_by_id(product_id)