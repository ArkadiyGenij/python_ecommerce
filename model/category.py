class Category:
    name: str
    description: str
    products: list

    category_count = 0
    unique_product = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

    def __str__(self):
        return f"{self.name} - {self.description}"
