import pytest

from src.model.lawn_grass import LawnGrass
from tests.test_product import product


@pytest.fixture
def lawn_grass_green():
    return LawnGrass('Трава зеленая', 'Очень зеленая трава', 1000, 15, 'Россия', 3, 'Зеленый')


@pytest.fixture
def lawn_grass_red():
    return LawnGrass('Трава красная', 'Очень красная трава', 1100, 10, 'Россия', 1, 'Красный')


def test_lawn_grass_init(lawn_grass_green):
    assert lawn_grass_green.name == 'Трава зеленая'
    assert lawn_grass_green.description == 'Очень зеленая трава'
    assert lawn_grass_green.price == 1000
    assert lawn_grass_green.quantity == 15
    assert lawn_grass_green.country == 'Россия'
    assert lawn_grass_green.germination_period == 3
    assert lawn_grass_green.color == 'Зеленый'


def test_lawn_grass_add(lawn_grass_green, lawn_grass_red):
    assert lawn_grass_green.__add__(lawn_grass_red) == 26000


def test_lawn_grass_add_error(lawn_grass_green, product):
    try:
        lawn_grass_green.__add__(product)
    except TypeError:
        pass
