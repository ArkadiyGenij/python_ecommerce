from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def calculate_total_price(self):
        pass

    @abstractmethod
    def product_price(self):
        pass

    @classmethod
    @abstractmethod
    def create_product(cls, name, description, price, quantity):
        pass
