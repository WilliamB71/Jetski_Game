import pygame
from game_levels import gameplay


pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Busy Harbour")
game_running = True
score = 0


game = gameplay(clock, score)
game.run(game_running)
