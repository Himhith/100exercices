# Question:
# Define a function 
# which can print a dictionary where the keys are numbers between 1 and 20 (both included) 
# and the values are square of keys.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary
# .Use ** operator to get power of a number.Use range() for loops.


def func():
	dict={}
	i=20
	for key in range(1,21):
		dict[key]=key**2
	print (dict)

func()