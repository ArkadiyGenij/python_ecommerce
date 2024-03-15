import pytest

from src.model.category import Category
from src.model.product import Product
from tests.test_product import product


@pytest.fixture()
def food_category():
    carrot = Product("Морковь", "Оранжевая и очень вкусная!", 70, 15)
    onion = Product("Лук", "Не очень вкусный, но очень полезный!", 30, 50)
    return Category('Еда', 'Продукты питания на каждый день', [carrot, onion])


@pytest.fixture()
def electronics_category():
    iphone = Product("iPhone", "Смартфон", 1000, 50)
    macbook = Product("MacBook", "Ноутбук", 1500, 30)
    return Category("Электроника", "Технические устройства", [iphone, macbook])


@pytest.fixture()
def clothing_category():
    tshirt = Product("Футболка", "Футболка с логотипом", 20, 100)
    jeans = Product("Джинсы", "Джинсы стандартной длины", 30, 80)
    return Category("Одежда", "Одежда и аксессуары", [tshirt, jeans])


@pytest.fixture(autouse=True)
def reset_category_counts():
    Category.total_categories = 0
    Category.total_unique_product = 0


def test_str_func(food_category):
    assert food_category.__str__() == "Еда, количество продуктов: 2"


def test_category_init(food_category):
    assert food_category.name == 'Еда'
    assert food_category.description == 'Продукты питания на каждый день'
    assert food_category.get_products[0] == food_category.get_products[0]
    assert food_category.get_products[1] == food_category.get_products[1]


def test_category_total_count(electronics_category, clothing_category):
    assert Category.total_categories == 2


def test_unique_product_count(electronics_category, clothing_category):
    assert Category.total_unique_product == 4


def test_add_product_in_products(product, food_category):
    food_category.add_product(product)
    assert product in food_category.get_products


def test_product_list(food_category):
    assert food_category.product_list == "Морковь, 70 руб. Остаток: 15 шт."


def test_len_product_list(food_category):
    assert food_category.__len__() == 2
