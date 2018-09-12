#Platformer boi
import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    #init game window, etc
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    #restarts game
    def new(self):
        self.all_Sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(game)
        self.all_Sprites.add(self.player)
        for plat in PLATFORM_LIST:
            platform = Platform(*plat)
            self.all_Sprites.add(platform)
            self.platforms.add(platform)

    #game loop
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_Sprites.update()
        if self.player.vy > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.py = hits[0].rect.top
                self.player.ay = 0

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_Sprites.draw(self.screen)
        self.screen.blit(self.background, (0, 0))

        pg.display.flip()

    def show_Start_Screen(self):
        pass

    def show_go_Screen(self):
        pass

game = Game()
game.show_Start_Screen()
while game.running:
    game.new()
    game.show_go_Screen()
    print("Hello World")
pg.quit()