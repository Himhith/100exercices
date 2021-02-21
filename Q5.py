# Write a program that calculates and prints the value according to the given formula:
#
# Q = Square root of [(2 * C * D)/H]
#
# Following are the fixed values of C and H:
#
# C is 50. H is 30.
#
# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:
#
# 100,150,180
# The output of the program should be:
#
# 18,22,24
# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value (for example,
# if the output received is 26.0, it should be printed as 26).In case of input data being supplied to the question,
# it should be assumed to be a console input.

#set up C and H
from cmath import sqrt

c= 50
h= 301

#read D  round up
f='10'
f=int(f)
#input_values=input('enter numbers \n')
input_values=('10,20,30')
d=input_values.split(',')
#d=int(d)
d=list(map(int,d))
print(d)
#calculate  Q = Square root of [(2 * C * D)/H]

#q= sqrt(((2*c*d)/h))
q=list(map(lambda x:sqrt((2*c*x)/h),d))

#return output
print(q)