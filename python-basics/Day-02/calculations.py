def total_price(price, quantity):
    return price * quantity


def discounted_price(price, quantity, discount):
    subtotal = total_price(price, quantity)
    discount_amount = subtotal * (discount / 100)
    return subtotal - discount_amount