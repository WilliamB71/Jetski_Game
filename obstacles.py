import pygame
import random
from utils import rotated_image_mask as rotated_image_mask


class Obstacle:
    def __init__(self, jetski: object, surface, img, speed, fixed=False) -> None:
        self.user_jetski = jetski
        self.surface = surface
        self.img = img
        self.speed = speed
        self.x = None
        self.y = None
        self.moving_direction = None
        self.flip_img = False
        self.fixed = fixed

        self.mask = pygame.mask.from_surface(self.img)

    def jetski_pos_printer(self):
        print(self.user_jetski.x, self.user_jetski.y)

    def collision(self):
        jetski_mask, jetski_coords = rotated_image_mask(
            self.user_jetski.img, (self.user_jetski.x, self.user_jetski.y), self.user_jetski._angle)
        offset = (int(jetski_coords[0] - self.x),
                  int(jetski_coords[1] - self.y))
        overlap = self.mask.overlap(jetski_mask, offset)
        choice = random.choice(["Vertical", "Horizontal"])
        if overlap:
            if self.fixed:
                if self.moving_direction in ['LEFT', 'RIGHT']:
                    Obstacle.horizontal_spawn(self, random_y=False ,start_y=self.y, start_left=(self.moving_direction == 'RIGHT'))
                elif self.moving_direction in ['UP', 'DOWN']:
                    Obstacle.verticle_spawn(self, random_x=False ,start_x=self.x, start_at_top=(self.moving_direction == 'DOWN'))
            else:
                if choice == "Vertical":
                    Obstacle.verticle_spawn(self, start_at_top=random.choice([True, False]))
                elif choice == "Horizontal":
                    Obstacle.horizontal_spawn(self, start_left=random.choice([True, False]))
            self.user_jetski.take_damage()


    def draw(self):
        if self.flip_img:
            flipped_img = pygame.transform.flip(self.img, flip_x=True, flip_y=False)
            self.surface.blit(flipped_img, (self.x, self.y))
        else:
            self.surface.blit(self.img, (self.x, self.y))

    def verticle_spawn(self, random_x=True, start_at_top=True, start_x=None):
        if random_x:
            x = random.randint(
                0, (self.surface.get_width() - self.img.get_width()))
        else:
            x = start_x
        self.x = x
        if start_at_top:
            y = -self.img.get_height()
            self.moving_direction = 'DOWN'
        else:
            y = self.surface.get_height()
            self.moving_direction = 'UP'

        self.y = y
        self.flip_img = False

    def horizontal_spawn(self, random_y=True, start_left=True, start_y=None):
        if random_y:
            y = random.randint(
                0, (self.surface.get_height() - self.img.get_height()))
        else:
            y = start_y
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
    
        # off top or bottom of screen
        if -abs(img_height) > self.y or self.y > (self.surface.get_height() + img_height):
            choice = random.choice(["Vertical", "Horizontal"])
            if self.fixed:
                Obstacle.verticle_spawn(self, random_x=False ,start_at_top=(self.y>0), start_x=self.x)
            else:
                if choice == "Vertical":
                    Obstacle.verticle_spawn(self, start_at_top=random.choice([True, False]))
                elif choice == "Horizontal":
                    Obstacle.horizontal_spawn(self, start_left=random.choice([True, False]))
                    

        # off left or right of screen.
        if -abs(img_width) > self.x or self.x > (self.surface.get_width() + img_width):
                choice = random.choice(["Vertical", "Horizontal"])
                if self.fixed:
                    Obstacle.horizontal_spawn(self, random_y=False ,start_left=(self.x<0), start_y=self.y)
                else:
                    if choice == "Vertical":
                        Obstacle.verticle_spawn(self, start_at_top=random.choice([True, False]))
                    elif choice == "Horizontal":
                        Obstacle.horizontal_spawn(self, start_left=random.choice([True, False]))
