import random
from constants import (
    GREY,
    YELLOW,
    GREEN,
    CHOOSABLE_WORDS_FILE,
    GUESSABLE_WORDS_FILE,
    STATS_FILE,
)
import json

guess_count = 0
guesses = [[] for _ in range(6)]
current_guess = []
current_guess_string = ""

game_result = ""


def get_random_word():
    try:
        with open(CHOOSABLE_WORDS_FILE, "r") as f:
            # Read all text and split into words by whitespace
            words = [word.strip().upper() for word in f.read().split()]
        if not words:
            raise ValueError("Words file is empty.")
        # Return a random word from the list
        return set(words), random.choice(words)
    except FileNotFoundError:
        print(f"Error: '{CHOOSABLE_WORDS_FILE}' not found. Please create it.")
        exit()
    except Exception as e:
        print(f"Error loading words: {e}")
        exit()


def get_guessable_words():
    try:
        with open(GUESSABLE_WORDS_FILE, "r") as f:
            # Read all text and split into words by whitespace
            words = [word.strip().upper() for word in f.read().split()]
        if not words:
            raise ValueError("Words file is empty.")
        # Return a random word from the list
        return set(words), random.choice(words)
    except FileNotFoundError:
        print(f"Error: '{GUESSABLE_WORDS_FILE}' not found. Please create it.")
        exit()
    except Exception as e:
        print(f"Error loading words: {e}")
        exit()


def load_stats():
    """Loads game statistics from the JSON file."""
    default_stats = {
        "wins": 0,
        "losses": 0,
        "current_streak": 0,
        "max_streak": 0,
        "guess_distribution": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0},
    }
    try:
        with open(STATS_FILE, "r") as f:
            stats = json.load(f)
            stats.update({k: v for k, v in default_stats.items() if k not in stats})
            return stats
    except (FileNotFoundError, json.JSONDecodeError):
        return default_stats


def save_stats(stats):
    """Saves the game statistics to the JSON file."""
    try:
        with open(STATS_FILE, "w") as f:
            json.dump(stats, f, indent=4)
    except IOError as e:
        print(f"Error saving stats: {e}")


def update_stats(stats, game_result, guess_count):
    """Updates the stats dictionary based on the game result."""
    if game_result == "W":
        stats["wins"] += 1
        stats["current_streak"] += 1
        if stats["current_streak"] > stats["max_streak"]:
            stats["max_streak"] = stats["current_streak"]
        stats["guess_distribution"][str(guess_count)] += 1
    elif game_result == "L":
        stats["losses"] += 1
        stats["current_streak"] = 0

    save_stats(stats)
    return stats  # Return the updated stats


def check_guess(guess_string, correct_word):
    """
    Checks a guess against the correct word.
    Returns:
        - A list of colours for the guess tiles (e.g., [GREEN, YELLOW, GREY]).
        - A dictionary of colours for the keyboard (e.g., {'A': GREEN}).
    """
    tile_colours = [GREY] * 5
    key_colours = {}

    correct_word_list = list(correct_word)
    guess_list = list(guess_string)

    for i in range(5):
        letter = guess_list[i]

        if letter == correct_word_list[i]:
            tile_colours[i] = GREEN
            key_colours[letter] = GREEN
            correct_word_list[i] = None

    for i in range(5):
        letter = guess_list[i]

        if tile_colours[i] == GREEN:
            continue

        if letter in correct_word_list:
            tile_colours[i] = YELLOW
            if key_colours.get(letter) != GREEN:  # Don't downgrade Green
                key_colours[letter] = YELLOW
            correct_word_list[correct_word_list.index(letter)] = None
        else:
            if key_colours.get(letter) not in (GREEN, YELLOW):  # Don't downgrade
                key_colours[letter] = GREY

    return tile_colours, key_colours
