# Question:
# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

# Hints:
# Use if statement to judge condition.


string = input()

acceptedstrings= ['yes','YES','Yes']
if string in acceptedstrings:
	print('string has been accepted.')
else:
	print('NO!') 