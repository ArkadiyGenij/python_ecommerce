from src.exception.zero_quantity_error import ZeroQuantityError
from src.model.object_creation_mixin import ObjectCreationMixin
from src.model.product import Product


class Category(ObjectCreationMixin):
    name: str
    description: str
    __products: list

    total_categories = 0
    total_unique_product = 0

    def __init__(self, name, description, products, *args, **kwargs):
        self.name = name
        self.description = description
        self.__products = products
        super().__init__(*args, **kwargs)

        unique_products = set(products)

        Category.total_categories += 1
        Category.total_unique_product += len(unique_products)

    def add_product(self, product: Product):
        try:
            if product.quantity <= 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен.")
        except ZeroQuantityError as e:
            print(e)
        else:
            self.__products.append(product)
            print("Товар успешно добавлен.")
        finally:
            print("Обработка добавления товара завершена.")

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

    def average_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            average_price = total_price / len(self.__products)
            return average_price
        except ZeroDivisionError:
            return 0
