# adds score (number of dodged objects)
# also increases difficulty by making game faster and obstacles bigger with
# each dodged obstacle
import pygame
import time
import random
import numpy as np

# window constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 1000

# agent constants
AGENT_WIDTH = 60
AGENT_HEIGHT = 100

AGENT_STARTX = WINDOW_WIDTH * .45
AGENT_STARTY = WINDOW_HEIGHT * .75

AGENT_SPEED = 5

# image paths
PATH_AGENTIMG = '../assets/spaceship.png'
PATH_ASTEROIDIMG = '../assets/asteroid.png'

# colors
COL_WHITE = (255, 255, 255)
COL_BLACK = (0, 0, 0)
COL_YELLOW = (245, 206, 66)

# obstacle constants
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
OBSTACLE_SPEED = 7

# stars (background)
N_STARS = 100
STARS_STARTX = np.random.randint(0, WINDOW_WIDTH, N_STARS)
STARS_STARTY = np.random.randint(0, WINDOW_HEIGHT, N_STARS)
STARS_WIDTH = 2
STARS_HEIGHT = 2
STARS_SPEED = 2


pygame.init()
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('asteroids 1.0')

clock = pygame.time.Clock()

agent_img = pygame.image.load(PATH_AGENTIMG)
# make image smaller
agent_img = pygame.transform.scale(agent_img, (AGENT_WIDTH, AGENT_HEIGHT))

asteroid_img = pygame.image.load(PATH_ASTEROIDIMG)


def draw_agent(x, y):
    game_display.blit(agent_img, (x, y))


def draw_stars(x, y, w, h):
    for ii in range(x.shape[0]):
        pygame.draw.rect(game_display, COL_YELLOW, [x[ii], y[ii], w, h])


def draw_obstacle(x, y, w, h, col):
    # pygame.draw.rect(game_display, col, [x, y, w, h])
    game_display.blit(asteroid_img, (x, y))


def draw_dodgecounter(count):
    font = pygame.font.SysFont(None, 26)
    text = font.render("Avoided Collisions: " + str(count),
                True, COL_WHITE)
    game_display.blit(text, (0, 0))


def update_stars(x, y):
    for ii in range(len(x)):
        if y[ii] > WINDOW_HEIGHT:
            y[ii] = 0
            x[ii] = np.random.randint(0, WINDOW_WIDTH, 1)
    return x, y


def print_message(messageText):
    textFont = pygame.font.Font('freesansbold.ttf', 28)
    textSurface = textFont.render(messageText, True, COL_WHITE)
    textRect = textSurface.get_rect()
    textRect.center = ((WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

    game_display.blit(textSurface, textRect)
    pygame.display.update()


def agent_left_screen(waitSecs=2):
    # print message
    print_message('game over!')
    # wait for three seconds
    time.sleep(waitSecs)
    main_loop()


def agent_crashed(waitSecs=2):
    print_message('game over!')
    time.sleep(waitSecs)
    main_loop()


def main_loop():
    quitGame = False
    agentXPos = AGENT_STARTX
    agentYPos = AGENT_STARTY

    n_dodged = 0

    # define change of x and y (init to 0)
    delta_x = 0
    delta_y = 0

    # init obstacle
    obstacleXPos = random.randrange(0, agentXPos)
    obstacleYPos = -agentYPos
    obstacleSpeed = OBSTACLE_SPEED

    # init stars
    starsXPos = STARS_STARTX
    starsYPos = STARS_STARTY
    starsSpeed = STARS_SPEED

    while not quitGame:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # check if any key is currently being pressed
            if event.type == pygame.KEYDOWN:
                # if left key, move left
                if event.key == pygame.K_LEFT:
                    delta_x = -AGENT_SPEED
                elif event.key == pygame.K_RIGHT:
                    delta_x = AGENT_SPEED
                elif event.key == pygame.K_UP:
                    delta_y = -AGENT_SPEED
                elif event.key == pygame.K_DOWN:
                    delta_y = AGENT_SPEED
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            # if key released, stop moving
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    delta_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    delta_y = 0
            # print(event)
        game_display.fill(COL_BLACK)

        # draw stars
        draw_stars(starsXPos, starsYPos, STARS_WIDTH, STARS_HEIGHT)
        starsYPos += starsSpeed
        starsXPos, starsYPos = update_stars(starsXPos, starsYPos)
        # draw dodge counter
        draw_dodgecounter(n_dodged)

        # update location of agent
        agentXPos += delta_x
        agentYPos += delta_y
        draw_agent(agentXPos, agentYPos)

        # update location of obstacles
        draw_obstacle(obstacleXPos, obstacleYPos,
                        OBSTACLE_WIDTH, OBSTACLE_HEIGHT, COL_WHITE)
        obstacleYPos += obstacleSpeed

        # if obstacle has left screen, put it back on top, but
        # with new random x location
        if obstacleYPos > WINDOW_HEIGHT:
            obstacleYPos = 0-OBSTACLE_HEIGHT
            obstacleXPos = random.randrange(0, WINDOW_WIDTH)
            # count up score and increase difficulty of game
            n_dodged += 1
            obstacleSpeed += 1
            starsSpeed += 1
            # OBSTACLE_WIDTH += (n_dodged * 1.2)

        # if obstacle has touched agent, restart
        if agentYPos < obstacleYPos+OBSTACLE_HEIGHT:
            if not(agentYPos < obstacleYPos):
                if (obstacleXPos + OBSTACLE_WIDTH > agentXPos and
                        agentXPos > obstacleXPos or
                        agentXPos+AGENT_WIDTH > obstacleXPos and
                        agentXPos+AGENT_WIDTH < obstacleXPos +
                        OBSTACLE_WIDTH):
                    agent_crashed()
        # if agent has left screen, restart
        if (agentXPos < 0 or agentYPos < 0 or agentXPos
                > WINDOW_WIDTH - AGENT_WIDTH
                or agentYPos > WINDOW_HEIGHT - AGENT_HEIGHT):
            agent_left_screen()
        pygame.display.update()

        clock.tick(60)


main_loop()
pygame.quit()
quit()
