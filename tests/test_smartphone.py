import pytest

from src.model.smartphone import Smartphone
from tests.test_product import product


@pytest.fixture
def smartphone_iphone():
    return Smartphone('IPhone 14', 'Андроид все равно лучше!', 60000, 10, 'Apple', 'IPhone 14', 256, 'Белый')


@pytest.fixture
def smartphone_samsung():
    return Smartphone('Samsung S24', 'Андроид это круто!', 70000, 5, 'Samsung', 'Samsung S24', 256, 'Белый')


def test_smartphone_init(smartphone_samsung):
    assert smartphone_samsung.name == 'Samsung S24'
    assert smartphone_samsung.description == 'Андроид это круто!'
    assert smartphone_samsung.price == 70000
    assert smartphone_samsung.quantity == 5
    assert smartphone_samsung.manufacturer == 'Samsung'
    assert smartphone_samsung.memory == 256
    assert smartphone_samsung.model == 'Samsung S24'
    assert smartphone_samsung.color == 'Белый'


def test_lawn_grass_add(smartphone_samsung, smartphone_iphone):
    assert smartphone_samsung.__add__(smartphone_iphone) == 950000


def test_lawn_grass_add_error(smartphone_samsung, product):
    try:
        smartphone_samsung.__add__(product)
    except TypeError:
        pass
