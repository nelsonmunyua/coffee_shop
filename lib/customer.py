class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not 1 <= len(name) <= 15:
            raise ValueError("Name must be a string between 1 and 15 characters")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not 1 <= len(value) <= 15:
            raise ValueError("Name must be a string between 1 and 15 characters")
        self._name = value

    def orders(self):
        return self._orders.copy()

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        from .order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        if not hasattr(coffee, '_orders'):
            return None
        customers = {}
        for order in coffee._orders:
            customer = order.customer
            customers[customer] = customers.get(customer, 0) + order.price
        if not customers:
            return None
        return max(customers, key=customers.get)
