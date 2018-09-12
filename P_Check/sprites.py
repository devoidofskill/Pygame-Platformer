
import pygame as py
from settings import *


class Player(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface((20,40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.px = WIDTH / 2
        self.py = HEIGHT / 2


    def update(self):
        self.ax = 0
        self.ay = 0
        keyState = py.key.get_pressed()
        if keyState[py.K_LEFT]:
            self.ax = -PLAYER_ACC
        if keyState[py.K_RIGHT]:
            self.ax = PLAYER_ACC

        self.ax += self.vx * PLAYER_FRIC
        self.ay += self.vy * PLAYER_FRIC

        self.vx += self.ax
        self.vy += self.ay
        self.px += self.vx + .5*self.ax
        self.py += self.vy + .5*self.ay

        self.rect.center = (self.px, self.py)