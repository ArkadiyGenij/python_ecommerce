import pytest

from model.category import Category


@pytest.fixture()
def category():
    return Category('Еда', 'Продукты питания на каждый день', ['Морковь', 'Лук', 'Гречка'])


def test_category_init(category):
    assert category.name == 'Еда'
    assert category.description == 'Продукты питания на каждый день'
    assert category.products == ['Морковь', 'Лук', 'Гречка']


def test_count_products(category):
    assert len(category.products) == 3


def test_count_categories():
    assert Category.category_count == 0


def test_unique_products(category):
    unique_products = set(category.products)
    assert len(unique_products) == len(category.products)
