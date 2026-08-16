name = input("Enter product name")
if name == "":
    print("name invalid")
price = float(input("Enter product price"))
if price <= 0:
    print("invalid price")
quantity = int(input("Enter Quantity"))
if quantity <= 0:
    print("invalid quantity")
discount = float(input("Enter discount"))
if discount < 0 or discount > 100:
    print("invalid discount")


def total_price(price, quantity):
    return price * quantity


def discounted_price(price, discount):
    return total_price(price, quantity) - (discount * 0.01) * total_price(
        price, quantity
    )


print(
    f"product:{name} \n price={price}\n Quantity:{quantity}\n Total:{total_price(price,quantity)}\n Discount:{discount}\n Discounted price:{discounted_price(price,discount)}"
)
