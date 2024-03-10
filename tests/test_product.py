import pytest

from src.model.product import Product


@pytest.fixture()
def product():
    return Product('Филе куриное', 'Филе курицы, очищенное', 300, 15)


@pytest.fixture()
def sample_product():
    return [
        Product('Чипсы', 'Новый вкус! Лук и барсук!', 120, 10),
        Product('Йогурт', 'Очень вкусный йогурт!', 70, 20)
    ]


def test_product_str(product):
    assert product.__str__() == 'Филе куриное - Филе курицы, очищенное - 300'


def test_product_init(product):
    assert product.name == 'Филе куриное'
    assert product.description == 'Филе курицы, очищенное'
    assert product.price == 300
    assert product.quantity == 15


def test_product_price_get(product):
    assert product.product_price == f"Цена товара: 300 руб."


def test_product_price_zero(product, capsys):
    product.product_price = 0
    captured = capsys.readouterr()
    assert "Цена введена не корректно!" in captured.out


def test_product_price_negative(product, capsys):
    product.product_price = -5
    captured = capsys.readouterr()
    assert "Цена введена не корректно!" in captured.out


def test_product_price_confirmation(product, capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    product.product_price = 10.0
    captured = capsys.readouterr()
    assert "Цена успешно обновлена!" in captured.out


def test_product_price_cancel(product, capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    product.product_price = 15.0
    captured = capsys.readouterr()
    assert "Обновление цены отменено." in captured.out


def test_product_price_other(product, capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'z')
    product.product_price = 15.0
    captured = capsys.readouterr()
    assert "Обновление цены отменено." in captured.out


def test_create_product_new_product(sample_product):
    new_product = Product.create_product("Новый продукт", "Новое описание", 100, 20, sample_product)
    assert new_product.name == "Новый продукт"
    assert new_product.description == "Новое описание"
    assert new_product.price == 100
    assert new_product.quantity == 20


def test_create_product_existing_product_price(sample_product):
    new_product = Product.create_product("Чипсы", "Новый вкус! Лук и барсук!", 130, 7, sample_product)
    assert new_product.name == "Чипсы"
    assert new_product.description == "Новый вкус! Лук и барсук!"
    assert new_product.price == 130
    assert new_product.quantity == 17


def test_create_product_price(sample_product):
    new_product = Product.create_product("Чипсы", "Новый вкус! Лук и барсук!", 110, 2, sample_product)
    assert new_product.name == "Чипсы"
    assert new_product.description == "Новый вкус! Лук и барсук!"
    assert new_product.price == 120
    assert new_product.quantity == 12
