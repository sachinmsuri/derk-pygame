import pygame
from SETTINGS import *
import os


class Background:
    def __init__(self, x, y, file_name):
        self.x = x
        self.y = y
        self.image = pygame.image.load('img/' + file_name)

bg1 = Background(0, 0, 'bg_1.jpg')
bg2 = Background(400, 0, 'bg_2.jpg')
bg3 = Background(800, 0, 'bg_3.jpg')
bg4 = Background(1200, 0, 'bg_2.jpg')

bg_list = [bg1, bg2, bg3, bg4]

def update_bg():
    for i in bg_list:
        screen.blit(i.image, (i.x, i.y))
        i.x -= (WORLD_SPEED / 2)
        if (i.x + 400) < 0:
            i.x = 1195

