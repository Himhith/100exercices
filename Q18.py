# A website requires the users to input username and password to register.
 # Write a program to check the validity of password input by users.

# Following are the criteria for checking the password:

# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords
# and will check them according to the above criteria. Passwords that
# match the criteria are to be printed, each separated by a comma.

# Example

# If the following passwords are given as input to the program:

# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:

# ABd1234@1
# Hints:
# In case of input data being supplied to the question, 
# it should be assumed to be a console input.

import re

inp=['ABd1234@1','a F1#','2w3E*','2We3345']

def check(password):
	p=re.compile('\w')
	if not p.search(password):
		#print('not w')
		return False
	p=re.compile('\d')
	if not p.search(password):
		#print('not d')
		return False
	p=re.compile('[#$?@]')
	if not p.search(password):
		#print('not $')
		return False
	return True

	# for char in password:
		# if char 

#print(check('asfa111$$$sfsvasfa'))

for password in inp:
	#print(len(password))
	if check(password) and len(password)>6 and len(password)<12:
		print(password,',')


#reg ex pattaren : ^\b(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}\b$ 

