#Hop Hop Hop

import pygame as py
import random
from settings import *
from sprites import *

class Game:
    #init game window, etc
    def __init__(self):
        py.init()
        py.mixer.init()
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        py.display.set_caption(TITLE)
        self.clock = py.time.Clock()
        self.running = True

    #restarts game
    def new(self):
        self.allSprites = py.sprite.Group()
        self.player = Player()
        self.allSprites.add(self.player)
        self.run()

    #game loop
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.allSprites.update()

    def events(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.allSprites.draw(self.screen)

        py.display.flip()

    def showStartScreen(self):
        pass

    def showGOScreen(self):
        pass

game = Game()
game.showStartScreen
while game.running:
    game.new()
    game.showGOScreen()

py.quit()