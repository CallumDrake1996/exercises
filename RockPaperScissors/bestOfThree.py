import random

player_point = 0
comp_point = 0


def paper():
    choice = 1
    opponent = random.randint(1, 3)
    if opponent == choice:
        print("Computer chose Paper")
        print('')
        print('Draw!!!')
    elif opponent == 2:
        print('Computer chose Rock')
        print('')
        print('Round WON!!!')
        global player_point 
        player_point += 1
    else:
        print('Computer chose Scissors')
        print('')
        print('You LOST!!!')
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


def RPS():
    print("Welcome to the game of Rock, Paper, Scissors!")
    print('')
    print("This game is best of three.")
    print('')
    print('Choose your weapon!')
    print('')

    while player_point < 3 and comp_point < 3:
        player_pick = input("Rock, Paper, or Scissors? ")
        if player_pick == "ROCK" or player_pick == "rock":
            rock()
            print('player score: ' + str(player_point))
            print('computer score: ' + str(comp_point))
            print('')
            continue
        elif player_pick == "PAPER" or player_pick == "paper":
            paper()
            print('player score: ' + str(player_point))
            print('computer score: ' + str(comp_point))
            print('')   
            continue
        elif player_pick == "scissors" or player_pick == "SCISSORS":
            scissors()
            print('player score: ' + str(player_point))
            print('computer score: ' + str(comp_point))
            print('')
            continue 
        else:
            print('PLEASE FOLLOW RULES AND TRY AGAIN')
            continue
    
RPS()
