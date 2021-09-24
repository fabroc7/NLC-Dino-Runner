from pygame.sprite import Sprite

from nlc_dino_runner.utils.constants import SCREEN_WIDTH, LIGHT_MODE


# Clase padre


class Obstacles(Sprite):

    def __init__(self, image, obstacle_type):
        self.image = image
        self.mode = LIGHT_MODE
        self.obstacle_type = obstacle_type
        self.rect = self.image[self.mode][self.obstacle_type].get_rect() # retorna una tupla (x,y)
        self.rect.x = SCREEN_WIDTH #1100

    def update(self, game_speed, obstacles_list, mode):
        self.mode = mode
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles_list.pop()

    def draw(self, screen):
        screen.blit(self.image[self.mode][self.obstacle_type], self.rect)
