from guess import guessTheNumber


while True:
    print(f'Welcome to the Number guessing game 😎\n')
    user_input = str(input(
        'There are 3 levels: easy, medium, hard. \nType "easy", "medium" or "hard" to select difficulty level \nor \n"quit" to end the game. \n>_ ')).lower()
    if user_input == 'easy':
        guessTheNumber(user_input, 10, 6)
    elif user_input == 'medium':
        guessTheNumber(user_input, 20, 4)
    elif user_input == 'hard':
        guessTheNumber(user_input, 50, 3)
    elif user_input == 'quit':
        print(f'See you next time ✌')
        break
    else:
        print(f'😕 I don\'t understand that')
