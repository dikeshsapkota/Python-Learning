def greet_user(name):
    return f"Hello {name}, welcome to Python!"


def calculate_total(price, quantity):
    return price * quantity


def is_adult(age):
    return age >= 18


print(greet_user("Dikesh"))
print("Total price:", calculate_total(250, 4))
print("Is adult:", is_adult(21))
