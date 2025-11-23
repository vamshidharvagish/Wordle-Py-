import pygame
import random
from constants import GREY, YELLOW, GREEN, WORDS_FILE, STATS_FILE
import json

guess_count = 0
guesses = [[] for _ in range(6)]
current_guess = []
current_guess_string = ""

game_result = ""

def get_word():
    try:
        with open(WORDS_FILE, "r") as f:
            # Read all text and split into words by whitespace
            words = f.read().split()
        if not words:
            raise ValueError("Words file is empty.")
        # Return a random word from the list
        return set(words), random.choice(words)
    except FileNotFoundError:
        print(f"Error: '{WORDS_FILE}' not found. Please create it.")
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
        "guess_distribution": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}
    }
    try:
        with open(STATS_FILE, 'r') as f:
            stats = json.load(f)
            stats.update({k: v for k, v in default_stats.items() if k not in stats})
            return stats
    except (FileNotFoundError, json.JSONDecodeError):
        return default_stats

def save_stats(stats):
    """Saves the game statistics to the JSON file."""
    try:
        with open(STATS_FILE, 'w') as f:
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
    return stats # Return the updated stats


def check_guess(guess_to_check, SECRET):

    global current_guess, current_guess_string, guess_count, game_result

    game_decided = False
    for i in range(5):
        lower_letter = guess_to_check[i].text.lower()
        if lower_letter in SECRET:
            if lower_letter == SECRET[i]:
                guess_to_check[i].bg_colour = GREEN
                # for indicator in keyboard_indicators:
                #     if indicator.text == lower_letter.upper():
                #         indicator.bg_colour = GREEN
                #         indicator.draw()
                guess_to_check[i].txt_colour = "#FFFFFF"
                if not game_decided:
                    game_result = "W"

            else:
                guess_to_check[i].bg_colour = YELLOW
                # for indicator in keyboard_indicators:
                #     if indicator.text == lower_letter.upper():
                #         indicator.bg_colour = YELLOW
                #         indicator.draw()
                guess_to_check[i].txt_colour = "#FFFFFF"
                game_result = ""
                game_decided = True

        else:
            guess_to_check[i].bg_colour = GREY
            # for indicator in keyboard_indicators:
            #     if indicator.text == lower_letter.upper():
            #         indicator.bg_colour = GREY
            #         indicator.draw()
            guess_to_check[i].txt_colour = "#FFFFFF"
            game_result = ""
            game_decided = True

        guess_to_check[i].draw()
        pygame.display.update()

    guess_count += 1
    current_guess = []
    current_guess_string = ""
    current_alphabet_bg_x = 110

    if guess_count == 6 and game_result == "":
        game_result = "L"

    # word = entry.upper()
    # ogList = list(secret)
    # newList = list(word)

    # common = []
    # correct = []

    # if ogList == newList:  # If the user inputs the correct answer, the program ends
    #     for i in range(5):
    #         print("\033[1;32m"+newList[i]+"\033[0;0m", end=" ")
    #     print()
    #     print("Congrats! That was the right word.")
    #     exit()

    # for i in range(5):
    #     # If the letters are in the right place, they are considered correct
    #     if newList[i] == secret[i]:
    #         correct.append(newList[i])

    #     # If the letters are not in the right place, but in the answer, they are common
    #     elif newList[i] in ogList:
    #         common.append(newList[i])

    # for i in range(5):
    #     if newList[i] in correct:
    #         print("\033[1;32m"+newList[i]+"\033[0;0m",
    #               end=" ")  # Prints in green
    #         correct.remove(newList[i])  # Remove once printed

    #     elif newList[i] in common:
    #         print("\033[1;33m"+newList[i]+"\033[0;0m",
    #               end=" ")  # Prints in yellow
    #         common.remove(newList[i])  # Remove once printed

    #     else:
    #         print(newList[i], end=" ")  # Prints in no colour

    print()


def isValid(word):
    """
    This function checks whether the user input is a valid english word.
    The text file "valid_wordle_words.txt" must be present in the same directory as the script.
    """
    with open("valid_wordle_words.txt") as f:  # Creates a set of all valid words
        word_list = set(word.strip().lower() for word in f)

    word = word.lower()  # All words are in lowercase
    if len(word) == 5 and (
        word in word_list
    ):  # Ignore words that do not have exactly 5 letters and check if word is valid in the english language
        return True
    else:
        return False


# def main():
#     print("Enter a 5 letter word: ")
    i = 0
    # while (i < 6):
    #     word = input()
    #     if len(word) != 5:
    #         print("Only 5-letter words are allowed.")
    #         continue
    #     if not isValid(word):  #
    #         print("Not in word list.")
    #         continue
    #     wordle(word)
    #     i += 1
    # else:
    #     print("The word was "+secret)


# if __name__ == "__main__":
#     main()

