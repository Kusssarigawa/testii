class ProductController:
    def __init__(self, product_service):
        self.product_service = product_service

    def get_all_products(self):
        return self.product_service.fetch_all_products()

    def get_product_by_id(self, product_id):
        return self.product_service.fetch_product_by_id(product_id)