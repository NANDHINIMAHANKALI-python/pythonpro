
import random

def choose_random_word():
    list_of_the_words = ["hangman", "java", "react", "python", "datascience", "webtechnology", "StructureQuerey"]
    return random.choice(list_of_the_words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_'
    return display

def hangman():
    print("Let's play Hangman game!")
    guess_word = choose_random_word()
    guessed_letters = []
    attempts = 6
    
    print(display_word(guess_word, guessed_letters))

    while '_' in display_word(guess_word, guessed_letters) and attempts > 0:
        guess = input("1st you Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only single letters.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in guess_word:
            print("YOUR guss is Good !")
        else:
            attempts -= 1
            print(f"Oops! That letter is not in the word. You have {attempts} attempts left that .")

        print(display_word(guess_word, guessed_letters))

    if '_' not in display_word(guess_word, guessed_letters):
        print(f"Congratulations! you are the winner of this game...You guessed the word: \"{word_to_guess}\".")
    else:
        print(f"Sorry, you're out of attempts. you are not winner of this game .The actual word was: \"{word_to_guess}\".")

if __name__ == "__main__":
    hangman()
