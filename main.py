import os
import random
from word_list import brain_areas
from graphs import logo, stages


def clear_screen():
    """
        Clear the console screen by sending the appropriate command
        based on the operating system:
            - 'cls' for Windows;
            - 'clear' for macOS and Linux.
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')


def choose_word():
    """Choose a random word from the dictionary of brain areas, where:
        - keys: names of brain areas;
        - values: definitions.
    Use the list function to convert the dictionary keys to a list and then select a random key.
    """
    return random.choice(list(brain_areas.keys()))


def display_word(word, guessed_letters):
    """Display the word with placeholders for unguessed letters and spaces between words."""
    display = ""
    for letter in word:
        if letter.lower() in guessed_letters or letter == " ":
            display += letter
        else:
            display += "_"
    return display


def get_guess(guessed_letters):
    """Ask the user to guess a letter and check:
            - if the user input is valid (i.e. a single letter, not a number, symbol or space);
            - if the letter has been previously entered in this round. """
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess not in guessed_letters:
                return guess
            else:
                print(f"You've already guessed the letter {guess}. Please enter a letter you haven't guessed before.\n")
        else:
            print("Invalid input. Please enter a single letter.\n")
        # if guess.isalpha() and len(guess) == 1 and guess not in guessed_letters:
        #     return guess
        # else:
        #     print(f"You've already entered {guess}. Please enter a single letter that you haven't guessed before.")


def display_definition(term):
    """Display the definition of the guessed brain area."""
    if term in brain_areas:
        print(f"{term.title()} - {brain_areas[term]}\n")
    else:
        print("Definition not found.")


def play_or_quit():
    """Ask the user if they want to play again or quit the game. """
    while True:
        play_again = input("Enter 'p' to play again or 'q' to quit: ").lower()
        if play_again == 'p':
            clear_screen()
            play_game()
            break  # Exit the while loop after restarting the game.
        elif play_again == 'q':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input.\n")


def play_game():
    chosen_word = choose_word()
    lives = 6
    guessed_letters = []

    print(logo)

    # Display explanatory text when game is launched:
    print("Welcome to Brain Hangman!\n")
    print("Can you guess the brain area by entering one letter at a time?")
    print("Keep in mind that some brain areas consist of more than one word.")
    print("You start with 6 lives. Every incorrect guess will cost you one life.")
    print("Try to guess the brain area before you run out of lives!\n")

    while lives > 0:
        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        clear_screen()
        print(stages[lives])
        print(display_word(chosen_word, guessed_letters))

        if guess not in chosen_word:
            print(f"The letter {guess} does not appear in the name of this brain area. You've lost a life.")
            lives -= 1
            print(f"Lives remaining: {lives}\n")
        else:
            print(f"Congratulations! The letter {guess} appears in the name of this brain area.\n")

            if all((letter in guessed_letters or letter == " ") for letter in chosen_word.replace(" ", "")):
                print("Bravo! You guessed it right :)\n")
                display_definition(chosen_word)
                break
    else:
        print("Game over :(\n")

    play_or_quit()


if __name__ == "__main__":
    play_game()
