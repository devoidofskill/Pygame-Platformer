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
        #self.background = pg.Surface(self.screen.get_size())
        #self.background = self.background.convert()
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)

    #restarts game
    def new(self):
        self.all_Sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.player = Player(game)
        self.mobs = pg.sprite.Group()
        self.score = 0
        self.all_Sprites.add(self.player)
        for plat in PLATFORM_LIST:
            platform = Platform(self, *plat)
            self.all_Sprites.add(platform)
            self.platforms.add(platform)
        '''bullet = Bullet(Bullet.rect.centerx, Bullet.rect.top)
        self.bullets = pg.sprite.Group()
        self.all_Sprites.add(bullet)
        self.bullets.add(bullet)'''
        self.mob_timer = 0
        self.run()
    #game loop
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
                # keep loop running at the right speed
        # Process input (events)


    def update(self):
        self.all_Sprites.update()
        if self.player.vy > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.py = hits[0].rect.top
                self.player.ay = 0
        if self.player.rect.top <= HEIGHT/4:
            self.player.py += abs(self.player.vy)
            for mob in self.mobs:
                mob.rect.y += max(abs(self.player.vy), 2)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vy)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10

        now = pg.time.get_ticks()
        if now - self.mob_timer > 5000 + random.choice([-1000, -500, 0, 500, 1000]):
            self.mob_timer = now
            Mob(self)
        # hit mobs?
        mob_hits = pg.sprite.spritecollide(self.player, self.mobs, False)
        if mob_hits:
            self.playing = False

        while len(self.platforms) < 6:
            width = random.randrange(50,100)
            p = Platform(self, random.randrange(0, WIDTH-width),
                         random.randrange(-75, -30),
                         width, 20)
            self.platforms.add(p)
            self.all_Sprites.add(p)

        for event in pg.event.get():
            #check for closing window
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    self.player.shoot()

        pow_hits = pg.sprite.spritecollide(self.player, self.powerups, True)
        for pow in pow_hits:
            if pow.type == 'boost':
                self.player.vy = -BOOST_POWER
                self.player.jumping = False

        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_Sprites:
                sprite.rect.y -= max(self.player.vy, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                if event.key == pg.K_1:
                    self.player.shoot()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_Sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)
        #self.screen.blit(self.background, (0, 0))

        pg.display.flip()

    def show_Start_Screen(self):
        pass

    def show_go_Screen(self):
        pass

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

game = Game()
game.show_Start_Screen()
#bullet = Bullet(Bullet.rect.centerx, Bullet.rect.top)
while game.running:
    game.new()
    game.show_go_Screen()
    print("Hello World")
pg.quit()

