import pygame

from nlc_dino_runner.components.Clouds import Clouds
from nlc_dino_runner.components.lifes.life_manager import LifeManager
from nlc_dino_runner.components.power_ups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils import text_utils
from nlc_dino_runner.components.dinosaur import Dinosaur
from nlc_dino_runner.components.obstacles.obstaclesManager import ObstaclesManager
from nlc_dino_runner.utils.constants import (
    TITLE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BG,
    FPS,
    ICON,
    GAME_OVER,
    DARK_MODE,
    LIGHT_MODE, SOUND_GAME_LOOP, SOUND_GAME_OVER,
)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 360
        self.player = Dinosaur()
        self.obstacle_manager = ObstaclesManager()
        self.power_up_manager = PowerUpManager()
        self.life_manager = LifeManager()
        self.clouds = Clouds()
        self.points = 0
        self.running = True
        self.death_count = 0
        self.mode = LIGHT_MODE
        self.background_color = (255, 255, 255)

    def run(self):
        # Game loop: events - update - draw
        self.points = 0
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points, self.player)
        self.life_manager.refull_lifes()
        self.game_speed = 20
        self.playing = True
        while self.playing:
            self.event()
            self.update()
            self.draw()
        SOUND_GAME_OVER.play()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()

    def update(self):
        if (self.points // 750) % 2 == 1 and self.points <= (self.points // 750) * 750 + 300:
            self.mode = DARK_MODE
        else:
            self.mode = LIGHT_MODE

        self.background_color = (0, 0, 0) if self.mode == DARK_MODE else (255, 255, 255)

        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.mode)
        self.obstacle_manager.update(self, self.mode)
        self.power_up_manager.update(self.points, self.game_speed, self.player, self.mode)
        self.life_manager.update(self.mode)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(self.background_color)
        self.score()
        self.draw_background()
        self.power_up_manager.draw(self.screen)
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.life_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def death(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.score()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.life_manager.draw(self.screen)
        self.game_over()
        pygame.display.update()
        pygame.display.flip()

    def game_over(self):
        self.screen.blit(GAME_OVER[self.mode], ((SCREEN_WIDTH // 2) - 180, (SCREEN_HEIGHT // 2) - 180))

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1

        score_element, score_element_rect = text_utils.get_score_element(self.points, self.mode)
        self.screen.blit(score_element, score_element_rect)
        self.player.check_invincibility(self.screen)

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))

        # La imagen se mueve
        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))

        # Resetear X = 0
        if self.x_pos_bg <= -image_width:
            self.x_pos_bg = 0

        self.x_pos_bg -= self.game_speed
        self.clouds.draw_clouds(self.screen, self.game_speed, self.mode)

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):
        self.running = True

        white_color = (255, 255, 255)
        self.screen.fill(white_color)

        # futuramente vamos a mostrar el menu
        self.print_menu_elements()

        pygame.display.update()

        self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2
        if self.death_count == 0:
            message = 'Press any Key to Start'
        else:
            message = 'Press any Key to Restart'

        text, text_rect = text_utils.get_centered_message(message)
        self.screen.blit(text, text_rect)

        death_score, death_score_rect = text_utils.get_centered_message('Death count: ' + str(self.death_count), height = half_screen_height + 50)
        self.screen.blit(death_score, death_score_rect)

        # Imprimir el puntaje de la última partida jugada
        score_element, score_element_rect = text_utils.get_centered_message('Last Score: ' + str(self.points), height=half_screen_height + 100)
        if self.points != 0:
            self.screen.blit(score_element, score_element_rect)

        # Imprimiendo el dinosaurio de portada
        self.screen.blit(ICON, ((SCREEN_WIDTH // 2) - 40, half_screen_height - 150))
