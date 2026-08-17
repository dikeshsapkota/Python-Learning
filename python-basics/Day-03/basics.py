#1. try / except
try:
    price=float(input("enter ptice"))
    print(f"price{price}")
except ValueError:
    print("enter valid number")      

#2 File Handling
with open("test.txt","w")as file: #opens the file and automatically closes it afterward.
    file.write("Learning Python")
""""r" → read
"w" → write/overwrite
"a" → append"""
with open("test.txt", "r") as file:
    content = file.read()

print(content)

#3 JSON
import json
product = {
    "name": "Laptop",
    "price": 80000,
    "stock": 5
}
#write json file
with open("product.json", "w") as file:
    json.dump(product, file, indent=4)
#read json file
with open("product.json", "r") as file:
    loaded_product = json.load(file)

print(loaded_product)