import pygame
from constants import *

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED | pygame.RESIZABLE)

try:
    BACKGROUND = pygame.image.load(os.path.join(ASSET_PATH, "Starting Tiles.png"))
    ICON = pygame.image.load(os.path.join(ASSET_PATH, "Icon.svg"))
    BG_RECT = BACKGROUND.get_rect(center=(317, 300))
except pygame.error as e:
    print(f"Error loading assets: {e}")
    exit()

pygame.display.set_caption("Wordle!")
pygame.display.set_icon(ICON)


def init_screen():
    """Draws empty white board."""
    DISPLAY.fill(WHITE)
    DISPLAY.blit(BACKGROUND, BG_RECT)
    pygame.display.update()


def init_indicators():
    from game_objects import Indicator

    indicators = []
    indicator_x, indicator_y = 20, 600
    for i in range(3):
        for letter in ALPHABET[i]:
            new_indicator = Indicator(indicator_x, indicator_y, letter)
            indicators.append(new_indicator)
            new_indicator.draw()
            indicator_x += 60
        indicator_y += 100
        if i == 0:
            indicator_x = 50
        elif i == 1:
            indicator_x = 105
    return indicators


def update_guess_colours(current_guess, tile_colour):
    """Updates Colour of tiles after guess."""
    for i in range(5):
        current_guess[i].bg_colour = tile_colour[i]
        current_guess[i].txt_colour = WHITE
        current_guess[i].draw()


def update_keyboard(indicators, key_colours):
    for letter, colour in key_colours.items():
        for indicator in indicators:
            if indicator.text == letter:
                # Logic to prevent downgrading colours
                if indicator.bg_colour == GREEN:
                    continue
                if indicator.bg_colour == YELLOW and colour == GREY:
                    continue
                indicator.bg_colour = colour
                indicator.draw()


def draw_play_again(stats, SECRET):
    """Displays the end-game screen with stats and play-again prompt."""

    pygame.draw.rect(DISPLAY, WHITE, (0, 600, WIDTH, 300))

    word_was_text = PLAY_AGAIN_FONT.render(f"The word was {SECRET}!", True, BLACK)
    word_was_rect = word_was_text.get_rect(center=(WIDTH / 2, 630))
    DISPLAY.blit(word_was_text, word_was_rect)

    # --- Display Statistics ---
    wins_text = STATS_FONT.render(f"Wins: {stats['wins']}", True, BLACK)
    losses_text = STATS_FONT.render(f"Losses: {stats['losses']}", True, BLACK)
    curr_streak_text = STATS_FONT.render(
        f"Current Streak: {stats['current_streak']}", True, BLACK
    )
    max_streak_text = STATS_FONT.render(
        f"Max Streak: {stats['max_streak']}", True, BLACK
    )

    DISPLAY.blit(wins_text, (WIDTH / 2 - 250, 670))
    DISPLAY.blit(losses_text, (WIDTH / 2 - 250, 700))
    DISPLAY.blit(curr_streak_text, (WIDTH / 2 + 50, 670))
    DISPLAY.blit(max_streak_text, (WIDTH / 2 + 50, 700))

    dist_title = STATS_FONT.render("Guess Distribution:", True, BLACK)
    dist_rect = dist_title.get_rect(center=(WIDTH / 2, 750))
    DISPLAY.blit(dist_title, dist_rect)

    total_width_estimate = 500
    start_x = (WIDTH - total_width_estimate) / 2
    spacing = 85

    for i in range(1, 7):
        dist_text = STATS_FONT.render(
            f"{i}: {stats['guess_distribution'][str(i)]}", True, GREY
        )
        DISPLAY.blit(dist_text, (start_x + (i - 1) * spacing, 780))

    play_again_text = PLAY_AGAIN_FONT.render("Press ENTER to Play Again!", True, BLACK)
    play_again_rect = play_again_text.get_rect(center=(WIDTH / 2, 840))
    DISPLAY.blit(play_again_text, play_again_rect)

    pygame.display.update()


def reset_display(indicators):
    init_screen()
    for indicator in indicators:
        indicator.bg_colour = BORDER
        indicator.draw()
