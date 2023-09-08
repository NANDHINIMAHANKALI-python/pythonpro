import time

def delay_print(text, delay=1):
    for character in text:
        print(character, end='', flush=True)
        time.sleep(delay)
    print()

def start_game():
    delay_print("Welcome to the Text-Based Adventure Game!")
    delay_print("You find yourself in a dark forest.")
    
    while True:
        delay_print("Choose your path:")
        delay_print("1 - Go left")
        delay_print("2 - Go right")
        delay_print("3 - Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            delay_print("You venture deeper into the forest.")
            delay_print("You discover a hidden treasure!")
            delay_print("Congratulations! You win!")
            break
        elif choice == "2":
            delay_print("You head towards the right side of the forest.")
            delay_print("You encounter a wild bear!")
            delay_print("You try to run, but the bear catches you.")
            delay_print("Game over! You were mauled by the bear.")
            break
        elif choice == "3":
            delay_print("Thanks for playing! Goodbye.")
            break
        else:
            delay_print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    start_game()
