#  Loop
import random

while True:
    choice= input('Do you want role the dice? (y/n):  ').lower()
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1, 6)
        print(f'({die1},{die2})')
    elif choice == 'n':
        print('Thank You for PLaying')
        break
    else:
        print ('invalid choice')


# Generate two numbers
# print them
# if user say n
# print thank message
# terminate
# Else
# print invalid choice