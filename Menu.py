from SETTINGS import *
from main import *
import pygame
from button import *
pygame.init()
pygame.display.set_caption('Derk')
icon = pygame.image.load('img/icon.jpg')
pygame.display.set_icon(icon)


def pc():  # Creates a menu page for the character selection, although it is more of a proof of concept
    back = Button(10, 10, 100, 75, 'BACK', mm, 32)
    derk_PC = PC_Button('img/derk_menu1.png', 'img/derk_menu2.png', 500, 200)
    isaac_PC = PC_Button('img/isaac_menu1.png', 'img/isaac_menu2.png', 200, 200)
    thor_PC = PC_Button('img/thor_menu1.png', 'img/thor_menu2.png', 800, 200)
    isaac_t = pygame.font.Font('assets/code.otf', 58).render("Isaac", True, pygame.color.Color((255, 255, 255)))
    derk_t = pygame.font.Font('assets/code.otf', 58).render("Derk", True, pygame.color.Color((255, 255, 255)))
    thor_t = pygame.font.Font('assets/code.otf', 58).render("Thor", True, pygame.color.Color((255, 255, 255)))
    wip = pygame.font.Font('assets/code.otf', 25).render("* Feature not yet fully functional", True, pygame.color.Color((255, 255, 255)))
    while True:
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            pygame.quit()
        screen.blit(background, (0, 0))
        back.exist()
        derk_PC.clicked = True
        derk_PC.exist()
        isaac_PC.exist()
        thor_PC.exist()
        screen.blit(isaac_t, (215, 420))
        screen.blit(derk_t, (535, 420))
        screen.blit(thor_t, (825, 420))
        screen.blit(wip, (10, 570))
        pygame.display.flip()

def control():  # Menu page for the controls
    back = Button(10, 10, 100, 75, 'BACK', mm, 32)
    title = pygame.font.Font('assets/code.otf', 70).render("CONTROLS", True, pygame.color.Color((0, 0, 0)))
    controls = pygame.image.load('img/control.png')
    while True:
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            pygame.quit()
        screen.blit(background, (0, 0))
        back.exist()
        screen.blit(title, (425, 10))
        screen.blit(controls, (0, 50))
        pygame.display.flip()


def credit():  # menu page for credits
    back = Button(10, 10, 100, 75, 'BACK', mm, 32)
    credit_img = pygame.image.load('img/credits.png')
    while True:
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            pygame.quit()
        screen.blit(background, (0, 0))
        back.exist()
        screen.blit(credit_img, (0, 20))
        pygame.display.flip()

# Main assets for menu are created before mm is called, as this reduced load time
derk = pygame.font.Font('assets/derk.otf', 250).render("DERK", True, pygame.color.Color((0, 0, 0)))
background = pygame.image.load('img/menu_bg.png')
play = Button(450, 250, 300, 100, 'PLAY', reset, 64)
pick = Button(475, 360, 250, 50, "PICK CHARACTER", pc, 30)
control = Button(475, 420, 250, 50, "CONTROLS", control, 30)
credit = Button(475, 480, 250, 50, "CREDITS", credit, 30)
quit1 = Button(475, 540, 250, 50, "QUIT", pygame.quit, 30)
def mm():  # Main menu function, which is primarily called to run the game
    if pygame.mixer.music.get_busy() == 0:  # Checks to see if music is already playing before starting song
        pygame.mixer.music.load('audio/menu.wav')
        pygame.mixer.music.play(-1)
    while True:
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            pygame.quit()
        screen.blit(background, (0, 0))
        screen.blit(derk, (300, 10))
        play.exist()
        pick.exist()
        control.exist()
        credit.exist()
        quit1.exist()
        pygame.display.flip()


mm()



