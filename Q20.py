# Question:
# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

# Suppose the following input is supplied to the program:

# 7
# Then, the output should be:

# 0
# 7
# 14
# Hints:
# Consider use class, function and comprehension.



class NumGen(object):
	"""docstring for NumGen"""
	def __init__(self, num):
		super(NumGen, self).__init__()
		self.num = num
		self.gener= self.generate()

	def generate(self):
		for i in range(self.num+5):
			#print(i)
			if i%7==0:
				yield i 

	def generate_out(self):
		return(next(self.gener))

gen_seven=NumGen(7)

#print(gen_seven.generate())
print (gen_seven.generate_out())

print (gen_seven.generate_out())

#print (gen_seven.generate_out())
# print(next(gen_seven.generate()))
# print(next(gen_seven.generate()))
# print(next(gen_seven.generate()))

'''Solution by: Seawolf159
# '''
# class Divisible:

#     def by_seven(self, n):
#         for number in range(1,n + 1):
#             if number % 7 == 0: yield number


# divisible = Divisible()
# generator = divisible.by_seven(int(input("Please insert a number. --> ")))
# for number in generator:
#     print(number)