#1
"""
Day 4 - Object-Oriented Programming (OOP) and JSON to Objects

Topics:
- Classes and Objects
- __init__ constructor
- self keyword
- Attributes
- Methods
- Creating objects from a class
- Reading JSON data
- Converting JSON dictionaries into Product objects
- Storing objects inside a list
- Calling methods on objects

In this exercise:
1. Product class acts as a blueprint for products.
2. __init__ initializes name, price, and stock.
3. total_stock_value() calculates the total inventory value.
4. is_in_stock() checks whether the product has available stock.
5. get_summary() returns product information.
6. product.json is loaded using json.load().
7. Each dictionary from JSON is converted into a Product object.
8. Product objects are stored inside product_objects.
"""
import json
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
        return(f"{self.name}| {self.price}| {self.stock}")
              

with open("product.json", "r") as file:
    products = json.load(file)
product_objects=[] 
for product in products:
   product_object= Product(product["name"],product["price"],product["stock"])
   product_objects.append(product_object) 
        
          
for product in product_objects:
    product.get_summary()