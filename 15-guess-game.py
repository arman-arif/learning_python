# Guess Game

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('\n Guess: '))
    guess_count += 1
    print(" Nope, it's not.")
    if guess == secret_number:
        print("\n You guessed it!\n You Won!")
        break
else:
    print("\n Sorry, you failed!")
