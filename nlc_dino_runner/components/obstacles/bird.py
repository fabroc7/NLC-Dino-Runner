# clase hija
import random

from nlc_dino_runner.components.obstacles.obstacles import Obstacles


class Bird(Obstacles):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, screen):
        if self.index > 5:
            self.rect.y = 236
            screen.blit(self.image[1], self.rect)
        else:
            self.rect.y = 250
            screen.blit(self.image[0], self.rect)

        if self.index >= 9:
            self.index = 0

        self.index += 1
