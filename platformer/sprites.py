#Sprites
import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20, 30))
        self.image.fill(RED)
        self.game = game
        #self.bullet = Bullet
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.px = WIDTH / 2
        self.py = HEIGHT / 2

    def jump(self):
        #jump only if on platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x = 1
        if hits:
            self.vy = -30

    '''def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)'''


    def update(self):
        self.ax = 0
        self.ay = PLAYER_GRAVITY
        key_State = pg.key.get_pressed()
        if key_State[pg.K_LEFT]:
            self.ax = -PLAYER_ACCELERATION
        if key_State[pg.K_RIGHT]:
            self.ax = PLAYER_ACCELERATION

        self.ax += self.vx * PLAYER_FRICTION
        self.ay += self.vy * PLAYER_FRICTION

        self.vx += self.ax
        self.vy += self.ay
        self.px += self.vx + .5 * self.ax
        self.py += self.vy + .5 * self.ay

        self.rect.midbottom = (self.px, self.py)

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

'''class Bullet(pg.sprite.Sprite):
    def __init__(self, bx, by):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.bottom = by
        self.rect.centerx = bx
        self.speedy = -10

    def update(self):
        self.rect.y += self.vy
        if self.rect.bottom < 0:
            self.kill()'''