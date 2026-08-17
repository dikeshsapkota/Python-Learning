#1 class 
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def total_stock_value(self):
        return self.price * self.stock
laptop = Product("Laptop", 80000, 5)

print(laptop.name)
print(laptop.price)
print(laptop.stock)
print(laptop.total_stock_value())