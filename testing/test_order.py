import pytest
from lib.order import Order
from lib.customer import Customer
from lib.coffee import Coffee

class TestOrder:
    def test_init_valid(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 4.5)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 4.5
        assert order in customer.orders()
        assert order in coffee.orders()

    def test_init_invalid_customer(self):
        coffee = Coffee("Latte")
        with pytest.raises(ValueError):
            Order("not a customer", coffee, 4.5)

    def test_init_invalid_coffee(self):
        customer = Customer("Alice")
        with pytest.raises(ValueError):
            Order(customer, "not a coffee", 4.5)

    def test_init_invalid_price_low(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.5)

    def test_init_invalid_price_high(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        with pytest.raises(ValueError):
            Order(customer, coffee, 15.0)

    def test_init_invalid_price_type(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        with pytest.raises(ValueError):
            Order(customer, coffee, "4.5")

    def test_price_setter_valid(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 4.5)
        order.price = 5.0
        assert order.price == 5.0

    def test_price_setter_invalid(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 4.5)
        with pytest.raises(ValueError):
            order.price = 0.5
