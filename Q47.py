# Question
# Define a class named Circle which can be constructed by a radius. 
#  The Circle class has a method which can compute the area.

# Hints
# Use def methodName(self) to define a method.



class Circle(object):
	"""docstring for Circle"""
	def __init__(self, radius):
		
		self.radius = radius
	def area(self):
		return self.radius*self.radius*3.14



aCircle = Circle(12)

print(aCircle.area())


# Question 48
# Question
# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

# Hints
# Use def methodName(self) to define a method.


class Rectangle(object):
	"""docstring for Rectangle"""
	def __init__(self, length, width):
		
		self.length = length
		self.width = width
		
	def area (self):
		return self.length*self.width

aRectangle= Rectangle(10,2)
print(aRectangle.area())


# Question 49
# Question
# Define a class named Shape and its subclass Square.
#  The Square class has an init function which takes a length as argument.
#   Both classes have a area function which can print the area of the shape
#    where Shape's area is 0 by default.

# Hints
# To override a method in super class, we can define a method with the same name in the super class.


class Shape(object):
	"""docstring for Shape"""
	def __init__(self):
		pass

	def area (self):
		return 0


class Square(Shape):
			"""docstring for Square"""
			def __init__(self, length):
				# super(self).__init__()
				self.length = length

			def area(self):
				return self.length**2

aSquare= Square(10)


print(aSquare.area())


# Question
# Please raise a RuntimeError exception.

# Hints
# UUse raise() to raise an exception.

raise RuntimeError('some error message')
	
