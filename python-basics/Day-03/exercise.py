"""products
   ↓
save to products.json
   ↓
read products.json
   ↓
loop through loaded products
   ↓
print"""
import json
products = [
    {"name": "Laptop", "price": 80000, "stock": 5},
    {"name": "Mouse", "price": 1500, "stock": 10},
    {"name": "Keyboard", "price": 3000, "stock": 7}
]
with open("product.json", "w") as file:
    json.dump(products, file, indent=4)
with open("product.json", "r") as file:
    loaded_product = json.load(file)
for product in products:
    print(f"{product["name"]}:{product["price"]}:{product["stock"]}")
 #mini challenege
with open("learning_log.txt","w")as file:
    file.write(f"Day 1 - Python fundamentals\n"
f"Day 2 - Functions and validation\n"
f"Day 3 - Exceptions, files and JSON")
    
    