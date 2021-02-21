# Write a program that accepts a sequence of whitespace separated words as
# input and prints the words after removing all duplicate words and sorting them alphanumerically.
#
# Suppose the following input is supplied to the program:
#
# hello world and practice makes perfect and hello world again
# Then, the output should be:
#
# again and hello makes perfect practice world
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.

#
words = set()
print(type(words))
#input_List=input().split()
words=input().split()
#for word in input_List:
#    words.add(word)

words=sorted(words)
output=''
for word in words:
    output=output+word+' '
    #print(f'{word} ')
print(output)


