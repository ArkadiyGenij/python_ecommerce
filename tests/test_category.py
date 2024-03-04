import pytest

from model.category import Category
from model.product import Product


@pytest.fixture()
def category():
    return Category('Еда', 'Продукты питания на каждый день', ['Морковь', 'Лук', 'Гречка'])


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


def test_category_init(category):
    assert category.name == 'Еда'
    assert category.description == 'Продукты питания на каждый день'
    assert category.products == ['Морковь', 'Лук', 'Гречка']


def test_category_total_count(electronics_category, clothing_category):
    assert Category.total_categories == 2


def test_unique_product_count(electronics_category, clothing_category):
    assert Category.total_unique_product == 4
