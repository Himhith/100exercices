# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

# Suppose the following input is supplied to the program:

# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.


text=input('write one line text to count the characters: ').split(' ')

wordcount=dict()

for word in text:
	if word in wordcount.keys():
		wordcount[word]+=1
	else:
		wordcount[word]=1


# simple print : print(wordcount)

#fancy print

for word in wordcount:
	print(f'{word} {wordcount[word]}')


