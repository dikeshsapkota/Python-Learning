def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        return "Cannot divide by zero"

    return first_number / second_number


print("Mini Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose an option 1-4: ")
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

if choice == "1":
    result = add(first_number, second_number)
elif choice == "2":
    result = subtract(first_number, second_number)
elif choice == "3":
    result = multiply(first_number, second_number)
elif choice == "4":
    result = divide(first_number, second_number)
else:
    result = "Invalid option"

print("Result:", result)
