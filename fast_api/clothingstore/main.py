from fastapi import FastAPI
from src.routes.product_routes import router as product_router

app = FastAPI()

app.include_router(product_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Clothing Store API!"}