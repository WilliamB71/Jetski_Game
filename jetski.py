import pygame
import math
from pygame import Vector2
from utils import center_rotate_image as center_rotate_image


class JetSki:
    def __init__(self, surface, img, img1, x, y) -> None:
        self.x = x
        self.y = y
        self.img = img
        self.img1 = img1
        self.width = img.get_width()
        self.height = img.get_height()
        self.surface = surface

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
