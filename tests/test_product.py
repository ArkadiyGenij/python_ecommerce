import pytest

from model.product import Product


@pytest.fixture()
def product():
    return Product('Филе куриное', 'Филе курицы, очищенное', 300, 15)


def test_product_init(product):
    assert product.name == 'Филе куриное'
    assert product.description == 'Филе курицы, очищенное'
    assert product.price == 300
    assert product.quantity == 15
