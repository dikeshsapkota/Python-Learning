products = [
    {"name": "Laptop", "price": 80000, "stock": 5},
    {"name": "Mouse", "price": 1500, "stock": 0},
    {"name": "Keyboard", "price": 3000, "stock": 7},
    {"name": "Monitor", "price": 25000, "stock": 2},
    {"name": "Headphones", "price": 5000, "stock": 10},
]
#map + filter
available_products=list(map(lambda product:product["name"],
                        filter(lambda product:product["stock"]>0,products)))
print(available_products)