import pygame
import math
from utils import center_rotate_image as center_rotate_image
from utils import rotated_image_mask as rotated_image_mask



class JetSki:
    def __init__(self, surface, img, img1, x, y) -> None:
        self.x = x
        self.y = y
        self.img = img
        self.img1 = img1
        self.width = img.get_width()
        self.height = img.get_height()
        self.surface = surface

        self._damage = 10
        self._damage_change_speed = 0.75
        self._health = 100
        self._health_border_width = 100
        self._target_health = 100
        self.health_bar_factor = 2

        self._speed = 0
        self._acceleration = 0.75
        self._reverse_acceleration = 0.25
        self._friction = 0.05
        self._max_speed = 8

        self._angle = 0
        self._rotate_speed = 0
        self._rotation_acceleration = 1
        self._rotate_friction = 0.2
        self._max_rotation = 5

        self.forward = False
        self.left = False
        self.right = False
        self.reverse = False
        

    def user_input(self, keys):
        if keys[pygame.K_UP]:
            self.forward = True
        elif not keys[pygame.K_UP]:
            self.forward = False
        if keys[pygame.K_DOWN]:
            self.reverse = True
        elif not keys[pygame.K_DOWN]:
            self.reverse = False
        if keys[pygame.K_LEFT]:
            self.left = True
        elif not keys[pygame.K_LEFT]:
            self.left = False
        if keys[pygame.K_RIGHT]:
            self.right = True
        elif not keys[pygame.K_RIGHT]:
            self.right = False

    def screen_border(self):
        surface_mask = pygame.mask.from_surface(self.surface)
        jetski_mask, jetski_coords = rotated_image_mask(self.img, (self.x, self.y), self._angle)

        a = surface_mask.overlap_area(jetski_mask, ((self.surface.get_width() / 2), (self.surface.get_height() /2)))
        b = surface_mask.overlap_area(jetski_mask, (jetski_coords[0], jetski_coords[1]))
        if a != b:
            JetSki.take_damage(self)
            temp_speed = self._speed
            self._speed =  0
            if abs(temp_speed) < 0.5:
                self._speed  -2 * temp_speed
            else:
                self._speed = -temp_speed
            
    def health_check(self):
        if self._target_health <= 0:
                pygame.quit()
            
    def take_damage(self):
        self._target_health -= self._damage

    def health_bar(self):
        
        JetSki.health_check(self)

        transition_bar_height = 0

        if self._health > self._target_health:
            self._health -= self._damage_change_speed
            transition_bar_height = 25
        
        health_width = int(self._target_health * self.health_bar_factor)
        transition_bar_width = int((self._health - self._target_health) * self.health_bar_factor)

        health_bar = pygame.Rect(10, 5, health_width, 25)
        transition_bar = pygame.Rect(health_bar.right, 5, transition_bar_width, transition_bar_height)

        pygame.draw.rect(self.surface, (0,255,0), health_bar)
        pygame.draw.rect(self.surface, (255,69,0), transition_bar)
        pygame.draw.rect(self.surface, (255,255,255), (10,5, int(self._health_border_width*self.health_bar_factor), 25), 4)


    def move(self):
        def rotate():
            if self.left:
                self._rotate_speed += self._rotation_acceleration
            if self.right:
                self._rotate_speed -= self._rotation_acceleration

            if self._rotate_speed > 0:
                self._rotate_speed -= self._rotate_friction
            else:
                self._rotate_speed += self._rotate_friction

            if abs(self._rotate_speed) < self._rotate_friction:
                self._rotate_speed = 0

            if abs(self._rotate_speed) > self._max_rotation:
                if self._rotate_speed > 0:
                    self._rotate_speed = self._max_rotation
                else:
                    self._rotate_speed = -abs(self._max_rotation)

            # will only be able to turn jetski with thrust.
            self._angle += (self._rotate_speed *
                            (self._speed / self._max_speed))

        def thrust():
            if self.forward:
                self._speed += self._acceleration
            if self.reverse:
                self._speed -= self._reverse_acceleration

            if self._speed > 0:
                self._speed -= self._friction
            else:
                self._speed += self._friction

            if abs(self._speed) <= self._friction:
                self._speed = 0

            if abs(self._speed) > self._max_speed:
                if self._speed > 0:
                    self._speed = self._max_speed
                else:
                    self._speed = -abs(self._max_speed)

        rotate()
        thrust()

        self._angle = self._angle % 360
        radian = math.radians(self._angle)
        self.x -= math.sin(radian)*self._speed
        self.y -= math.cos(radian)*self._speed

    def draw(self):
        if self.forward:
            center_rotate_image(self.surface, self.img1,
                                (self.x, self.y), self._angle)
        else:
            center_rotate_image(self.surface, self.img,
                                (self.x, self.y), self._angle)
