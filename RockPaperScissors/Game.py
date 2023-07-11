import random 
# importing random module to generate random numbers


# global variables
player_point = 0
comp_point = 0

# each function will be used to determine the outcome of the game one for rock, paper and scissors
def paper():
    choice = 1
    # random number generator 1-3 then assigned each number to a choice
    opponent = random.randint(1, 3)
    if opponent == choice:
        print("Computer chose Paper")
        print('')
        print('Draw!!!')
    elif opponent == 2:
        print('Computer chose Rock')
        print('')
        print('Round WON!!!')
        # global variables are used to keep track of the score win adding a point
        global player_point
        player_point += 1
    else:
        print('Computer chose Scissors')
        print('')
        print('You LOST!!!')
        # global variables are used to keep track of the score loss adding a point
        global comp_point 
        comp_point += 1


def rock():
    choice = 2
    opponent = random.randint(1, 3)
    if opponent == 1:
        print("Computer chose Paper")
        print('')
        print('You LOST!!!')
        global comp_point
        comp_point += 1
    elif opponent == choice:
        print('Computer chose Rock')
        print('')
        print('Draw')
    else:
        print('Computer chose Scissors')
        print('')
        print('Round WON!!!')
        global player_point 
        player_point += 1


def scissors():
    choice = 3
    opponent = random.randint(1, 3)
    if opponent == 1:
        print("Computer chose Paper")
        print('')
        print('Round WON!!!')
        global player_point 
        player_point += 1
    elif opponent == 2:
        print('Computer chose Rock')
        print('')
        print('You LOST!!!')
        global comp_point
        comp_point += 1
    elif opponent == choice:
        print('Computer chose Scissors')
        print('')
        print('DRAW!!!')

# this is the function for the start of the game
def RPS():
    global player_point
    player_point = 0
    global comp_point
    comp_point = 0
    print("Welcome to the game of Rock, Paper, Scissors!")
    print('')
    print("this game is first to 3 points wins the game")
    print('')
    print('Choose your weapon!')
    print('')

# while loop is used to keep track of the score and keep the game going until the score is 3 for either the player or the computer and then prints the score after every round.
    while player_point < 3 and comp_point < 3:
        player_pick = input("Rock, Paper, or Scissors? ")
        player_pick = player_pick.lower()
        if player_pick == "rock":
            rock()
            print('player score: ' + str(player_point))
            print('computer score: ' + str(comp_point))
            print('')
            continue
        elif  player_pick == "paper":
            paper()
            print('player score: ' + str(player_point))
            print('computer score: ' + str(comp_point))
            print('')   
            continue
        elif player_pick == "scissors":
            scissors()
            print('player score: ' + str(player_point))
            print('computer score: ' + str(comp_point))
            print('')
            continue 
        else:
            print('PLEASE FOLLOW RULES AND TRY AGAIN')
            print('')
            continue
    
# calling the function for the game to start and then asking if the user would like to play again. 
RPS()

replay = input('Would you like to play again? Y/N? ')

while replay == 'Y' or replay == 'y':
    RPS()
    replay = input('Would you like to play again? Y/N? ')

print('')
print('Thanks for playing!')
