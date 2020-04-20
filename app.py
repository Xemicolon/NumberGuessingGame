from random import randint
from guess import guessTheNumber


while True:
    print(f'Welcome to the Number guessing game 😎\n')
    user_input = str(input(
        'There are 3 levels: easy, medium, hard. \nType "easy", "medium" or "hard" to select difficulty level \nor \ntype "quit" to end the game. \n>_  '))
    if user_input == 'easy':
        guessTheNumber('easy', 10, 6)
    elif user_input == 'medium':
        guessTheNumber('medium', 20, 4)
    elif user_input == 'hard':
        guessTheNumber('hard', 50, 3)
    elif user_input == 'quit':
        print(f'See you next time ✌')
        break
    else:
        print(f'😕 I don\'t understand that')
