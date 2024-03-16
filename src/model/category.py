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
        self.__products = products

        unique_products = set(products)

        Category.total_categories += 1
        Category.total_unique_product += len(unique_products)

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError

    @property
    def product_list(self):
        for product in self.__products:
            return f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."

    @property
    def get_products(self):
        return self.__products

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)}"

    def __len__(self):
        return len(self.__products)
