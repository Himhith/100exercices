# Write a program which accepts a sequence of comma separated 4 digit binary
# numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#
# Example:
#
# 0100,0011,1010,1001
# Then the output should be:
#
# 1010
# Notes: Assume the data is input by console.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


numbers=list(input().split(','))
new_li2=[int(item,2) for item in numbers]
print(new_li2)
print(numbers)
new_li=[]
#new_li=[new_li.append(i) for i in numbers if i % 5 != 0]
[new_li.append(numbers[i]) for i in range(len(numbers)) if new_li2[i] % 5 == 0]
# for index in range(len(numbers)):
#     if new_li2[index] % 5 == 0:
#         new_li.append(numbers[index])


print (new_li)
#
# def check(x):                   # check function returns true if divisible by 5
#     return int(x,2)%5 == 0      # int(x,b) takes x as string and b as base from which
#                                 # it will be converted to decimal
# data = input().split(',')
#
# data = list(filter(check,data)) # in filter(func,object) function, elements are picked from 'data' if found True by 'check' function
# print(",".join(data))