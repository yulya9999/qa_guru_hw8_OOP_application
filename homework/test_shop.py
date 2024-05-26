"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # напишите проверки на метод check_quantity
        assert product.check_quantity(1000) is True
        assert product.check_quantity(589) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # напишите проверки на метод buy
        assert product.buy(50) == 950

    def test_product_buy_more_than_available(self, product):
        # напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии

        with pytest.raises(ValueError):
            assert product.buy(5000)


class TestCart:
    """
        Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_products(self, cart, product):
        cart.add_product(product, 2)
        assert product in cart.products
        assert cart.products[product] == 2

    def test_remove_product(self, cart, product):
        cart.add_product(product, 2)
        cart.remove_product(product, 1)
        assert cart.products[product] == 1

        cart.remove_product(product)
        assert product not in cart.products

    def test_clear(self, cart, product):
        cart.add_product(product, 2)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 5)
        assert cart.get_total_price() == 500

    def test_buy(self, cart, product):
        cart.add_product(product, 5000)
        with pytest.raises(ValueError):
            assert cart.buy()
