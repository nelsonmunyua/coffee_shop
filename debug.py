#!/usr/bin/env python3

from lib.customer import Customer
from lib.coffee import Coffee

# Create some customers and coffees
customer1 = Customer("Alice")
customer2 = Customer("Bob")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Cappuccino")

# Create some orders
order1 = customer1.create_order(coffee1, 4.5)
order2 = customer1.create_order(coffee2, 5.0)
order3 = customer2.create_order(coffee1, 4.0)
order4 = customer2.create_order(coffee2, 5.5)

# Test methods
print("Customer1 orders:", len(customer1.orders()))
print("Customer1 coffees:", [c.name for c in customer1.coffees()])
print("Coffee1 orders:", len(coffee1.orders()))
print("Coffee1 customers:", [c.name for c in coffee1.customers()])
print("Coffee1 num_orders:", coffee1.num_orders())
print("Coffee1 average_price:", coffee1.average_price())
print("Most aficionado for coffee1:", Customer.most_aficionado(coffee1).name)
print("Most aficionado for coffee2:", Customer.most_aficionado(coffee2).name)
