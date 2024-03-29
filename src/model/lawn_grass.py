from src.model.object_creation_mixin import ObjectCreationMixin
from src.model.product import Product


class LawnGrass(Product):
    country: str
    germination_period: int
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError
