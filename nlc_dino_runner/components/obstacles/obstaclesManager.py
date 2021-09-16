import pygame.time, random

from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.components.obstacles.bird import Bird
from nlc_dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS


class ObstaclesManager:

    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        obstacles_types = [Cactus(SMALL_CACTUS, 325), Cactus(LARGE_CACTUS, 300), Bird(BIRD)]
        if len(self.obstacles_list) == 0:
            self.obstacles_list.append(random.choice(obstacles_types))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            # Rect1.colliderect(Rect2)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

# commit -m "Clase 4 - Colisiones"