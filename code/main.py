# adds score (number of dodged objects)
# also increases difficulty by making game faster and obstacles bigger with
# each dodged obstacle
import pygame
import time
import random
import numpy as np

pygame.init()
windowWidth = 800
windowHeight = 1000
gameDisplay = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('hello world')

clock = pygame.time.Clock()

agentImg = pygame.image.load('../assets/spaceship.png')
# make image smaller
agentWidth = 60
agentHeight = 100
agentImg = pygame.transform.scale(agentImg, (agentWidth, agentHeight))

asteroidImg = pygame.image.load('../assets/asteroid.png')

def draw_agent(x, y):
    gameDisplay.blit(agentImg, (x, y))


def draw_stars(x, y, w, h):
    for ii in range(x.shape[0]):
        pygame.draw.rect(gameDisplay, (245, 206, 66), [x[ii], y[ii], w, h])


def draw_obstacle(x, y, w, h, col):
    # pygame.draw.rect(gameDisplay, col, [x, y, w, h])
    gameDisplay.blit(asteroidImg, (x, y))

def draw_dodgecounter(count):
    font = pygame.font.SysFont(None, 26)
    text = font.render("Avoided Collisions: " + str(count),
            True, (255, 255, 255))
    gameDisplay.blit(text, (0, 0))


def update_stars(x, y):
    for ii in range(len(x)):
        if y[ii] > windowHeight:
            y[ii] = 0
            x[ii] = np.random.randint(0,windowWidth,1)
    return x, y

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


def agent_crashed(waitSecs=2):
    print_message('your ship got destroyed!')
    time.sleep(waitSecs)
    main_loop()



def main_loop():
    quitGame = False
    agentXPos = windowWidth * .45
    agentYPos = windowHeight * .75

    spaceshipSpeed = 5
    dodgedItems = 0

    # define change of x and y (init to 0)
    delta_x = 0
    delta_y = 0

    # init obstacle
    obstacleXPos = random.randrange(0, agentXPos)
    obstacleYPos = -agentYPos
    obstacleSpeed = 7
    obstacleWidth = 50
    obstacleHeight = 50

    # init stars
    numStars = 100
    starsXPos = np.random.randint(0,windowWidth,numStars)
    starsYPos = np.random.randint(0,windowHeight,numStars)
    starsWidth = 2
    starsHeight = 2
    starsSpeed = 2

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

        # draw stars
        draw_stars(starsXPos, starsYPos, starsWidth, starsHeight)
        starsYPos+= starsSpeed
        starsXPos, starsYPos = update_stars(starsXPos, starsYPos)
        # draw dodge counter
        draw_dodgecounter(dodgedItems)

        # update location of agent
        agentXPos += delta_x
        agentYPos += delta_y
        draw_agent(agentXPos, agentYPos)

        # update location of obstacles
        draw_obstacle(obstacleXPos, obstacleYPos,
            obstacleWidth, obstacleHeight, (255, 255, 255))
        obstacleYPos += obstacleSpeed

        # if obstacle has left screen, put it back on top, but with new random x location
        if obstacleYPos > windowHeight:
            obstacleYPos = 0-obstacleHeight
            obstacleXPos = random.randrange(0, windowWidth)
            # count up score and increase difficulty of game
            dodgedItems += 1
            obstacleSpeed +=1
            starsSpeed += 1
            # obstacleWidth += (dodgedItems * 1.2)

        # if obstacle has touched agent, restart
        if agentYPos < obstacleYPos+obstacleHeight:
            print('y crossover')
            if not(agentYPos < obstacleYPos):
                if (obstacleXPos + obstacleWidth > agentXPos and agentXPos > obstacleXPos
                        or agentXPos+agentWidth > obstacleXPos and agentXPos+agentWidth < obstacleXPos+obstacleWidth):
                        agent_crashed()
        # if agent has left screen, restart
        if (agentXPos < 0 or agentYPos < 0 or agentXPos
                > windowWidth - agentWidth
                or agentYPos > windowHeight - agentHeight):
            agent_left_screen()
        pygame.display.update()

        clock.tick(60)


main_loop()
pygame.quit()
quit()
