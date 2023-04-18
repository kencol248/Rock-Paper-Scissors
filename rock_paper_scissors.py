'''10/31/2022
Kenyah Collins
rock_paper_scissor_game
This program will execute a digital version of the game rock, paper, scissors'''

# Here we are doing some setup by importing the random module and setting up the winner variable.
import random

winner = ' '


# Here the computer randomly chooses rock, paper, scissors by bgenerating a random number from 0 to 2 and
# then mapping that to a corresponding string.

random_choice = random.randint(0,2)

# two equal signs mean "equal to"
if random_choice == 0:
    computer_choice = 'rock'
# elif is short for else if
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

# get the users choice with a simple input statement
# user_choice = input('rock, paper, scissors? ')

user_choice = ' '
while (user_choice != 'rock' and
    user_choice != 'paper' and
    user_choice != 'scissors'):

    user_choice = input('rock, paper, scissors? ')

# print('user chose', user_choice)


# Here our game logic which checks to see if the computer wins (or not), and makes the 
# appropriate change to the winner variations

if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'user'

# Here we announce the game was a tie, or the winner along with the computer's choice.

if winner == 'Tie':
    print('We both chose', computer_choice + ',play again.')
else:
    print(winner, 'won. The computer chose', computer_choice + '.')
