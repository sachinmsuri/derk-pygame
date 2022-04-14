import pygame
from SETTINGS import *


class Button:  # Class used by both Menu and Main, creates general purpose button with mouse-over transparency
    def __init__(self, x, y, wid, hei, txt, action, fs):
        self.x = x
        self.y = y
        self.wid = wid
        self.hei = hei
        self.txt = txt
        self.bound = pygame.Rect(self.x, self.y, self.wid, self.hei)
        self.action = action
        self.fs = fs

    def exist(self):  # .exist is the method called within main and menu that prompt the creation of the button
        click = pygame.mouse.get_pressed()
        text_surf = pygame.font.Font('assets/code.otf', self.fs).render(self.txt, True, pygame.color.Color((0, 0, 0)))
        text_rect = text_surf.get_rect(center=(self.x + (0.5 * self.wid), self.y + (0.5 * self.hei)))
        if self.bound.collidepoint((pygame.mouse.get_pos())):
            image = pygame.Surface((self.wid, self.hei))
            image.fill((255, 255, 255))
            image.set_alpha(128)
            screen.blit(image, (self.x, self.y))
            screen.blit(text_surf, text_rect)
            if click[0] == 1:
                self.action()

        else:
            image = pygame.Surface((self.wid, self.hei))
            image.fill((255, 255, 255))
            image.set_alpha(200)
            screen.blit(image, (self.x, self.y))
            screen.blit(text_surf, text_rect)

    def getclick(self):
        click2 = pygame.mouse.get_pressed()
        if self.bound.collidepoint((pygame.mouse.get_pos())) and click2[0] == 1:
            return True


class PC_Button:  # A special version of button made for the 'Pick Character' screen on the menu.
    def __init__(self, mo_path, mno_path, x, y):
        self.mo = pygame.image.load(mo_path)
        self.mno = pygame.image.load(mno_path)
        self.x = x
        self.y = y
        self.bound = pygame.Rect(self.x, self.y, 200, 200)
        self.clicked = False

    def exist(self):
        if self.bound.collidepoint((pygame.mouse.get_pos())) or self.clicked:
            screen.blit(self.mo, (self.x, self.y))
        else:
            screen.blit(self.mno, (self.x, self.y))
