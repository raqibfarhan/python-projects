import random

Correct_num = random.randint(1,100)

while True:
    try:
        guess = int(input('guess the number between 1 and 100: '))
        if guess < Correct_num:
            print('too low')
        elif guess > Correct_num:
            print('too high')
        else:
            print('Conragulations! you Found the number')
            break
    except ValueError:
        print('please enter a vlaid number')







# Generate a random number
# loop
#   ask the user to guess the number 
# If not a valid number 
# print error
# if rnumber < guess
# print too low
# if number > guess
# print too high 
# else 
# print weeel done you guessed right 