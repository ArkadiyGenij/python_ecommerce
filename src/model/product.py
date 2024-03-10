class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity}"

    @property
    def product_price(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity}"

    @product_price.setter
    def product_price(self, price: float):
        if price <= 0:
            print("Цена введена не корректно!")
        else:
            confirmation = input(f"Вы уверены, что хотите установить цену {price} руб.? (y/n): ")
            if confirmation.lower() == 'y':
                self.price = price
                print("Цена успешно обновлена!")
            else:
                print("Обновление цены отменено.")

    @classmethod
    def create_product(cls, name, description, price, quantity, products):
        for product in products:
            if product.name == name:
                quantity += product.quantity
                if product.price > price:
                    price = product.price

        return cls(name, description, price, quantity)

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity
