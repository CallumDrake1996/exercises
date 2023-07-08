import random

def RBS():
    player_pick = input("Rock, Paper, or Scissors? ")
    if player_pick == "rock" or player_pick == 'Rock':
        player_pick = 1
    elif player_pick == "paper" or player_pick == 'Paper':
        player_pick = 2
    elif player_pick == "scissors" or player_pick == 'Scissors':
        player_pick = 3
    comp = random.randint(1, 3)

    if comp == 1 and player_pick == 1:
        print('Comp chose Rock')
        print("Draw!!!")
        return 0
    elif comp == 2 and player_pick == 1:
        print('Comp chose Paper')
        print("You lose!!!")
        return 1
    elif comp == 3 and player_pick == 1:
        print('Comp chose Scissors')
        print("You Win!!!")
        return -1
    elif comp == 2 and player_pick == 2:
        print('Comp chose Paper')
        print("Draw!!!")
        return 0
    elif comp == 1 and player_pick == 2:
        print('Comp chose rock')
        print("You Win!!!")
        return -1
    elif comp == 3 and player_pick == 2:
        print('Comp chose Scissors')
        print("You lose!!!")
        return 1
    elif comp == 3 and player_pick == 3:
        print('Comp chose Scissors')
        print("Draw!!!")
        return 0
    elif comp == 2 and player_pick == 3:
        print('Comp chose Paper')
        print("You Win!!!")
        return -1
    elif comp == 1 and player_pick == 3:
        print('Comp chose rock')
        print("You lose!!!")
        return 1

print("Welcome to the game of Rock, Paper, Scissors!")
print('')
print("This game is best of 3!")
print('')
print('Choose your weapon!')
print('')

var = 0
while var <= 3:
    result = RBS()
    var += result

replay = input('Would you like to play again? Y/N? ')

while replay == 'Y' or replay == 'y':
    var = 0
    while var <= 3:
        result = int(RBS())
        var += result
    replay = input('Would you like to play again? Y/N? ')

print('')
print('Thanks for playing')