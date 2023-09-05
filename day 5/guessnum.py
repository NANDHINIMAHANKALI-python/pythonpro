import random

def number_guesser(attempts_left=10):
    if attempts_left == 10:
        print("Welcome to the Number Guesser Game!")
        print("I've selected a number between 1 and 100.")
    
    if attempts_left == 0:
        print("Out of attempts! The number was", target_number)
        return
    
    try:
        guess = int(input(f"You have {attempts_left} attempts left. Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        number_guesser(attempts_left)
        return

    if guess < target_number:
        print("Too low!")
    elif guess > target_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {10 - attempts_left + 1} attempts.")
        return
    
    number_guesser(attempts_left - 1)

target_number = random.randint(1, 100)
number_guesser()
