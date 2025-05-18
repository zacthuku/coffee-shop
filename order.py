class Order:
    all=[]
    def __init__(self, customer, coffee, price):
        self.customer=customer
        self.coffee=coffee
        self.price=price
        Order.all.append(self)
    
    @property
    def customer (self):
        return self._customer 
    @customer.setter
    def 