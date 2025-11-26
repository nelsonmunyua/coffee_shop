import pytest
from lib.customer import Customer
from lib.coffee import Coffee

class TestCustomer:
    def test_init_valid(self):
        customer = Customer("Alice")
        assert customer.name == "Alice"
        assert customer.orders() == []

    def test_init_invalid_name_short(self):
        with pytest.raises(ValueError):
            Customer("")

    def test_init_invalid_name_long(self):
        with pytest.raises(ValueError):
            Customer("A" * 16)

    def test_init_invalid_name_type(self):
        with pytest.raises(ValueError):
            Customer(123)

    def test_name_setter_valid(self):
        customer = Customer("Alice")
        customer.name = "Bob"
        assert customer.name == "Bob"

    def test_name_setter_invalid(self):
        customer = Customer("Alice")
        with pytest.raises(ValueError):
            customer.name = ""

    def test_orders(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = customer.create_order(coffee, 4.5)
        assert customer.orders() == [order]

    def test_coffees(self):
        customer = Customer("Alice")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Cappuccino")
        customer.create_order(coffee1, 4.5)
        customer.create_order(coffee2, 5.0)
        customer.create_order(coffee1, 4.0)
        coffees = customer.coffees()
        assert len(coffees) == 2
        assert coffee1 in coffees
        assert coffee2 in coffees

    def test_create_order(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = customer.create_order(coffee, 4.5)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 4.5

    def test_most_aficionado(self):
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee = Coffee("Latte")
        customer1.create_order(coffee, 4.5)
        customer1.create_order(coffee, 5.0)
        customer2.create_order(coffee, 3.0)
        aficionado = Customer.most_aficionado(coffee)
        assert aficionado == customer1

    def test_most_aficionado_no_orders(self):
        coffee = Coffee("Latte")
        aficionado = Customer.most_aficionado(coffee)
        assert aficionado is None
