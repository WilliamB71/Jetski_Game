import pygame
import math

def image_resize(img, scale):
    new_dimension = round(img.get_width() * scale), round(img.get_height() * scale)
    return pygame.transform.scale(img, new_dimension)

def center_rotate_image(surface, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    surface.blit(rotated_image, new_rect.topleft)