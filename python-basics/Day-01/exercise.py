#1 

price = 1000
discount_percentage = 10
def calculate_discount(price, discount_percentage):
    
   final_price=price-(price*discount_percentage/100)
   return final_price
print(f" original price {price} and discount percentage {discount_percentage} ")

print(f"final price {calculate_discount(price, discount_percentage)}")

#2 print only names of price >2000 and  #3 ecommerce or project logic
products = [
    {"name": "Laptop", "price": 80000, "stock": 5},
    {"name": "Mouse", "price": 1500, "stock": 0},
    {"name": "Keyboard", "price": 3000, "stock": 10},
    {"name": "Monitor", "price": 25000, "stock": 0},
]
total_inventory_value = 0
for product in products:
    if product["price"]>2000:
        print(product["name"])

for product in products:
    if product["stock"] > 0:
        print (f"in Stock {product["name"]} at price {product["price"]}")
        total_stock_price=product["price"] * product["stock"]
        total_inventory_value+=total_stock_price
        
    else:
        print (f"Out of Stock {product["name"]}")

 #final exercise day 1:
 
print(f"total value is {total_inventory_value}")


   