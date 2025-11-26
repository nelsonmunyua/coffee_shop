import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.coffee import Coffee
from lib.customer import Customer
from lib.order import Order

class TestCoffee:
    def test_init_valid(self):
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"
        assert coffee.orders() == []
        assert coffee.customers() == []
        assert coffee.num_orders() == 0
        assert coffee.average_price() == 0.0

    def test_init_invalid_name(self):
        with pytest.raises(ValueError):
            Coffee("ab")  # less than 3 characters
        with pytest.raises(ValueError):
            Coffee(123)  # not a string

    def test_name_setter(self):
        coffee = Coffee("Latte")
        coffee.name = "Mocha"
        assert coffee.name == "Mocha"
        with pytest.raises(ValueError):
            coffee.name = "ab"
        with pytest.raises(ValueError):
            coffee.name = 123

    def test_orders_and_customers(self):
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee = Coffee("Espresso")
        order1 = Order(customer1, coffee, 3.5)
        order2 = Order(customer2, coffee, 4.0)
        order3 = Order(customer1, coffee, 5.0)
        orders = coffee.orders()
        customers = coffee.customers()
        assert len(orders) == 3
        assert set(customers) == {customer1, customer2}

    def test_num_orders_and_average_price(self):
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee = Coffee("Cappuccino")
        Order(customer1, coffee, 4.0)
        Order(customer2, coffee, 6.0)
        Order(customer1, coffee, 5.0)
        assert coffee.num_orders() == 3
        assert pytest.approx(coffee.average_price(), 0.01) == (4.0 + 6.0 + 5.0) / 3
