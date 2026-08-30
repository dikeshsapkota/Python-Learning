fruits = ["apple", "banana", "mango"]

fruits.append("orange")
print("Fruit list:", fruits)
print("First fruit:", fruits[0])

student = {
    "name": "Dikesh",
    "course": "Python Basics",
    "level": "Beginner",
}

print("Student name:", student["name"])
print("Course:", student["course"])

for fruit in fruits:
    print(f"I like {fruit}")
