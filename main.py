#Rubix cube simulation. User enters moves separated by spaces.
#(D U' F2 means turn the bottom face clockwise, turn the top face counter-clockwise, and turn the front face twice.)

from numpy import *

def Copy(axis = 'z'):
	if axis == 'z':
		for i in range(5):
			rubiy[i] = rubiz[::-1, i, :]
			rubix[i] = rubiz[:, :, 4-i].T
	elif axis == 'y':
		for i in range(5):
			rubiz[i] = rubiy[:, 4-i, :]
			rubix[i] = rubiy[:, ::-1, 4-i]
	else:
		for i in range(5):
			rubiz[i] = rubix[::-1, :, i].T
			rubiy[i] = rubix[::-1, i, ::-1].T

def Rotate(face, dir = 1):
	if face in ('f', 'b'):
		if face == 'f':
			rubiz[0] = rot90(rubiz[0], -dir)
			rubiz[1] = rot90(rubiz[1], -dir)
		else:
			rubiz[3] = rot90(rubiz[3], dir)
			rubiz[4] = rot90(rubiz[4], dir)
		Copy('z')
	
	elif face in ('u', 'd'):
		if face == 'u':
			rubiy[0] = rot90(rubiy[0], -dir)
			rubiy[1] = rot90(rubiy[1], -dir)
		else:
			rubiy[3] = rot90(rubiy[3], dir)
			rubiy[4] = rot90(rubiy[4], dir)
		Copy('y')
	
	elif face in ('r', 'l'):
		if face == 'r':
			rubix[0] = rot90(rubix[0], -dir)
			rubix[1] = rot90(rubix[1], -dir)
		else:
			rubix[3] = rot90(rubix[3], dir)
			rubix[4] = rot90(rubix[4], dir)
		Copy('x')
	
	else:
		print "Unrecognised command"
		exit(1)

def PrintCube():
	s = array([' '] * 9).reshape(3, 3)
	n = array(['\n', '\n', '']).reshape(3, 1)
	print
	print ''.join(hstack((s, rubiy[0, 1:4, 1:4], n)).flatten())
	print ''.join(hstack((rubix[4, 1:4, 3:0:-1], rubiz[0, 1:4, 1:4], rubix[0, 1:4, 1:4], rubiz[4, 1:4, 3:0:-1], n)).flatten())
	print ''.join(hstack((s, rubiy[4, 1:4, 3:0:-1], n)).flatten())

#3 different copies of the same cube are used, they each have their front face pointing in the z, y, x axes, respectively.
#This is because it is easiest to rotate a face when it is normal to the axis.
#A 5x5x5 array is used instead of a 3x3x3 array because a side or corner piece has more than 1 color associated with it.
#It could be thought of as a 3x3x3 cube with a "shell" around it representing the colour.
rubiz = array([''] * 125).reshape(5, 5, 5)
rubiy = rubiz.copy()
rubix = rubiz.copy()

rubiz[1:4,0,1:4] = 'y'
rubiz[1:4,1:4,0] = 'b'
rubiz[0,1:4,1:4] = 'r'
rubiz[1:4,1:4,4] = 'g'
rubiz[4,1:4,1:4] = 'o'
rubiz[1:4,4,1:4] = 'w'

Copy('z')
	
userInput = raw_input('\nInput: ').lower().split()

for i in userInput:
	if(len(i) == 1):
		Rotate(i)
	elif(i[1] == "'"):
		Rotate(i[0], -1)
	else:
		Rotate(i[0], 2)

PrintCube()
