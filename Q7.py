# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i * j.
#
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
#
# Then, the output of the program should be:
#
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input
# in a comma-separated form.


#ZRÓB TO KRÓTKIMI FORAMI :D j

#D = [int(i) for i in D]

#input for 2 digits: i,j
numbers=input("podaj i,j").split(',')
i=int(numbers[0])
j=int(numbers[1])
# two dimensional tab
tab=[]
# for each in i {for each in j : j*i
for i1 in range(i) :
    tab.append([])
    for j1 in range(j):
        tab[i1].append(i1*j1)
print(tab)
#
# x,y = map(int,input().split(','))
# lst = [[i*j for j in range(y)] for i in range(x)]
# print(lst)

