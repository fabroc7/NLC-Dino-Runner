import random

from nlc_dino_runner.components.obstacles.obstacles import Obstacles
from nlc_dino_runner.utils.constants import BIRD


class Bird(Obstacles):
    def __init__(self):
        self.type = 0
        super().__init__(BIRD, self.type)
        self.rect.y = random.randint(220, 310)
        self.index = 0
        self.initial_pos_y = self.rect.y

    def draw(self, screen):
        if self.index > 5:
            self.rect.y = self.initial_pos_y - 14
            screen.blit(self.image[1], self.rect)
        else:
            self.rect.y = self.initial_pos_y
            screen.blit(self.image[0], self.rect)
        if self.index >= 9:
            self.index = 0
        self.index += 1
