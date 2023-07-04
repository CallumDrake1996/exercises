import random

def main():
  for i in range(6):
      numbers = random.randint(1,50)
      print(numbers)
  a = input('Would you like a bonus ball? (y/n)')
  if a == 'y':
    print('Your bonus ball is')
    print(random.randint(1,50))
  elif a == 'Y':
    print('Your bonus ball is')
    print(random.randint(1,50))

print('Hello and welcome to your personal lotery generator')

name = input('What is your name? ') 

print('Hello ' + name + ', here are your numbers:') 

main()

print('would you like to run the program again? (y/n)')
b = input()
while b == 'y':
   main()
   print('would you like to run the program again? (y/n)')
   b = input()
   if b == 'n':
     break

print('Thank you for using the program')