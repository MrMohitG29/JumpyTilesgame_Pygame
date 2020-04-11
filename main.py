import pygame as p
import random
from setting import *
from sprites import *
import os

class Game:
    def __init__(self):
        p.init()
        p.mixer.init()
        self.screen = p.display.set_mode((screen_width ,screen_height))
        p.display.set_caption("Jumpy tiles")
        self.clock = p.time.Clock()
        self.running = True
        self.font_name = p.font.match_font(FONT_NAME)
        self.score = 0
        self.load_data()

    def load_data(self):
    # load high score

        if (not os.path.exists(HS_FILE)):
            with open(HS_FILE, "w") as f:
                f.write("0")

        with open(HS_FILE, 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

    def new(self):
        self.score = 0
        self.all_sprites = p.sprite.Group()
        self.obstacle = p.sprite.Group()
        self.obstacleA = p.sprite.Group()
        self.obstacleB = p.sprite.Group()
        cor_y = 40
        for i in range(2):
            o = Obstacle(random.randint(100,250),70 + cor_y,10,10)
            self.obstacle.add(o)
            self.all_sprites.add(o)
            self.obstacleB.add(o)
            cor_y += 80

        cor_y = 50
        for i in range(1):
            width = 300
            o1 = Obstacle(-125,cor_y,width,10)
            self.obstacle.add(o1)
            self.all_sprites.add(o1)
            self.obstacleA.add(o1)
            o2 = Obstacle(225, cor_y, width, 10)
            self.obstacle.add(o2)
            self.all_sprites.add(o2)
            self.obstacleA.add(o2)


        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        if self.player.pos.y < 150:
            for i in self.obstacle:
                i.rect.y += 1

        for i in self.obstacleB:
            if i.rect.y > 299:
                i.rect.y = 0
                i.rect.x = random.randint(70,230)
                self.score +=1

        i,j  = self.obstacleA
        if i.rect.y > 299:
            a = random.choice([-25,-50,25,50])
            i.rect.x += a
            j.rect.x += a
            i.rect.y = 0
            j.rect.y = 0
            self.score += 1


        hits = p.sprite.spritecollide(self.player , self.obstacle , False)
        if hits:
            #while self.player.pos.y < 300:
            #    pass
            p.mixer.music.load('over.mp3')
            p.mixer.music.play()
            self.playing = False

    def events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(white)
        self.all_sprites.draw(self.screen)
        self.draw_text("Score: " + str(self.score), 15, black, 32 , 10)
        p.display.flip()

    def show_start_screen(self):
        self.screen.fill(white)
        self.draw_text("Jumpy Tiles", 44, black, screen_width / 2, screen_height / 4)
        self.draw_text("Arrows to move", 22, black, screen_width / 2, screen_height / 2)
        self.draw_text("Press a key to play", 20, black, screen_width / 2, screen_height * 3 / 4)
        self.draw_text("High Score: " + str(self.highscore), 22, black, screen_width / 2, 15)
        p.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        if not self.running:
            return
        self.screen.fill(white)
        self.draw_text("GAME OVER", 44, black, screen_width / 2, screen_height / 4)
        self.draw_text("Score: " + str(self.score), 22, black, screen_width / 2, screen_height / 2)
        self.draw_text("Press a key to play again", 20, black, screen_width / 2, screen_height * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!" + str(self.highscore), 22, black, screen_width / 2, screen_height / 2 + 40)
            with open(HS_FILE, 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, black, screen_width / 2, screen_height / 2 + 40)
        p.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in p.event.get():
                if event.type == p.QUIT:
                    waiting = False
                    self.running = False
                if event.type == p.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = p.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)



g = Game()
g.show_start_screen()
while g.running:
     g.new()
     g.show_go_screen()

p.quit()