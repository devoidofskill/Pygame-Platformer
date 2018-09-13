#Sprites
import pygame as pg
from settings import *
from random import choice, randrange


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_Sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((27, 48))
        self.image.fill(RED)
        self.game = game
        self.all_Sprites = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.bullet = Bullet
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
            self.vy = -50

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

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.all_Sprites.add(bullet)
        self.bullets.add(bullet)

class Platform(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((w, h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if randrange(100) < POW_SPAWN_PCT:
            Pow(self.game, self)

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.vy = -10

    def update(self):
        self.rect.y += self.vy
        if self.rect.bottom < 0:
            self.kill()

class Mob(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = MOB_LAYER
        self.groups = game.all_Sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((40, 48))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = choice([-100, WIDTH + 100])
        self.vx = randrange(1, 4)
        if self.rect.centerx > WIDTH:
            self.vx *= -1
        self.rect.y = randrange(HEIGHT / 2)
        self.vy = 0
        self.dy = 0.5

class Pow(pg.sprite.Sprite):
    def __init__(self, game, plat):
        self.groups = game.all_Sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.type = choice(['boost'])
        self.image = pg.Surface((20,20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top - 5

    def update(self):
        self.rect.bottom = self.plat.rect.top - 5
        if not self.game.platforms.has(self.plat):
            self.kill()