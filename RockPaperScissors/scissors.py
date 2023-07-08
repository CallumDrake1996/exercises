import random
def scissors():
    choice = 3
    opponent = random.randint(1,3)
    if opponent == 1:
        print("Computer chose Paper")
        print('')
        print('Round WON!!!')
        player_point =+ 1
        return
    elif opponent == 2:
        print('Computer chose Rock')
        print('')
        print('You LOST!!!')
        computer_point =+ 1
        return
    else:
        print('Computer chose Scissors')
        print('')
        print('DRAW!!!')
        return

        