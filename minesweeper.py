import sys
import random
import AnimationTest

def printNice(twodee):
	for row in range(1, len(twodee)-1):
		for col in range(1, len(twodee[0])-1):
			print(twodee[row][col], end=' ')
		print('')#Don't want to print board
level = input("Would you like to play on Easy, Medium or Hard?")
if level == 'easy' or level == 'Easy':
	width = int(5)+2
	height = int(5)+2
	mines = int(5)
if level == 'medium' or level == 'Medium':
	width = int(12)+2
	height = int(12)+2
	mines = int(15)
if level == 'hard' or level == 'Hard':
	width = int(30)+2
	height = int(15)+2
	mines = int(50)
	#return width, height, mines
def AnswerBoard():
	AnswerBoard.board = [] #adding blank spaces
	for i in range(height):
		row = ['.']*width
		AnswerBoard.board.append(row)
	# add mines to the AnswerBoard.board
	for i in range(mines):
		x = random.randint(1,height-2)
		y = random.randint(1,width-2)
		while AnswerBoard.board[x][y] == '*':
			x = random.randint(1,height-2)
			y = random.randint(1,width-2)
		AnswerBoard.board[x][y] = '*'
	for r in range(1, len(AnswerBoard.board)-1):  #adding neighbor numbers
		for c in range(1, len(AnswerBoard.board[0])-1):
			if AnswerBoard.board[r][c] != '*':
				neighbors = 0
				if AnswerBoard.board[r][c-1] == '*':
					neighbors += 1
				if AnswerBoard.board[r][c+1] == '*':
					neighbors += 1
				if AnswerBoard.board[r-1][c] == '*':
					neighbors += 1
				if AnswerBoard.board[r+1][c] == '*':
					neighbors += 1
				if AnswerBoard.board[r-1][c-1] == '*':
					neighbors += 1
				if AnswerBoard.board[r+1][c-1] == '*':
					neighbors += 1
				if AnswerBoard.board[r-1][c+1] == '*':
					neighbors += 1
				if AnswerBoard.board[r+1][c+1] == '*':
					neighbors += 1
				if neighbors > 0:
					AnswerBoard.board[r][c] = neighbors
	return AnswerBoard.board
def NewGame():
	level = input("Would you like to play on Easy, Medium or Hard?")
	if level == 'easy' or level == 'Easy':
		width = int(5)+2
		height = int(5)+2
		mines = int(5)
	if level == 'medium' or level == 'Medium':
		width = int(12)+2
		height = int(12)+2
		mines = int(15)
	if level == 'hard' or level == 'Hard':
		width = int(30)+2
		height = int(15)+2
		mines = int(50)
def Neighbor():
	for r in range(1, len(AnswerBoard.board)-1):  #checking neighbor numbers
		for c in range(1, len(AnswerBoard.board[0])-1):
			if AnswerBoard.board[r][c] != '.':
				neighbors = 0
				if AnswerBoard.board[r][c-1] == '.':
					neighbors += 1
				if AnswerBoard.board[r][c+1] == '.':
					neighbors += 1
				if AnswerBoard.board[r-1][c] == '.':
					neighbors += 1
				if AnswerBoard.board[r+1][c] == '.':
					neighbors += 1
				if AnswerBoard.board[r-1][c-1] == '.':
					neighbors += 1
				if AnswerBoard.board[r+1][c-1] == '.':
					neighbors += 1
				if AnswerBoard.board[r-1][c+1] == '.':
					neighbors += 1
				if AnswerBoard.board[r+1][c+1] == '.':
					neighbors += 1
				if neighbors > 0:
					AnswerBoard.board[r][c] = neighbors
	return AnswerBoard.board

def BlankBoard():
	empty = []
	empty[0:(width*height)] = ["[]"]
	
	#need to take r,c value and append to empty

def Guess():
	bom = True
	while bom == True:
		board = AnswerBoard.board
		x = int(input('To Guess, specify row'))
		y = int(input('To Guess, specify column'))
		turn = board[x][y]
		if board[x][y] == '*':
			AnimationTest.explode()
			AnimationTest.cls()
			print('You hit a bomb.')
			newgame = input('Play again?')
			if newgame == 'Yes' or newgame == 'yes':
				NewGame()
				bom = False
			else:
				sys.exit()
		else:
			Neighbor()
			#need to add to new blank board
			print(board[r][c])
#def check(): #compare guess to calculate

# print the completed board using my helper function		


while True:
	Guess()
	printNice(AnswerBoard())

#calculate()
#guess()
#check()














