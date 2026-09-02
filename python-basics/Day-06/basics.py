#lamda, sorted(), map(), filter()
products = [
    {"name": "Laptop", "price": 80000, "stock": 5},
    {"name": "Mouse", "price": 1500, "stock": 0},
    {"name": "Keyboard", "price": 3000, "stock": 7},
    {"name": "Monitor", "price": 25000, "stock": 2},
]
sorted_by_stock=sorted(
    products,
    key=lambda product: product["stock"],    
    reverse=True
)
print(sorted_by_stock)    
