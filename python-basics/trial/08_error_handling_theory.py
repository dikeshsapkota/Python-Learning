# Error handling helps a program respond to problems without crashing.
# try runs code that might fail, and except handles a specific type of error.


def divide_numbers(first_number, second_number):
    try:
        result = first_number / second_number
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."


print(divide_numbers(10, 2))
print(divide_numbers(10, 0))

try:
    user_age = int("twenty")
    print(f"User age is {user_age}")
except ValueError:
    print("Error: Please enter age as a number.")
