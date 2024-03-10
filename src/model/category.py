from src.model.product import Product


class Category:
    name: str
    description: str
    __products: list

    total_categories = 0
    total_unique_product = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        unique_products = set(products)

        Category.total_categories += 1
        Category.total_unique_product += len(unique_products)

    def add_product(self, product: Product):
        self.products.append(product)

    @property
    def product_list(self):
        for product in self.products:
            return f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."

    def __str__(self):
        return f"{self.name} - {self.description}"
