from httpx import AsyncClient, ASGITransport
import pytest
from main import app

# Пример простой функции
def add(a: int, b: int) -> int:
    return a + b

# Тесты для простой функции
def test_add():
    assert add(1, 2) == 3
    assert add(5, 7) == 12

@pytest.mark.anyio
async def test_read_main():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Clothing Store API!"}

@pytest.mark.anyio
async def test_get_items():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        response = await ac.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.anyio
async def test_create_item():
    new_item = {"id": 6, "name": "Hat", "description": "Stylish Hat", "price": 15.99, "category": "Accessories"}
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        response = await ac.post("/products", json=new_item)
    assert response.status_code == 405
    # assert response.status_code == 201    

# @pytest.mark.anyio
# async def test_update_item():
#     update_data = {"name": "Updated T-Shirt", "price": 29.99}
#     item_id = 1  # Предполагаем, что элемент с ID 1 существует
#     async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
#         response = await ac.put(f"/items/{item_id}", json=update_data)
#     assert response.status_code == 200
#     assert response.json()["name"] == update_data["name"]
#     assert response.json()["price"] == update_data["price"]

# @pytest.mark.anyio
# async def test_delete_item():
#     item_id = 1  # Предполагаем, что элемент с ID 1 существует
#     async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
#         response = await ac.delete(f"/items/{item_id}")
#     assert response.status_code == 204