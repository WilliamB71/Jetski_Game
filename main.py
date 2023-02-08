import pygame
import sys
from jetski import JetSki
import utils as U

pygame.init()

JETSKI_BLUE = U.image_resize(pygame.image.load("img/bluejs.png"), 0.4)
JETSKI_GREEN = U.image_resize(pygame.image.load("img/greenjs.png"), 0.28)
JETSKI_GREEN1 = U.image_resize(pygame.image.load("img/greenjs1.png"), 0.28)
SHARK = U.image_resize(pygame.image.load("img/sharkfin.png"), 0.07)
OCEAN = U.image_resize(pygame.image.load("img/ocean1.png"), 1.4)


surface = pygame.display.set_mode((OCEAN.get_width(), OCEAN.get_height()))
game_running = True
clock = pygame.time.Clock()
jetski1 = JetSki(surface, JETSKI_GREEN, JETSKI_GREEN1, 400, 400)
pygame.display.set_caption("Busy Harbour")
while game_running:
    surface.blit(OCEAN, (0, 0))
    jetski1.move()
    surface.blit(SHARK, (300, 300))
    jetski1.draw()

    keys = pygame.key.get_pressed()
    jetski1.user_input(keys)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    clock.tick(30)
