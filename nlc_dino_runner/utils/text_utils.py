import pygame

from nlc_dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LIGHT_MODE

FONT_STYLE = 'freesansbold.ttf'
BLACK_COLOR = (0, 0, 0)

def get_score_element(points, mode):
    font = pygame.font.Font(FONT_STYLE, 22)
    text_color = BLACK_COLOR if mode == LIGHT_MODE else (255, 255, 255)
    text = font.render('Points: ' + str(points), True, text_color) # E.g. Points : 100
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)
    return (text, text_rect)

def get_centered_message(message, width = SCREEN_WIDTH // 2, height = SCREEN_HEIGHT // 2, size=30, color = BLACK_COLOR):
    font = pygame.font.Font(FONT_STYLE, size)
    text = font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return (text, text_rect)
