import pygame.time
import random

from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.components.obstacles.bird import Bird
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class ObstaclesManager:

    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        obstacles_types = [Cactus(SMALL_CACTUS, 325), Cactus(LARGE_CACTUS, 300), Bird()]
        if len(self.obstacles_list) == 0:
            self.obstacles_list.append(random.choice(obstacles_types))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)

            if game.power_up_manager.hammer.rect.colliderect(obstacle.rect):
                self.obstacles_list.remove(obstacle)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles_list.remove(obstacle)
                elif game.life_manager.life_counter() == 1:
                    game.life_manager.delete_life()
                    pygame.time.delay(1000)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    game.life_manager.delete_life()
                    self.obstacles_list.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []
