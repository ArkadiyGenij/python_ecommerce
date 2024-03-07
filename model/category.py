class Category:
    name: str
    description: str
    products: list

    total_categories = 0
    total_unique_product = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        unique_products = set(products)

        Category.total_categories += 1
        Category.total_unique_product += len(unique_products)

    def __str__(self):
        return f"{self.name} - {self.description}"
