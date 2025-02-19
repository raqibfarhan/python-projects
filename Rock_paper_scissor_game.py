import random


emojis = {'r': '🪨', 'p': '📃', 's':'✂️' }
choices = ('r','p','s') 

while True:
    user_choice = input('select rock, paper ,scissor ? (r/p/s): ').lower()
    if user_choice not in  choices:
        print('invalid choice!')
        continue

    computer_choice = random.choice(choices)
  
    print(f'you choose {emojis[user_choice]}')
    print(f'computer choose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie !')
    elif (
    (user_choice == 'r' and computer_choice == 's') or 
    (user_choice == 's' and computer_choice == 'p') or
    (user_choice == 'p' and computer_choice == 'r')):
        print('you win !')
    else:
        print('you loose !')

    user_continue = input('do you want try again (y/n)? ').lower()
    if user_continue == 'n':
        break


# key :value
# 'r':'🪨'
# 's' : '✂️'
# Ask the user to make a choice
#if the choice is not valid 
# Print an error
# Let the computer make a choice
# Print chouces (Emojis)
# detremie the winner
# Ask theuser if  they want to continue
# if not
# Terminate 