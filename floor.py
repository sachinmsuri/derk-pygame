from SETTINGS import *
import pygame
from random import *

square_img = pygame.image.load('img/sq_ob.jpg')
hor_img = pygame.image.load('img/hor_ob.jpg')
ver_img = pygame.image.load('img/ver_ob.jpg')


class Base(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, width, height, type):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.type = type
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

        """The base class which gets inherited by the floor class creates rectangles, with specific heights 
        and positions for both the floor of the game and the obstacles of the game """

    ################################################################################
    def update_rect(self):
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def move(self, speed):
        self.x_pos = self.x_pos - speed
        self.update_rect()
        self.show()

        """The move method will shift the obstacles and print them at there new location based on 
        a WORLD_SPEED that gets adjusted in main file depending on the score of the game"""

    def show(self):
        if self.type == 'square':
            screen.blit(square_img, (self.x_pos, self.y_pos))
        if self.type == 'hor_ob':
            screen.blit(hor_img, (self.x_pos, self.y_pos))
        if self.type == 'ver_ob':
            screen.blit(ver_img, (self.x_pos, self.y_pos))

        """The show method allows to create different shaped sized obstacles with different images
        and is called when we create new obstacles within the new_obstacle function"""


class Floor(Base):
    def __init__(self, x):
        self.image = pygame.image.load('img/floor.png')
        self.x = x

    def show(self):
        self.x -= WORLD_SPEED
        screen.blit(self.image, (self.x, 308))

    """The floor class inherits from the base class, however the show method is different;
    here we move the floor constadnlty at the WORLD_SPEED"""


floor1 = Floor(0)
floor2 = Floor(1198)
floor3 = Floor(2398)
floors = [floor1, floor2, floor3]


def floor_handler():
    for floor in floors:
        floor.show()
        if floor.x < - 1200:
            floor.x = 2398

    """"Initally we have created 3 different floors all based in different x positions on the screen
    so that when they move we see one after the other, once a floor x position reaches -1200
    and is no longer visible on the screen we move it to the x position 2398 and start moving it again 
    using the show method, therefore after a period of time/iterations it will be visible on the screen again"""


a1 = Base(1200, (SCREEN_HEIGHT - BOTTOM_BORD - 200), 100, 100, 'square')
a2 = Base(1500, (SCREEN_HEIGHT - BOTTOM_BORD - 100), 100, 100, 'square')
a3 = Base(1800, (SCREEN_HEIGHT - BOTTOM_BORD - 200), 50, 200, 'ver_ob')
a4 = Base(2100, (SCREEN_HEIGHT - BOTTOM_BORD - 100), 200, 50, 'hor_ob')

obs = [a1, a2, a3, a4]


def obstacle_handler(speed):
    global obs
    for i in obs:
        i.move(speed)
        i.show()
        if i.x_pos < -200:
            del obs[0]
            obs.append(new_obstacle(1200))

    """"Initally we have created 4 different obstacles that are off the far right of the screen with different 
    positions and sizes and place them within a list. We then go through the list and move each of the obstacles
    at the world speed using the method move, once the obstacle moves leftwards through the screen and then off the screen again we delete 
    that obstacle from the list and generate a new obstacle by calling function new_obstacle."""


def new_obstacle(xpos):
    x = randint(1, 3)
    if x == 1:
        y = randint(100, 200)
        return Base((xpos), (SCREEN_HEIGHT - BOTTOM_BORD - y), 100,
                    100, 'square')
    if x == 2:
        y = randint(1, 50)
        return Base((xpos + y), (SCREEN_HEIGHT - BOTTOM_BORD - 200), 50,
                    200, "ver_ob")
    if x == 3:
        y = randint(75, 200)
        return Base((xpos), (SCREEN_HEIGHT - BOTTOM_BORD - y), 200,
                    50, "hor_ob")

    """The function new_obstacle allows us to randomly generate new obstacles within obstacle_hanlder.
    Within the function we have created three differnt types of obstacles with different sizes and positions
    and when this function is called in obstacle hanlder it will choose a random number between 1 and 3 and return 
    that specific obstacle, we have futher used random numbers within the obstacle genration so that the obstalces have
    random x and y positions"""