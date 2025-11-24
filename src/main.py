import pygame
import sys
from constants import *
from game_objects import Letter
import logic
import display

try:
    import ctypes

    ctypes.windll.user32.SetProcessDPIAware()
except AttributeError:
    pass

guess_count = 0
guesses = [[] for _ in range(6)]
current_guess = []
current_guess_str = ""
current_alphabet_bg_x = 110
game_result = ""

clock = pygame.time.Clock()
stats = logic.load_stats()
display.init_screen()
indicators = display.init_indicators()

GUESSABLE_WORDS, SECRET = logic.get_guessable_words()


def add_letter_to_guess(key_pressed):
    """Adds new a new letter to the current guess."""
    global current_guess_str, current_alphabet_bg_x

    if len(current_guess_str) < 5:
        current_guess_str += key_pressed
        new_letter = Letter(
            key_pressed,
            (current_alphabet_bg_x, guess_count * 100 + ALPHABET_Y_DISTANCE),
        )
        current_alphabet_bg_x += ALPHABET_X_DISTANCE
        guesses[guess_count].append(new_letter)
        current_guess.append(new_letter)
        new_letter.draw()


def remove_letter_from_guess():
    """Deletes the last letter from the current guess"""
    global current_guess_str, current_alphabet_bg_x

    if len(current_guess_str) > 0:
        letter = current_guess.pop()
        guesses[guess_count].pop()
        current_guess_str = current_guess_str[:-1]
        current_alphabet_bg_x -= ALPHABET_X_DISTANCE
        letter.delete()


def evaluate_guess():
    """Checks the guess and updates screen if valid"""
    global guess_count, game_result, stats, current_alphabet_bg_x, current_guess_str, current_guess

    if len(current_guess_str) != 5:
        print("Word must be 5 letters long!")  # Debug feedback
        return

    if current_guess_str not in GUESSABLE_WORDS:
        print(f"'{current_guess_str}' is not in the word list!")  # Debug feedback
        return

    tile_colours, key_colours = logic.check_guess(current_guess_str, SECRET)

    display.update_guess_colours(current_guess, tile_colours)
    display.update_keyboard(indicators, key_colours)

    guess_count += 1

    if current_guess_str == SECRET:
        game_result = "W"
    elif guess_count == 6:
        game_result = "L"

    if game_result:
        stats = logic.update_stats(stats, game_result, guess_count)

    current_guess = []
    current_guess_str = ""
    current_alphabet_bg_x = 110


def reset():
    """Resets the game."""
    global guess_count, guesses, current_guess, current_guess_str, current_alphabet_bg_x, game_result, SECRET

    guess_count = 0
    guesses = [[] for _ in range(6)]
    current_guess = []
    current_guess_str = ""
    current_alphabet_bg_x = 110
    game_result = ""

    _, SECRET = logic.get_random_word()
    display.reset_display(indicators)


while True:
    if game_result != "":
        display.draw_play_again(stats, SECRET)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_result != "":
                    reset()
                else:
                    evaluate_guess()

            elif event.key == pygame.K_BACKSPACE:
                if game_result == "":
                    remove_letter_from_guess()

            elif game_result == "":
                key_pressed = event.unicode.upper()
                if key_pressed in VALID_KEYS and key_pressed != "":
                    add_letter_to_guess(key_pressed)

    pygame.display.update()
    clock.tick(60)
