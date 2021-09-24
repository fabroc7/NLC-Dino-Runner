import random
from pygame.sprite import Sprite

from nlc_dino_runner.utils.constants import SCREEN_HEIGHT, LIGHT_MODE


class PowerUp(Sprite):

    def __init__(self, image, type):
        self.image = image
        self.mode = LIGHT_MODE
        self.rect = self.image[self.mode].get_rect()
        self.type = type
        self.rect.x = SCREEN_HEIGHT + random.randint(800, 1000)
        self.rect.y = random.randint(100, 150)

    def draw(self, screen):
        screen.blit(self.image[self.mode], self.rect)

    def update(self, game_speed, powerups, mode):
        self.mode = mode
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            powerups.pop()
