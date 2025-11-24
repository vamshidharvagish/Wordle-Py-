import pygame
import os

pygame.init()
pygame.font.init()

# File Paths
ASSET_PATH = "assets"
DATA_PATH = "data"
GUESSABLE_WORDS_FILE = os.path.join(DATA_PATH, "guessable_words.txt")
CHOOSABLE_WORDS_FILE = os.path.join(DATA_PATH, "choosable_words.txt")
STATS_FILE = os.path.join(DATA_PATH, "stats.json")

# Dimensions
WIDTH, HEIGHT = 633, 900
LETTER_SIZE = 75
ALPHABET_X_DISTANCE = 85
ALPHABET_Y_DISTANCE = 12

# --- Colours ---
GREY = "#3A3A3C"
YELLOW = "#B59F3B"
GREEN = "#538D4E"
BORDER = "#D3D6DA"
FILLED_BORDER = "#878A8C"
BLACK = "#000000"
WHITE = "#FFFFFF"

# --- Fonts ---
try:
    FONT_PATH = os.path.join(ASSET_PATH, "FreeSansBold.otf")
    GUESSED_LETTER_FONT = pygame.font.Font(FONT_PATH, 50)
    AVAILABLE_LETTER_FONT = pygame.font.Font(FONT_PATH, 25)
    PLAY_AGAIN_FONT = pygame.font.Font(FONT_PATH, 40)
    STATS_FONT = pygame.font.Font(FONT_PATH, 20)
except FileNotFoundError:
    print(f"Error: Font file '{FONT_PATH}' not found.")
    print("Please ensure the font file is in the 'assets' directory.")
    pygame.quit()
    exit()

# --- Keyboard Layout ---
ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
VALID_KEYS = "QWERTYUIOPASDFGHJKLZXCVBNM"
