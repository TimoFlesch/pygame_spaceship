# draws shapes at various semi-random locations on the screen and let them move towards player

import pygame
import time
import random

pygame.init()
windowWidth = 800
windowHeight = 600
gameDisplay = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('hello world')

clock = pygame.time.Clock()

agentImg = pygame.image.load('../assets/spaceship.png')
# make image smaller
agentWidth = 60
agentHeight = 100
agentImg = pygame.transform.scale(agentImg, (agentWidth, agentHeight))


def draw_agent(x, y):
    gameDisplay.blit(agentImg, (x, y))


def draw_shape(x, y, w, h, col):
    pygame.draw.rect(gameDisplay, col, [x, y, w, h])



def print_message(messageText):
    textFont = pygame.font.Font('freesansbold.ttf', 28)
    textSurface = textFont.render(messageText, True, (255, 255, 255))
    textRect = textSurface.get_rect()
    textRect.center = ((windowWidth/2, windowHeight/2))

    gameDisplay.blit(textSurface, textRect)
    pygame.display.update()


def agent_left_screen(waitSecs=2):
    # print message
    print_message('please stay insde the window!')
    # wait for three seconds
    time.sleep(waitSecs)
    main_loop()


def main_loop():
    quitGame = False
    agentXPos = windowWidth * .45
    agentYPos = windowHeight * .75

    spaceshipSpeed = 5

    # define change of x and y (init to 0)
    delta_x = 0
    delta_y = 0

    # init shape
    shapeXPos = random.randrange(0, agentXPos)
    shapeYPos = -agentYPos
    shapeSpeed = 7
    shapeWidth = 50
    shapeHeight = 50

    while not quitGame:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # check if any key is currently being pressed
            if event.type == pygame.KEYDOWN:
                # if left key, move left
                if event.key == pygame.K_LEFT:
                    delta_x = -spaceshipSpeed
                elif event.key == pygame.K_RIGHT:
                    delta_x = spaceshipSpeed
                elif event.key == pygame.K_UP:
                    delta_y = -spaceshipSpeed
                elif event.key == pygame.K_DOWN:
                    delta_y = spaceshipSpeed
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            # if key released, stop moving
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    delta_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    delta_y = 0
            print(event)
        gameDisplay.fill((0, 0, 0))

        # update location of agent
        agentXPos += delta_x
        agentYPos += delta_y
        draw_agent(agentXPos, agentYPos)

        # update location of shapes
        draw_shape(shapeXPos, shapeYPos, shapeWidth, shapeHeight, (255, 255, 255))
        shapeYPos += shapeSpeed
        # if shape has left screen, put it back on top, but with new random x location
        if shapeYPos > windowHeight:
            shapeYPos = 0-shapeHeight
            shapeXPos = random.randrange(0, windowWidth)

        # quit if left screen
        if agentXPos < 0 or agentYPos < 0 or agentXPos > windowWidth - agentWidth or agentYPos > windowHeight - agentHeight:
            agent_left_screen()
        pygame.display.update()

        clock.tick(30)


main_loop()
pygame.quit()
quit()
