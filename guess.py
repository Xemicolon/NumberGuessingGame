def guessTheNumber(difficulty, range, chances):
    computer = randint(1, range)
    level = str(difficulty)
    chances = chances
    print(f'Difficulty level: {level}\nChances: {chances}')
    while True:
        try:
            user_input = int(input(f'Guess the number: '))
            chances -= 1
            print(f'You have {chances} left.')
            if user_input == computer:
                print(f'✅ You got it right!')
                break
            else:
                print(f'❌ That was wrong.')
                if chances == 0:
                    print(f'Game over! You exhausted your chances 😖\n')
                    break
        except ValueError:
            print(f'⚠ Invalid number! Please enter a valid number.')
