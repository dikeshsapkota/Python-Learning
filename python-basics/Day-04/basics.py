#1 class , encapsulation, inheritence
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def total_stock_value(self):
        return self.price * self.stock
    def update_stock(self,amount):
        self.stock+=amount
        return self.stock
#inheritence and super()which runs parent's constructor
class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
class Customer(User):
    def __init__(self,name,email,address):
        super().__init__(name,email)
        self.address=address



laptop = Product("Laptop", 80000, 5)
laptop.update_stock(3)
print(laptop.name)
print(laptop.price)
print(laptop.stock)
print(laptop.total_stock_value())
