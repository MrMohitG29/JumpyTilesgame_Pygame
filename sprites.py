import pygame as p
import random
from setting import *
vec = p.math.Vector2

class Player(p.sprite.Sprite):
    def __init__(self):
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface((10,10))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width/2, screen_height/2 + 50)
        self.pos = vec(screen_width/2 , screen_height/2 + 50)
        self.vel = vec(0,0)
        self.acc = vec(0,0)


    def update(self):
        p.mixer.init()
        self.acc = vec(0,0.2)
        key = p.key.get_pressed()
        p.mixer.music.load('jump.mp3')
        if key[p.K_LEFT]:
            self.acc.y = -PLAYER_ACC
            self.acc.x = -PLAYER_ACC/2
            p.mixer.music.play()

        if key[p.K_RIGHT]:
            self.acc.y = -PLAYER_ACC
            self.acc.x = PLAYER_ACC/2
            p.mixer.music.play()

        self.acc += self.vel * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.y > screen_width:
            self.pos.y = 0
        if self.pos.x < 0:
            self.pos.x = screen_width
        if self.pos.x > screen_width:
            self.pos.x = 0

        self.rect.center = self.pos


class Obstacle(p.sprite.Sprite):
    def __init__(self,x,y,w,h):
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface((w,h))
        self.image.fill(random.choice([blue , brown , tomato]))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y