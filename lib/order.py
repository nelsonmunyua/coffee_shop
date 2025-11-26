class Order:
    def __init__(self, customer, coffee, price):
        if not (hasattr(customer, '_orders') and type(customer).__name__ == 'Customer'):
            raise ValueError("Invalid customer")
        if not (hasattr(coffee, '_orders') and type(coffee).__name__ == 'Coffee'):
            raise ValueError("Invalid coffee")
        if not isinstance(price, (int, float)) or not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        customer._orders.append(self)
        coffee._orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = value
