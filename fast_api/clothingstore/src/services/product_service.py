class ProductService:
    def __init__(self):
        self.products = [
            {"id": 1, "name": "T-Shirt", "description": "Cotton T-Shirt", "price": 19.99, "category": "Clothing"},
            {"id": 2, "name": "Jeans", "description": "Blue Denim Jeans", "price": 49.99, "category": "Clothing"},
            {"id": 3, "name": "Sneakers", "description": "Comfortable Sneakers", "price": 69.99, "category": "Footwear"},
            {"id": 4, "name": "Jacket", "description": "Warm Winter Jacket", "price": 89.99, "category": "Outerwear"},
            {"id": 5, "name": "Hat", "description": "Stylish Hat", "price": 15.99, "category": "Accessories"},
        ]

    def fetch_all_products(self):
        return self.products

    def fetch_product_by_id(self, product_id):
        for product in self.products:
            if product["id"] == product_id:
                return product
        return None