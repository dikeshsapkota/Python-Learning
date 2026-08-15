""""
js vs python
const / let      → not needed
true             → True
false            → False
null             → None
;                → not needed
camelCase        → snake_case is preferred
"""
skills = ["JavaScript", "React", "Node.js"]#arrays but in py it is list

user = {
    "name": "Dikesh",
    "role": "Developer",
    "age": 21
}#objects but in py it is dictionary

technologies = {"React", "Python", "FastAPI"} #sets are unordered and unindexed collection of unique elements

coordinates = (27.7172, 85.3240)#tuples are ordered and unchangeable collection of elements

#lets access them 
print(skills[-2])
print(user["name"])
print(technologies)
print(coordinates[0])

#conditions
age = 21

if age >= 18:
    print("Adult")
else:
    print("Minor")

#loops
for skill in skills:
    print(f"i know {skill}")    #python's version of `I know ${skill}`

#functions 
def greet(name):
    return f"Hello {name}"

print(greet("Dikesh"))    