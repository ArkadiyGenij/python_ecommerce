import json

from src.model.category import Category
from src.model.product import Product

with open('../../products.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


def get_category():
    categories = []

    for objects in data:
        category = Category(objects['name'],
                            objects['description'],
                            [product['name'] for product in objects['products']])
        categories.append(category)

    return categories


def get_products():
    products = []

    for category_data in data:
        for product_data in category_data['products']:
            product = Product(product_data['name'],
                              product_data['description'],
                              product_data['price'],
                              product_data['quantity'])
            products.append(product)

    return products


categories_list = get_category()
products_list = get_products()


def view_result():
    print("Категории:")
    print("_______________________________________________________________")
    for category in categories_list:
        print(category)
        print("_______________________________________________________________")
    print("Товары:")
    print("_______________________________________________________________")
    for product in products_list:
        print(product)
        print("_______________________________________________________________")


if __name__ == '__main__':
    view_result()
