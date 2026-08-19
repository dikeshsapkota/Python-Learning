"""1. List comprehensions
2. Dictionary comprehensions
3. Lambda functions
4. map()
5. filter()
6. Type hints
7. *args / **kwargs
8. Packages, pip & imports
9. Small challenge"""
#list comprehension
numbers=[1,2,3,4,5]
squares=[number*number for number in numbers]
""" for number in numbers:
    squares.append(number*number)"""
print(squares)
# filtering
prices = [1000, 5000, 800, 10000, 2500]

expensive = [price for price in prices if price>2000]
"""normal approach
for price in prices:
    if price > 2000:
        expensive.append(price)
"""
print (expensive)