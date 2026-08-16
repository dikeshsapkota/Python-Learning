#1 Function parameters and return values
def calculate_total(price, quantity):
    total = price * quantity
    return total

result = calculate_total(1500, 3)

print(result)
def greet(name, role="Customer"):
    return f"Welcome {name}, you are logged in as {role}"

print(greet("Dikesh"))
print(greet("Ram", "Seller")) 

#2 user input 
name=input("enter name")
print(f"hello {name}")

#3 Type conversion
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"Total: Rs. {total}")

#4 while loop 
number = 1

while number <= 5:
    print(number)
    number += 1

#4 while true
while True:
    command = input("Enter 'exit' to quit: ")

    if command == "exit":
        break

    print(f"You entered: {command}")
    