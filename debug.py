from customer import Customer
from coffee import Coffee
from order import Order

# Create Customers
alice = Customer("Alice")
bob = Customer("Bob")
carol = Customer("Carol")

# Create Coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")
cappuccino = Coffee("Cappuccino")

# Place Orders
alice.create_order(latte, 5.0)
alice.create_order(latte, 5.5)
alice.create_order(espresso, 4.0)

bob.create_order(latte, 6.0)
bob.create_order(cappuccino, 4.5)

carol.create_order(latte, 7.0)
carol.create_order(espresso, 5.0)

# Display Orders
print("Orders for Alice:", alice.orders())
print("Coffees ordered by Alice:", [c.name for c in alice.coffees()])
print("Orders for Latte:", latte.orders())
print("Customers who ordered Latte:", [c.name for c in latte.customers()])

# Average spending of Alice
average_spent = sum([order.price for order in alice.orders()]) / len(alice.orders())
print(f"Alice's average spending: ${average_spent:.2f}")

# Total number of orders for a coffee
print(f"Total orders for Latte: {latte.num_orders()}")

# Average price of a coffee
print(f"Average price for Latte: ${latte.average_price():.2f}")

# Most aficionado (highest spender) for Latte
aficionado = Customer.most_aficionado(latte)
if aficionado:
    print(f"Most aficionado for Latte: {aficionado.name}")
else:
    print("No orders for this coffee.")

# Try some invalid values to trigger exceptions (Uncomment to test)
# bad_customer = Customer("")                # Should raise ValueError
# bad_coffee = Coffee("AB")                  # Should raise ValueError
# bad_order = Order(alice, latte, 0.5)       # Should raise ValueError

