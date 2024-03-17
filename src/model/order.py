from src.model.product import Product


class Order:
    product: Product
    quantity: int
    total_price: float

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        return self.product.price * self.quantity
