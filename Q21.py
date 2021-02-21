# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:


#import mathlib
import math

directions_vertcal=[]
directions_horizontal=[]
directions=[]

while True:
	direction=input()
	#print(type(direction))
	if direction:

		directions.append(direction)
	else:
		break
#print(type(directions[1]))
direc=directions
vertical=0
horizontal=0


#print(enumerate(direc))
#type(direc)
for i in range(len(direc)):
	#print(type(direc[i]))

	#print(directions[i])
	a =direc[i].split(' ')
	if a[0]=="UP":
		vertical+=int(a[1])
	elif a[0]=="DOWN":
		vertical-=int(a[1])
	elif a[0]=="LEFT":
		horizontal-=int(a[1])
	elif a[0]=="RIGHT":
		horizontal+=int(a[1])

print(int(math.sqrt(horizontal**2+vertical**2)))


def dircetions_measure(direc):
	vertical=0
	horizontal=0
	type(direc)
	for i in enumerate(direc):
		print(type(direc[i]))

		#print(directions[i])
		a =direc[i].split(' ')
		if a[0]=="UP":
			vertical+=a[1]
		elif a[0]=="DOWN":
			vertical-=a[1]
		elif a[0]=="LEFT":
			horizontal-=a[1]
		elif a[0]=="RIGHT":
			horizontal+=a[1]

		# if directions[i][0]=="UP":
		# 	vertical+=directions[i][0]
		# elif directions[i][0]=="DOWN":
		# 	vertical-=directions[i][0]
		# elif directions[i][0]=="LEFT":
		# 	horizontal-=directions[i][0]
		# elif directions[i][0]=="RIGHT":
		# 	horizontal+=directions[i][0]

	return math.sqrt(horizontal**2+vertical**2)

#dircetions_measure(directions)



