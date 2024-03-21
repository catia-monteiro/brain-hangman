# Brain Hangman

Welcome to Brain Hangman, an educational command-line game where you'll decipher the names of various brain areas.
Each correct guess reveals a definition, enhancing your knowledge of neuroscience as you play.

## How to Play

1. Run the game script (`main.py`) in your Python environment.
2. Your goal is to identify the name of a brain area, which may comprise one or more words. You'll be presented with
a series of dashes, where each dash represents a letter to be guessed. You will also see a graphical representation of
a hangman, showing your remaining lives following each guess.
3. Guess letters one at a time. If the letter is part of the word(s), its position in the word(s) will be revealed.
If not, you'll lose a life.
4. Keep guessing until you've either uncovered all the letters in name of the brain area or run out of lives.
5. You win if you manage to guess the brain area correctly before running out of lives. As a reward, you'll see a
definition of the brain area you just revealed. Win or lose, you can play again, as many times as you want, and keep
improving your knowledge of the brain.


## Features

- Randomly selects brain area names from a predefined list to be guessed by the player.
- Supports brain area names comprised of one or more words.
- Uses ASCII art to visually represent the number of remaining lives during the game.
- Includes definitions of each brain area to educate players about the functions and significance of different parts
of the brain.

## Requirements

- Python 3.x

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Ensure you have Python installed on your machine.
4. Run the following command in your terminal or command prompt:
`cd path/to/brain_hangman`
Replace path/to/brain_hangman with the actual path to the directory where you cloned the repository on your local machine.

## Contributing

If you have any suggestions or improvements for the game, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE.txt).