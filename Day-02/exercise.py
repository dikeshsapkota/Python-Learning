""" 1-Build a simple checkout calculator.

The terminal should behave approximately like:

Enter product name: Keyboard
Enter product price: 3000
Enter quantity: 2


Product: Keyboard
Price: Rs. 3000
Quantity: 2
Total: Rs. 6000"""
#2 — Add discount
#3 — Validation
def total_price(price, quantity):
    return price * quantity


def discounted_price(price, quantity, discount):
    subtotal = total_price(price, quantity)
    discount_amount = subtotal * (discount / 100)
    final_price = subtotal - discount_amount
    return final_price


while True:
    name = input("Enter product name: ")

    if name == "":
        print("Invalid name. Please try again.")
    else:
        break


while True:
    price = float(input("Enter product price: "))

    if price <= 0:
        print("Invalid price. Please try again.")
    else:
        break


while True:
    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity. Please try again.")
    else:
        break


while True:
    discount = float(input("Enter discount percentage: "))

    if discount < 0 or discount > 100:
        print("Invalid discount. Enter a value between 0 and 100.")
    else:
        break


subtotal = total_price(price, quantity)
final_total = discounted_price(price, quantity, discount)


print("\n----- ORDER SUMMARY -----")
print(f"Product: {name}")
print(f"Price: Rs. {price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: Rs. {subtotal}")
print(f"Discount: {discount}%")
print(f"Final Total: Rs. {final_total}")