# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

# Hints:
# Use map() to generate a list. Use lambda to define anonymous functions.


li= [num+1 for num in range(20)]

print(li)
print(list(map(lambda num: num*num,li)))
# print(map(lambda num: num*num,li))

# Question 45
# Question:
# Define a class named American which has a static method called printNationality.

# Hints:
# Use @staticmethod decorator to define class static method.There are also two more methods.To know more, go to this link.


class American(object):
	"""docstring for American"""
	def __init__(self):
		super(American, self).__init__()

	@staticmethod
	def printNationality():
		return print("American"	)
		


obj= American()

obj.printNationality()	 

American.printNationality()

# Question 46:
# Define a class named American and its subclass NewYorker.

# Hints:
# Use class Subclass(ParentClass) to define a subclass.*


class NewYorker(American):
	"""docstring for NewYorker"""
	def __init__(self, arg):
		super(NewYorker, self).__init__()
		self.arg = arg


print(NewYorker.__name__)
NewYorker.printNationality()