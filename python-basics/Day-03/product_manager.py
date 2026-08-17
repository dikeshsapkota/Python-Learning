import json
with open("product.json", "r") as file:
   products = json.load(file)
print(products)
for product in products:
    print(f"{product["name"]}|{product["price"]}|{product["stock"]}" )

add_name=input("enter product name")
add_price=int(input("enter price"))
add_stock=int(input("enter stock"))
new_product= {
    "name":add_name,
    "price":add_price,
    "stock":add_stock
}
products.append(new_product)
with open("product.json", "w") as file:
    json.dump(products, file, indent=4)

give_name=input("enter name to be deleted")
found =False
for product in products:
    if(give_name==product["name"]):
        products.remove(product)
        found=True
        break   
if not found:
    print("invalid name")    
with open("product.json", "w") as file:
    json.dump(products, file, indent=4)