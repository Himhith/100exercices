#  q35 Question:
# Define a function which can generate a list where the values 
# are square of numbers between 1 and 20 (both included).
#  Then the function needs to print the last 5 elements in the list.

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append()
#  to add values into a list.Use [n1:n2] to slice a list

# q36 Define a function which can generate a list where the values are square of numbers
#  between 1 and 20 (both included). Then the function needs to print all values except
#   the first 5 elements in the list.

# q37 Define a function which can generate and print a tuple where the value are square of 
# numbers between 1 and 20 (both included).

def q35():
	li=[i**2 for i in range(1,21) ]
	print(f'first elements: {li[:5]} \n last elements: {li[(len(li)-5):]} ')

q35()

def q36():
	li=[i**2 for i in range(1,21) ]
	print(f'elements after fifth: {li[5:]} \n ')

q36()

def q37():
	tpl=tuple([i**2 for i in range(1,21)])
	print(f'tuple elem {tpl}' )

q37()