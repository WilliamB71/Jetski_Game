import pygame
import random
from utils import rotated_image_mask as rotated_image_mask


class Obstacle:
    def __init__(self, jetski: object, surface, img, speed) -> None:
        self.user_jetski = jetski
        self.surface = surface
        self.img = img
        self.speed = speed
        self.x = None
        self.y = None
        self.moving_direction = None
        self.flip_img = False

        self.mask = pygame.mask.from_surface(self.img)

    def jetski_pos_printer(self):
        print(self.user_jetski.x, self.user_jetski.y)

    def collision(self):
        jetski_mask, jetski_coords = rotated_image_mask(
            self.user_jetski.img, (self.user_jetski.x, self.user_jetski.y), self.user_jetski._angle)
        offset = (int(jetski_coords[0] - self.x),
                  int(jetski_coords[1] - self.y))
        overlap = self.mask.overlap(jetski_mask, offset)
        return overlap

    def draw(self):
        if self.flip_img:
            flipped_img = pygame.transform.flip(self.img, flip_x=True, flip_y=False)
            self.surface.blit(flipped_img, (self.x, self.y))
        ##TODO change mask and change back
        else:
            self.surface.blit(self.img, (self.x, self.y))

    def verticle_spawn(self, random_x=True, start_at_top=True, start_x=None, end_x=None):
        if random_x:
            x = random.randint(
                0, (self.surface.get_width() - self.img.get_width()))
        else:
            x = random.randint(start_x, end_x)
        self.x = x
        if start_at_top:
            y = -self.img.get_height()
            self.moving_direction = 'DOWN'
        else:
            y = self.surface.get_height()
            self.moving_direction = 'UP'

        self.y = y
        self.flip_img = False

    def horizontal_spawn(self, random_y=True, start_left=True, start_y=None, end_y=None):
        if random_y:
            y = random.randint(
                0, (self.surface.get_height() - self.img.get_height()))
        else:
            y = random.randint(start_y, end_y)
        self.y = y
        if start_left:
            x = -self.img.get_width()
            self.moving_direction = 'RIGHT'
            self.flip_img = True
        else:
            x = self.surface.get_width()
            self.moving_direction = 'LEFT'
            self.flip_img = False
        self.x = x

    def move(self):
        if self.moving_direction == 'UP':
            self.y -= self.speed
        if self.moving_direction == 'DOWN':
            self.y += self.speed
        if self.moving_direction == 'LEFT':
            self.x -= self.speed
        if self.moving_direction == 'RIGHT':
            self.x += self.speed

    def offscreen(self):
        img_height = self.img.get_height()
        img_width = self.img.get_width()
        if -abs(img_height) > self.y or self.y > (self.surface.get_height() + img_height):
            return True

        if -abs(img_width) > self.x or self.x > (self.surface.get_width() + img_width):
            return True