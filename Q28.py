
# Question 28
# Question:
# Define a function that can receive two integer numbers in string form and compute 
# their sum and then print it in console.

def sum_of_two_number_string (str1,str2):
	return int(str1)+int(str2)

print(sum_of_two_number_string("324","34243"))


def concatenate_two_strings(s1,s2):
	return (f'{s1}{s2}')

con_two= lambda s1,s2: (f'{s1}{s2}')

print(concatenate_two_strings('ala',"ola"))
print(con_two('tak','zupa'))


# Question:
# Define a function that can accept two strings as input and print the string with maximum length in console. 
# If two strings have the same length, then the function should print all strings line by line.

# longer_string= lambda s1,s2: s1 if len(s1)>

def longer_str (s1,s2):
	if len(s1)>len(s2):
		return s1
	elif len(s1)<len(s2):
		return s2
	else:
		return s1,s2

print (longer_str('aaa','bbb'))

