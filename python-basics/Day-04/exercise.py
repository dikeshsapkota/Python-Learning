#1
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def total_stock_value(self):
        return self.price * self.stock
    def is_in_stock(self):
        return (self.stock>0)
    def get_summary(self):
      print(f"{self.name}| {self.price}| {self.stock}")
                

laptop = Product("Laptop", 80000, 5)
print(laptop.is_in_stock())
mouse = Product("Mouse", 1500, 0)

print(mouse.is_in_stock())
laptop.get_summary()