from customer import Customer
from coffee import Coffee

c1 = Customer("Zach")
c2 = Customer("Milly")
latte = Coffee("Latte")
mocha = Coffee("Mocha")

c1.create_order(latte, 4.5)
c1.create_order(mocha, 5.0)
c2.create_order(latte, 6.0)
c2.create_order(latte, 3.5)

print(f"Aficionado for Latte: {Customer.most_aficionado(latte).name}")
