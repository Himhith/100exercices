#Q38 With a given tuple (1,2,3,4,5,6,7,8,9,10), 
# write a program to print the first half values
#  in one line and the last half values in one line.

tup= 1,2,3,4,5,6,7,8,9,10

print(f'{tup[:5]}\n{tup[5:]}')

#Q39 Write a program to generate and print another 
# tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

# Hints:
# Use "for" to iterate the tuple. Use tuple() to generate a tuple from a list.

print([x for x in tup if x%2==0])
