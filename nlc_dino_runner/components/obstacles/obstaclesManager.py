import pygame.time
import random

from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.components.obstacles.bird import Bird
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, DEAD, SOUND_HAMMER_COLLISION, \
    SOUND_COLLISION


class ObstaclesManager:

    def __init__(self):
        self.obstacles_list = []

    def update(self, game, mode):
        obstacles_types = [Cactus(SMALL_CACTUS, 325), Cactus(LARGE_CACTUS, 300), Bird()]
        if len(self.obstacles_list) == 0:
            self.obstacles_list.append(random.choice(obstacles_types))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list, mode)

            if game.power_up_manager.hammer.rect.colliderect(obstacle.rect):
                if obstacle in self.obstacles_list:
                    self.obstacles_list.remove(obstacle)
                    SOUND_HAMMER_COLLISION.play()

            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles_list.remove(obstacle)
                elif game.life_manager.life_counter() == 1:
                    game.life_manager.delete_life()
                    game.player.image = DEAD[mode]
                    game.playing = False
                    game.death_count += 1
                    game.death()
                    pygame.time.delay(1500)
                    break
                else:
                    game.life_manager.delete_life()
                    SOUND_COLLISION.play()
                    if obstacle in self.obstacles_list:
                        self.obstacles_list.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []
