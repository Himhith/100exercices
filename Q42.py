# Question:
# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.Use filter() to filter elements of a list.Use lambda to define anonymous functions.


li=[1,2,3,4,5,6,7,8,9,19]

# print(list(filter(lambda: list(map(lambda x: x**2,li),li))))


print(list(filter(lambda x: x%2==0, list(map(lambda y: y**2,li)))))



