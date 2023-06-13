import pygame
import sys
from jetski import JetSki
from obstacles import Obstacle
import utils as U
import random


class gameplay(JetSki, Obstacle):
    def __init__(self, clock, score) -> None:
        self.clock = clock
        self.score = score
        self.JETSKI_BLUE = U.image_resize(
            pygame.image.load("img/bluejs.png"), 0.4)
        self.JETSKI_GREEN = U.image_resize(
            pygame.image.load("img/greenjs.png"), 0.28)
        self.JETSKI_GREEN1 = U.image_resize(
            pygame.image.load("img/greenjs1.png"), 0.28)
        self.SHARK = U.image_resize(
            pygame.image.load("img/sharkfin.png"), 0.07)
        self.SHARK1 = U.image_resize(
            pygame.image.load("img/sharkfin1.png"), 0.13)
        self.SHARK2 = U.image_resize(
            pygame.image.load("img/sharkfin1.png"), 0.07)
        self.SWIMMER = U.image_resize(
            pygame.image.load("img/lilolady.png"), 0.4)
        self.OCEAN = U.image_resize(pygame.image.load("img/ocean1.png"), 1.4)
        self.surface = pygame.display.set_mode(
            (self.OCEAN.get_width(), self.OCEAN.get_height()))

        self.level1_obstacles = None
        self.level2_obstacles = None
        self.level3_obstacles = None
        self.level4_obstacles = None
        self.level5_obstacles = None
        self.level6_obstacles = None

    def level1_init(self, user):
        shark = Obstacle(user, self.surface, self.SHARK, 4, True)
        shark1 = Obstacle(user, self.surface, self.SHARK, 4)
        swimmer = Obstacle(user, self.surface, self.SWIMMER, 0.4, True)
        self.level1_obstacles = [shark, shark1, swimmer]

    def level2_init(self, user):
        shark = Obstacle(user, self.surface, self.SHARK, 10)
        shark1 = Obstacle(user, self.surface, self.SHARK, 12)
        swimmer = Obstacle(user, self.surface, self.SWIMMER, 0.4)
        swimmer1 = Obstacle(user, self.surface, self.SWIMMER, 0.1)
        self.level2_obstacles = [shark, shark1, swimmer, swimmer1]

    def level3_init(self, user):
        shark = Obstacle(user, self.surface, self.SHARK, 2, True)
        shark1 = Obstacle(user, self.surface, self.SHARK, 2, True)
        shark2 = Obstacle(user, self.surface, self.SHARK, 2, True)
        swimmer1 = Obstacle(user, self.surface, self.SWIMMER, 0.4)
        swimmer2 = Obstacle(user, self.surface, self.SWIMMER, 0.4)
        swimmer3 = Obstacle(user, self.surface, self.SWIMMER, 0.4)
        swimmer4 = Obstacle(user, self.surface, self.SWIMMER, 0.4)
        swimmer5 = Obstacle(user, self.surface, self.SWIMMER, 0.4)
        swimmer6 = Obstacle(user, self.surface, self.SWIMMER, 0.4)
        swimmer7 = Obstacle(user, self.surface, self.SWIMMER, 0.4)

        self.level3_obstacles = [
            shark,
            shark1,
            shark2,
            swimmer1,
            swimmer2,
            swimmer3,
            swimmer4,
            swimmer5,
            swimmer6,
            swimmer7,
        ]

    def level4_init(self, user):
        shark = Obstacle(user, self.surface, self.SHARK1, 25)
        self.level4_obstacles = [shark]

    def level5_init(self, user):
        swimmer1 = Obstacle(user, self.surface, self.SWIMMER, 0.4)
        swimmer2 = Obstacle(user, self.surface, self.SWIMMER, 0.2)
        swimmer3 = Obstacle(user, self.surface, self.SWIMMER, 0.4)
        swimmer4 = Obstacle(user, self.surface, self.SWIMMER, 0.3)
        swimmer5 = Obstacle(user, self.surface, self.SWIMMER, 0.4)
        swimmer6 = Obstacle(user, self.surface, self.SWIMMER, 0.6)
        swimmer7 = Obstacle(user, self.surface, self.SWIMMER, 0.1)
        shark = Obstacle(user, self.surface, self.SHARK1, 8)

        self.level5_obstacles = [
            shark,
            swimmer1,
            swimmer2,
            swimmer3,
            swimmer4,
            swimmer5,
            swimmer6,
            swimmer7,
        ]

    def level6_init(self, user):
        swimmer1 = Obstacle(user, self.surface, self.SWIMMER, 0.4)
        swimmer2 = Obstacle(user, self.surface, self.SWIMMER, 0.2)
        swimmer3 = Obstacle(user, self.surface, self.SWIMMER, 0.4)
        swimmer4 = Obstacle(user, self.surface, self.SWIMMER, 0.3)
        swimmer5 = Obstacle(user, self.surface, self.SWIMMER, 0.4)
        swimmer6 = Obstacle(user, self.surface, self.SWIMMER, 0.6)
        swimmer7 = Obstacle(user, self.surface, self.SWIMMER, 0.1)
        shark = Obstacle(user, self.surface, self.SHARK1, 8)
        shark1 = Obstacle(user, self.surface, self.SHARK1, 14, True)

        self.level6_obstacles = [
            shark,
            shark1,
            swimmer1,
            swimmer2,
            swimmer3,
            swimmer4,
            swimmer5,
            swimmer6,
            swimmer7,
        ]

    def start_level(self, obstacles: list):
        for obstacle in obstacles:
            choice = random.choice(["Vertical", "Horizontal"])
            if choice == "Vertical":
                obstacle.verticle_spawn(
                    start_at_top=random.choice([True, False]))
            elif choice == "Horizontal":
                obstacle.horizontal_spawn(
                    start_left=random.choice([True, False]))

    def game_loop(self, user, obstacles: list):
        self.surface.blit(self.OCEAN, (0, 0))
        user.move()
        user.draw()
        user.screen_border()
        for obstacle in obstacles:
            obstacle.move()
            obstacle.draw()
            obstacle.offscreen()
            obstacle.collision()
        keys = pygame.key.get_pressed()
        user.user_input(keys)
        user.health_bar()
        self.score = U.score_update_display(
            self.surface, self.clock, self.score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        self.clock.tick(40)

    def introduction_screen(self):
        self.surface.blit(self.OCEAN, (0, 0))
        title_font = pygame.font.Font('freesansbold.ttf', 60)
        text_font = pygame.font.Font('freesansbold.ttf', 26)
        screen_width = self.OCEAN.get_width()

        title_display = title_font.render(
            'Busy Harbour Game', True, (255, 255, 255))
        text_display1 = text_font.render(
            'Arrow Keys to control Jetski, avoid crashing into obstacles.', True, (255, 255, 255))
        text_display2 = text_font.render(
            'Progress through levels to gain a highscore.', True, (255, 255, 255))
        title_rect = title_display.get_rect()
        text1_rect = text_display1.get_rect()
        text2_rect = text_display2.get_rect()
        title_rect.x, title_rect.y = (screen_width-title_rect.width)/2,  100
        text1_rect.x, text1_rect.y = (screen_width-text1_rect.width)/2, 500
        text2_rect.x, text2_rect.y = (screen_width-text2_rect.width)/2, 550
        self.surface.blit(self.JETSKI_GREEN, (605, 350))
        self.surface.blit(title_display, title_rect)
        self.surface.blit(text_display1, text1_rect)
        self.surface.blit(text_display2, text2_rect)
        pygame.display.flip()

    def run(self, game_running):
        user = JetSki(self.surface, self.JETSKI_GREEN,
                      self.JETSKI_GREEN1, 605, 350)
        intro_running = True
        while intro_running:
            self.introduction_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                        intro_running = False

        while game_running:
            if self.score < 1 and self.level1_obstacles == None:
                self.level1_init(user)
                obstacles = self.level1_obstacles
                self.start_level(obstacles)

            if self.score >= 20 and self.level2_obstacles == None:
                self.level2_init(user)
                obstacles = self.level2_obstacles
                self.start_level(obstacles)

            if self.score >= 40 and self.level3_obstacles == None:
                self.level3_init(user)
                obstacles = self.level3_obstacles
                self.start_level(obstacles)

            if self.score >= 60 and self.level4_obstacles == None:
                self.level4_init(user)
                obstacles = self.level4_obstacles
                self.start_level(obstacles)

            if self.score >= 80 and self.level5_obstacles == None:
                self.level5_init(user)
                obstacles = self.level5_obstacles
                self.start_level(obstacles)

            if self.score >= 100 and self.level6_obstacles == None:
                self.level6_init(user)
                obstacles = self.level6_obstacles
                self.start_level(obstacles)

            self.game_loop(user, obstacles)
