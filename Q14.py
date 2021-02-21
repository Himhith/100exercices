# Write a program that accepts a sentence and calculate the number
# of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:

# Hello world!
# Then, the output should be:

# UPPER CASE 1
# LOWER CASE 9

inp= input()

#inp = 'Hello world!'

n = 0
m= 0 

for index in range(len(inp)):
	if inp[index].islower():
		n+=1
	elif inp[index].isupper():
		m+=1


print(f"UPPER CASE= {n} \n LOWER CASE= {m}")