# Define a function which can generate\
#  a dictionary where the keys are numbers
#   between 1 and 20 (both included) and the 
#   values are square of keys. The function should just print the keys only.

# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.Use range() for loops.
# Use keys() to iterate keys in the dictionary. 
# Also we can use item() to get key/value pairs.

def func():
	dict={}
	for key in range(1,21):
		dict[key]=key**2
	#print(type(dict))
	print (dict.keys())

func()