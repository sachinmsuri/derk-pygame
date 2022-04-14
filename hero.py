from SETTINGS import *
from floor import *
import pygame

pygame.mixer.init()


class Player(pygame.sprite.Sprite):
    BLOCK_H = 85
    BLOCK_W = 85

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.still = pygame.image.load('img/derk_still.jpg')
        self.move = pygame.image.load('img/derk_move.jpg')
        self.jump_img = pygame.image.load('img/derk_jump.jpg')
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.BLOCK_H, self.BLOCK_W)
        self.isjump = False
        self.ay = 0
        self.vy = 0

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.BLOCK_H, self.BLOCK_W)

    def show(self, action):
        if action == 1:
            screen.blit(self.still, (self.x, self.y))
        elif action == 2:
            screen.blit(self.move, (self.x, self.y))
        elif action == 3:
            screen.blit(self.jump_img, (self.x, self.y))

        """"The show method changes the players face/expression we print on ths screen
        depending on whether we are moving, jumping or standing still, these actions are 
        then called in the update method below when a user changes the position of a player """

    def jump(self):
        jumpsound = pygame.mixer.Sound("audio/jumpsoundeffect.wav")
        for ob in obs:
            if ((self.y + self.BLOCK_H) >= SCREEN_HEIGHT - BOTTOM_BORD and self.isjump == False or (
            self.rect.colliderect(ob.rect)) and (self.y == ob.y_pos - Player.BLOCK_H) and self.isjump == False):
                jumpsound.play()
                self.isjump = True
                self.vy = -18

        """"The jump method sets the attribute isjump to true allowing the player to jump, however, 
        the player can only jump if he is standing on the floor or has collided with the top of an obstacle.
        Jump gets called in the update method and within the update method we apply gravity to self.vy (jump velocity)
        and for every iteration we are adding 0.5 to self.vy which after a certain point will turn self.vy positive 
        and bring the player back down to the ground"""

    def update(self):
        x = 1
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_UP]:
            self.jump()
        if key_input[pygame.K_LEFT] and self.x > 10:
            self.x -= MOVE_SPD
            x = 2
        if key_input[pygame.K_RIGHT] and self.x < (SCREEN_WIDTH - 10 - Player.BLOCK_H):
            self.x += MOVE_SPD
            x = 2

        self.vy += 0.5
        if self.vy > 18:
            self.vy = 18
        self.y += self.vy

        if self.y + self.BLOCK_H > SCREEN_HEIGHT - BOTTOM_BORD:
            self.y = SCREEN_HEIGHT - BOTTOM_BORD - self.BLOCK_H
            self.isjump = False

        if self.isjump:
            x = 3

        self.update_rect()
        for ob in obs:
            if self.rect.colliderect(ob.rect) and abs(self.rect.top - ob.rect.bottom) < 10:
                self.vy = 0
                self.y = ob.y_pos + ob.height
            else:
                self.collision_detect()
        self.show(x)

        """"The update method updates the players position on the screen depending on user input 
        and calls the actions in the show method to print the new players position on the screen. 

        The method also adds limits to the player so it cannot fall below the floor
        of the game and has the ability to stop falling when it lands on an obstacle

        In addition we call the collision detect function; due to game speed and frame rates, 
        we initially check to see if there has been a collision with the top of the player and 
        the bottom of an object if not we check for the rest of the rectangle collisions mentioned 
        in the method collision_detect"""

    def collision_detect(self):
        for ob in obs:
            if self.rect.colliderect(ob.rect) and self.vy >= 0 and abs(self.rect.bottom - ob.rect.top) < 15:
                self.y = ob.y_pos - self.BLOCK_H
                self.vy = 0
                self.isjump = False
            elif self.rect.colliderect(ob.rect) and self.x < ob.x_pos + ob.width and self.x > ob.x_pos + ob.width / 2:
                self.x = ob.x_pos + ob.width
                self.isjump = False
            elif self.rect.colliderect(
                    ob.rect) and self.x + self.BLOCK_W > ob.x_pos and self.x < ob.x_pos + ob.width / 2:
                self.x = ob.x_pos - self.BLOCK_W
                self.isjump = False

        """"Here we check to see if a collision has occurred between the obstacles and the player
        using collide.rect and  we check to see which sides of the rectangle the collision
        has occurred and adjust the x and y coordinate accordingly.

        Left / Right Collision:
        For a left hand or right hand side collision we split the obstacle width down the middle 
        and check which side the player x position is in. 

        Top Collision:
        For a top collision due to the speed of the jump and frame rates we check to see if the top y position of 
        the obstacle minus the bottom y position of the player is within a range of 0 - 15 and making sure that 
        the velocity of the player is greater than 0 (as this tells us the player is on his way down from a jump, 
        therefore making sure we do not detect the collision when the player is jumping upwards) 
        (look at game description for more details on collisions)"""