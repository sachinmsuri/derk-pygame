import pygame
import random
from SETTINGS import *
from hero import *
from floor import *
from background import *
from button import *
import random



def get_highscore():  # Retrieves High Score from .txt file
    hs_file = open('score.txt', 'r')
    h_score = hs_file.read()
    hs_file.close()
    return int(h_score)


def set_highscore(new_score):  # Sets a new High Score when called
    hs_file = open('score.txt', 'w')
    hs_file.write(str(int(new_score)))
    hs_file.close()

########### MAIN GAME FUNCTION ##########

def main():  # All objects for gameplay are created on the call for main
    pygame.init()
    high_score = get_highscore()
    clock = pygame.time.Clock()
    block = Player(10, (SCREEN_HEIGHT - BOTTOM_BORD - 40))    # Draws initial block
    PAUSED = False
    GAME_OVER = False
    score = 0
    paused_txt = pygame.font.SysFont('arial', 64).render('Paused', True, pygame.color.Color((255, 255, 255, 150)))
    paused_txt2 = pygame.font.SysFont('arial', 48).render('Move to continue', True, pygame.color.Color((255, 255, 255, 150)))
    paused_bg = pygame.image.load('img/pause_bg.png')
    pause_counter = 0
    GO_bg = pygame.image.load('img/GO_bg.png')
    GO_count = 0
    GO_txt = pygame.font.SysFont('arial', 64).render('Game Over', True, pygame.color.Color((255, 255, 255, 150)))
    GO_sound = pygame.mixer.Sound('audio/game_over.wav')
    GO_HS_sound = pygame.mixer.Sound('audio/GO_HS.wav')
    pygame.mixer.music.load('audio/loop1.wav')
    pygame.mixer.music.play(-1)
    global WORLD_SPEED

    ############ MAIN GAME LOOP ##################
    while True:
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            break

        if score > 250:  # Handles the increase in world speed, gradually increasing the higher score is
            WORLD_SPEED = 5
            if score > 500:
                WORLD_SPEED = 7
                if score > 750:
                    WORLD_SPEED = 10
                    if score > 1000:
                        WORLD_SPEED = 15

        key_input = pygame.key.get_pressed()

        if block.x < 0 - block.BLOCK_W:  # Detects if block has gone off screen, and therefore lost
            GAME_OVER = True

        if not (PAUSED or GAME_OVER):  # Main functional statement of game

            if key_input[pygame.K_p]:
                PAUSED = not PAUSED
            if key_input[pygame.K_ESCAPE]:
                break
            score = score + WORLD_SPEED / 20
            update_bg()
            floor_handler()
            obstacle_handler(WORLD_SPEED)
            block.update()
            high_score_txt = pygame.font.Font('assets/code.otf', 32).render(f"High Score: {str(int(high_score))}", True, pygame.color.Color((255, 255, 255, 150)))
            score_txt = pygame.font.Font('assets/code.otf', 32).render(f"Score: {str(int(score))}", True, pygame.color.Color((255, 255, 255, 150)))
            if score < high_score:  # Shows score and High score, unless High score has been beaten
                screen.blit(score_txt, (0, 0))
                screen.blit(high_score_txt, (200, 0))
            elif score > high_score:
                screen.blit(score_txt, (0, 0))

        if GAME_OVER:  # Creates all objects for Game Over screen
            GO_cen = GO_txt.get_rect(center=(SCREEN_WIDTH/2, 130))
            score_txt2 = pygame.font.Font('assets/code.otf', 128).render(str(int(score)), True, pygame.color.Color((255, 255, 255, 150)))
            score_txt_cen = score_txt2.get_rect(center=(SCREEN_WIDTH / 2, 230))
            hs_text = pygame.font.Font('assets/code.otf', 90).render('HIGH SCORE', True, pygame.color.Color((255, 255, 255, 150)))
            hs_text_cen = hs_text.get_rect(center=(SCREEN_WIDTH / 2, 320))
            not_hs = pygame.font.Font('assets/code.otf', 90).render('UNLUCKY', True, pygame.color.Color((255, 255, 255, 150)))
            not_hs_cen = not_hs.get_rect(center=(SCREEN_WIDTH / 2, 320))
            play_again = Button(500, 400, 200, 100, "Play Again", reset, 32)
            main_menu = Button(200, 400, 200, 100, "Main Menu", menu_reset, 32)
            quit_game = Button(800, 400, 200, 100, 'Quit', pygame.quit, 32)
            pygame.mixer.music.fadeout(500)

            if GO_count == 1:  # Prevents game over sound effect playing on every loop
                if score < high_score:
                    GO_sound.play(0)
                else:  # If high score has been beaten a seperate sound is played
                    GO_HS_sound.play(0)

            if GO_count < 10:  # Allows game over screen to fade in
                screen.blit(GO_bg, (0, 0))
                screen.blit(GO_txt, GO_cen)
                screen.blit(score_txt2, score_txt_cen)
                GO_count += 1
                if score > high_score:
                    set_highscore(score)
                    screen.blit(hs_text, hs_text_cen)
                else:
                    screen.blit(not_hs, not_hs_cen)
            play_again.exist()
            quit_game.exist()
            main_menu.exist()
            if main_menu.getclick():
                pygame.quit()

        if PAUSED:
            pygame.mixer.music.pause()
            if pause_counter < 1:  # Prevents items from being repeatedly drawn when paused
                screen.blit(paused_bg, (0, 0))
                screen.blit(paused_txt, ((SCREEN_WIDTH / 2)-100, (SCREEN_HEIGHT / 2) - 75))
                screen.blit(paused_txt2, ((SCREEN_WIDTH / 2-200), (SCREEN_HEIGHT / 2)))
                pause_counter += 1
            if key_input[pygame.K_UP] or key_input[pygame.K_LEFT] or key_input[pygame.K_RIGHT]:  # Unpause
                PAUSED = not PAUSED
                pygame.mixer.music.unpause()
                pause_counter = 0
            if key_input[pygame.K_ESCAPE]:
                break

        clock.tick(FRAMERATE)  # Tick to next frame
        pygame.display.flip()  # Prints entire screen

    pygame.quit()


def reset():  # A function that resets the obstacles and world speed, then calls main again. Called by 'play again' button
    global obs
    global WORLD_SPEED
    obs.clear()
    a1 = Base(1200, (SCREEN_HEIGHT - BOTTOM_BORD - 200), 100, 100, 'square')
    a2 = Base(1500, (SCREEN_HEIGHT - BOTTOM_BORD - 100), 100, 100, 'square')
    a3 = Base(1800, (SCREEN_HEIGHT - BOTTOM_BORD - 200), 50, 200, 'ver_ob')
    a4 = Base(2100, (SCREEN_HEIGHT - BOTTOM_BORD - 100), 200, 50, 'hor_ob')
    obs.append(a1)
    obs.append(a2)
    obs.append(a3)
    obs.append(a4)
    WORLD_SPEED = 4
    main()

def menu_reset():
    import Menu
    mm()





