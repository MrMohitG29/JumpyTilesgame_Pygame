import pygame as p

exit_game = False
game_over = False
screen_width = 300
screen_height = 300

FPS = 150
FONT_NAME = 'courier new'

HS_FILE = "hiscore.txt"


tomato = (255,99,71)
black = (0,0,0)
red = (255,0,0)
blue = (0,150,200)
white = (244,244,244)
brown = (212,142,111)
# Player properties
PLAYER_ACC = 0.5

PLAYER_FRICTION = -0.12