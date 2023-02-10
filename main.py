import pygame
import sys
from jetski import JetSki
from obstacles import Obstacle
import utils as U
import random
import itertools

pygame.init()

JETSKI_BLUE = U.image_resize(pygame.image.load("img/bluejs.png"), 0.4)
JETSKI_GREEN = U.image_resize(pygame.image.load("img/greenjs.png"), 0.28)
JETSKI_GREEN1 = U.image_resize(pygame.image.load("img/greenjs1.png"), 0.28)
SHARK = U.image_resize(pygame.image.load("img/sharkfin.png"), 0.07)
SHARK1 = U.image_resize(pygame.image.load("img/sharkfin1.png"), 0.07)
SHARK2 = U.image_resize(pygame.image.load("img/sharkfin1.png"), 0.07)
SWIMMER = U.image_resize(pygame.image.load("img/lilolady.png"), 0.4)
OCEAN = U.image_resize(pygame.image.load("img/ocean1.png"), 1.4)


surface = pygame.display.set_mode((OCEAN.get_width(), OCEAN.get_height()))
game_running = True
clock = pygame.time.Clock()
jetski1 = JetSki(surface, JETSKI_GREEN, JETSKI_GREEN1, 400, 400)
obshark = Obstacle(jetski1, surface, SHARK, 4)
pygame.display.set_caption("Busy Harbour")
obshark.verticle_spawn(random_x=True, start_at_top=True)
swimmer = Obstacle(jetski1, surface, SWIMMER, 0.2)
swimmer.horizontal_spawn()

while game_running:
    surface.blit(OCEAN, (0, 0))
    jetski1.move()
    jetski1.draw()
    jetski1.screen_border()
    swimmer.move()
    obshark.move()
    obshark.draw()
    swimmer.draw()
    if obshark.offscreen():
        random.choice([obshark.verticle_spawn(), obshark.horizontal_spawn(
            start_left=random.choice([True, False]))])
    if swimmer.offscreen():
        random.choice([swimmer.horizontal_spawn(start_left=random.choice([True, False])), swimmer.verticle_spawn(start_at_top=random.choice([True, False]))])
    keys = pygame.key.get_pressed()
    jetski1.user_input(keys)
    obshark.collision()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    clock.tick(40)
