# Wordle-Py

## Team Name

code_BASE

## Project Title

Wordle-Py: A Wordle Clone in Python

## Short Description

Wordle-Py is a Python-based clone of the popular Wordle word-guessing game. It offers a graphical interface using Pygame and faithfully replicates the core gameplay mechanics, allowing players to guess a secret five-letter word in six attempts with colour-coded feedback.

## Authors

- Amogh Gurudatta
- Aryan Sujay
- Vamshidhar V

## Concepts and Libraries Used

- Concepts:
  - Game state management
  - Word validation and logic checking
  - GUI rendering and event handling
  - Statistics tracking (wins, losses, streaks)
- Libraries:
  - Python standard libraries (`random`, `json`, `ctypes`, `sys`, `os`)
  - `Pygame` for graphical interface and input handling

## Main Modules and Functions

### src/main.py

- Entry point of the application.
- Manages game loop, user input and drawing/updating the interface.
- Key functions:
  - `add_letter_to_guess(key_pressed)`: Adds a pressed letter to current guess.
  - `remove_letter_from_guess()`: Deletes last letter in current guess.
  - `evaluate_guess()`: Validates and evaluates the current guess; updates display colors and game state.
  - `reset()`: Resets the game state for a new game.

Example gameplay interaction:

- On typing letters, they appear on screen.
- Press ENTER to submit guess; feedback colours show tile correctness.
- Game displays stats and option to play again after win or loss.

### src/logic.py

- Implements game logic and word management.
- Key functions:
  - `get_guessable_words()`: Loads valid guess words from file.
  - `get_random_word()`: Picks random secret word.
  - `check_guess(guess_string, correct_word)`: Returns tile and keyboard feedback colours for guess evaluation.
  - `load_stats()` / `save_stats(stats)`: Manage persistent game statistics.
  - `update_stats(stats, game_result, guess_count)`: Updates stats based on result.

### src/display.py

- Handles all graphical rendering and UI updates using Pygame.
- Key functions:
  - `init_screen()`: Draws initial game board.
  - `init_indicators()`: Initializes keyboard indicator tiles.
  - `update_guess_colours(current_guess, tile_colour)`: Updates tile colours for a guess.
  - `update_keyboard(indicators, key_colours)`: Updates keyboard key colours.
  - `draw_play_again(stats, SECRET)`: Displays endgame screen with stats and option to replay.
  - `reset_display(indicators)`: Resets graphical display for new game.

## Setup Instructions

Have python3.x and pip3.x installed, (and added to `PATH` if on Windows).

1. Clone the repository:

    ```bash
    git clone https://github.com/vamshidharvagish/Wordle-Py-.git
    cd Wordle-Py-
    ```

2. Install required dependencies:

    1. Using a virtual environment(venv) (Recommended):
        - **Windows**

            ```bash
            py -m venv .venv
            .\.venv\Scripts\activate
            ```

            To confirm the virtual environment is activated, check the location of your Python interpreter:

            ```bash
            where python
            ```

            While the virtual environment is active, the above command will output a filepath that includes the .venv directory, by ending with the following:

            ```bash
            .venv\Scripts\python
            ```

            Now, install pygame using pip:

            ```bash
            py -m pip install pygame
            ```

        - **Linux/macOS**

            ```bash
            python3 -m venv .venv
            source .venv/bin/activate
            ```

            To confirm the virtual environment is activated, check the location of your Python interpreter:

            ```bash
            which python
            ```

            While the virtual environment is active, the above command will output a filepath that includes the .venv directory, by ending with the following:

            ```bash
            .venv/bin/python
            ```

            Now, install pygame using pip:

            ```bash
            python3 -m pip install pygame
            ```

    2. Installing systemwide (Not recommended):
        - **Windows**

            ```bash
            py -m pip install pygame
            ```

        - **macOS**

            ```bash
            python3 -m pip install pygame
            ```

        - **Linux (Ubuntu/Debian)**

            ```bash
            sudo apt install python3-pygame
            ```

3. Ensure required word files are present (`choosable_words.txt`, `guessable_words.txt`) in the appropriate location.

4. Run the game:

    - **Windows**

        ```bash
        py src/main.py
        ```

    - **Linux/macOS**

      ```bash
      python3 src/main.py
      ```

Enjoy the game!
