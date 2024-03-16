from src.model.product import Product


class Smartphone(Product):
    manufacturer: str
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, manufacturer, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.manufacturer = manufacturer
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError
