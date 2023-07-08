import random

player_point = 0


def paper(player, comp):
    choice = 1
    opponent = random.randint(1, 3)
    if opponent == choice:
        print("Computer chose Paper")
        print('')
        print('Draw!!!')
        return
    elif opponent == 2:
        print('Computer chose Rock')
        print('')
        print('Round WON!!!')
        player += 1
        return
    else:
        print('Computer chose Scissors')
        print('')
        print('You LOST!!!')
        comp += 1
        return


def rock(player, comp):
    choice = 2
    opponent = random.randint(1, 3)
    if opponent == 1:
        print("Computer chose Paper")
        print('')
        print('You LOST!!!')
        comp += 1
        return
    elif opponent == choice:
        print('Computer chose Rock')
        print('')
        print('Draw')
        return
    else:
        print('Computer chose Scissors')
        print('')
        print('Round WON!!!')
        player += 1
        return


def scissors(player, comp):
    choice = 3
    opponent = random.randint(1, 3)
    if opponent == 1:
        print("Computer chose Paper")
        print('')
        print('Round WON!!!')
        player += 1
        return
    elif opponent == 2:
        print('Computer chose Rock')
        print('')
        print('You LOST!!!')
        comp += 1
        return
    else:
        print('Computer chose Scissors')
        print('')
        print('DRAW!!!')
        return


def RPS():
    print("Welcome to the game of Rock, Paper, Scissors!")
    print('')
    print("this game is best of 3!")
    print('')
    print('Choose your weapon!')
    print('')


    player = 0
    comp = 0

    while player <= 3 or comp <= 3:
        player_pick = input("Rock, Paper, or Scissors? ")
        if player_pick == "Rock" or player_pick == "rock":
            rock(player, comp)
            if player == 1:
                player = player + 1
                return
            continue
        elif player_pick == "Paper" or player_pick == "paper":
            player_pick = paper(player, comp)
            continue
        else:
            scissors(player, comp)
            continue


RPS()
replay = input('Would you like to play again? Y/N? ')

while replay == 'Y' or replay == 'y':
    RPS()
    replay = input('Would you like to play again? Y/N')

print('')
print('Thanks for playing!')
