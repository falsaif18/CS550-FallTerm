#Faisal Alsaif
#10/5/17
#On my honor, I have neither given nor received unauthorized aid.
#Faisal Alsaif 

import random #to generate a random number later 
import sys #helps in quitting the system when the player wants 

def userchoice(): #variable that is the program 
	global rank #stores rank for later reference
	global x #stores x for later reference
	global score #stores score for later referenc
	global card1 #stores card1 for later reference
	global card2 #stores card2 for later reference 
	global card3 #stores card3 for later reference

	rank = ''
	x = 0 
	score = 'Your score is:'
	card1 = ''	
	card2 = ''
	card3 = ''
	card4 = ''

	while True: #loop that continues program so long as its true
		card1 = int(random.randrange(2,15)) #genertates card
		card2 = int(random.randrange(2,15)) #''
		card3 = int(random.randrange(2,15)) #''

		print('Here is your hand: ' + str(card1), str(card2), str(card3)) #displays hand
		rank = int(random.randrange(2,14)) #generates the computer's card

		try:  #tries all the functions          
	            choice = input('Which card would you like to play? ') #user chooses which card
	            if choice == 'quit': #to quit game
	                    print('Hope you had fun, have a good day')
	                    sys.exit()
	            else: #to continue game
	                    choice = int(choice)
	                    if choice == card1 or choice == card2 or choice == card3: #
	                            print ('Opponent\'s card: ' + str(rank))
	                    else:
	                            print('Nice try cheater, here\'s a new hand:')
                            
		except ValueError: #if the choice input is not an integer 
			print('That\'s not a number... pick again')
			print(score)
			print(x)
			return

		if choice != card1 and choice != card2 and choice != card3: #does not accept a card not in your hand 
                        print(score)
                        print(x)
		elif choice > rank: #compares to computer
			x = x+2
			print(score) 
			print(x)
		elif choice == rank: #in event of a tie
	            print('Looks like you tied this hand. No points awarded, draw again')
	            print(score)
	            print(x)
		else: #if you loose the hand
			x = x-2
			print(score) 
			print(x)

		if x < 0:
			print('Ouch looks like you\'re negative. Let\'s bring that up!')

		if x == 32: #winning total 
	            print('YOU WIN!')
	            sys.exit()

Confirm = input('Would you play a game of endless fun? (yes/no) ') #asks if they even want to play 
if Confirm == 'yes' or Confirm == 'Yes': #prints the following if they do want to play 
	print('Welcome to war, the rules are easy: ')
	print('1) you are given a hand of 3 cards and play against the computer')
	print('2) you pick a number from your hand; hand will regenerate each turn')
	print('3) if the numbers tie, draw again until the pile is won')
	print('4) Once you reach 32 points you win')
	print('5) you may quit the game at any time by typing "quit"')
	print('6) don\'t type words you\'ll go back to 0')
	print('Have Fun!')
else: #if they dont want to play 
	print('Sorry to bother you, but it\'s a fun game. Carry on')
	sys.exit()

while True: #runs the program
	userchoice()







        









