#1 
products = [
    {"name": "Laptop", "price": 80000, "stock": 5},
    {"name": "Mouse", "price": 1500, "stock": 0},
    {"name": "Keyboard", "price": 3000, "stock": 7},
    {"name": "Monitor", "price": 25000, "stock": 0},
]
# Filter by stock
in_stock_products=[product for product in products if product["stock"]>0]
# Filter by price
expensive_products =[product for product in products if product["price"]>2000]
# Transform dictionaries → names
product_names=[product["name"] for product in products]
#Dictionary Comprehensions
product_prices={product["name"]: product["price"] for product in products}

print(in_stock_products)
print(expensive_products)
print(product_names)
print(product_prices)