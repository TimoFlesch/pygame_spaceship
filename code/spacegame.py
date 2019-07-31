# http://programarcadegames.com/python_examples/show_file.php?file=game_class_example.py
# https://realpython.com/pygame-a-primer/#images

# playground
import pygame
from pygame.locals import *
import random
import numpy as np
import time

# window constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800

# agent constants
AGENT_WIDTH = 40
AGENT_HEIGHT = 60

AGENT_STARTX = WINDOW_WIDTH * .45
AGENT_STARTY = WINDOW_HEIGHT * .75

AGENT_SPEED = 7

# image paths
IMG_AGENT = '../assets/spaceship.png'
IMG_OBSTACLE = '../assets/asteroid.png'

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
STARS_WIDTH = 2
STARS_HEIGHT = 2
STARS_SPEED = 2


class Agent(pygame.sprite.Sprite):
    """docstring for Agent."""

    def __init__(self, w=AGENT_WIDTH, h=AGENT_HEIGHT, col=(255, 255, 255)):
        super(Agent, self).__init__()
        self.image = pygame.image.load(IMG_AGENT).convert()
        self.image = pygame.transform.scale(self.image,
                                (AGENT_WIDTH, AGENT_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = AGENT_STARTX
        self.rect.y = AGENT_STARTY
        self.speed = AGENT_SPEED

    def update(self, keys):
        if keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        # keep agent on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT

    def reset_pos(self):
        self.rect.x = AGENT_STARTX
        self.rect.y = AGENT_STARTY


class Obstacle(pygame.sprite.Sprite):
    """docstring for Obstacle."""

    def __init__(self):
        super(Obstacle, self).__init__()
        self.image = pygame.image.load(IMG_OBSTACLE).convert()
        self.image = pygame.transform.scale(self.image,
                            (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WINDOW_WIDTH-OBSTACLE_WIDTH)
        self.rect.y = 0-OBSTACLE_HEIGHT
        self.speed = OBSTACLE_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > WINDOW_HEIGHT:
            self.rect.x = random.randrange(0, WINDOW_WIDTH-OBSTACLE_WIDTH)
            self.rect.bottom = 0

    def reset_pos(self):
        self.rect.x = random.randrange(0, WINDOW_WIDTH-OBSTACLE_WIDTH)
        self.rect.y = 0-OBSTACLE_HEIGHT


class Star(pygame.sprite.Sprite):
    """docstring for Star."""

    def __init__(self):
        super(Star, self).__init__()
        self.surf = pygame.Surface((STARS_WIDTH, STARS_HEIGHT))
        self.surf.fill((COL_YELLOW))
        self.rect = self.surf.get_rect(center=(random.randint(0, WINDOW_WIDTH),
                                            random.randint(0, WINDOW_HEIGHT)))
        self.speed = STARS_SPEED

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > WINDOW_HEIGHT:
            self.rect.top = 0
            self.rect.x = random.randrange(0, WINDOW_WIDTH)

    def reset_pos(self):
        self.rect.x = random.randrange(0, WINDOW_WIDTH-OBSTACLE_WIDTH)
        self.rect.y = 0-OBSTACLE_HEIGHT


class Game(object):
    """instantiates a new game"""

    def __init__(self, w=WINDOW_WIDTH, h=WINDOW_HEIGHT):
        self.score = -1
        self.is_game_over = False
        self.display = pygame.display.set_mode((w, h))
        pygame.display.set_caption('asteroids game')
        self.display.fill(COL_BLACK)
        self.waitSecs = 2
        self.agent = Agent()
        self.obstacle = Obstacle()
        self.stars = pygame.sprite.Group()
        [self.stars.add(Star()) for ii in range(N_STARS)]

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
        return False

    def update_state(self):
        # overwrite prev disp content
        self.display.fill(COL_BLACK)

        # check score, if increased, update speed
        if self.obstacle.rect.bottom == 0:
            self.score += 1
            self.obstacle.speed += .5
            for star in self.stars:
                star.speed += .5

        # move agent
        keys = pygame.key.get_pressed()
        self.agent.update(keys)
        # move stars
        for star in self.stars:
            star.update()
        # move obstacles
        self.obstacle.update()


    def check_state(self):
        # check for collisions etc (i.e. game over state)
        return pygame.sprite.collide_rect(self.agent, self.obstacle)

    def disp_frame(self):
        for entity in self.stars:
            self.display.blit(entity.surf, entity.rect)
        self.display.blit(self.agent.image, self.agent.rect)
        self.display.blit(self.obstacle.image, self.obstacle.rect)
        self.disp_score()
        pygame.display.update()

    def disp_score(self):
        score_txt = 'avoided asteroids: ' + str(self.score)
        self.render_text(score_txt,18, 0.8*WINDOW_WIDTH, 0.1*WINDOW_HEIGHT)

    def disp_game_over(self):
        # print message
        self.render_text('game over :(')
        # wait for three seconds
        time.sleep(self.waitSecs)

    def render_text(self, messageText, font_size=28, x=WINDOW_WIDTH/2, y=WINDOW_HEIGHT/2):
        textFont = pygame.font.Font('freesansbold.ttf', font_size)
        textSurface = textFont.render(messageText, True, COL_WHITE)
        textRect = textSurface.get_rect()
        textRect.center = ((x, y))

        self.display.blit(textSurface, textRect)
        pygame.display.update()

    def reset_state(self):
        # resets game state
        self.agent.reset_pos()
        self.obstacle.reset_pos()
        self.obstacle.speed = OBSTACLE_SPEED
        for star in self.stars:
            star.speed = STARS_SPEED
        self.score = -1

    def run(self):
        # process events
        game_state = self.process_events()
        # update states
        self.update_state()
        # display frame
        self.disp_frame()
        # check if game over
        self.is_game_over = self.check_state()
        # if game over, reset game
        if self.is_game_over:
            self.disp_game_over()
            self.reset_state()
        # return game state (True or False)
        return game_state


def main():

    pygame.init()
    clock = pygame.time.Clock()

    game = Game()

    exit_game = False
    while not exit_game:
        # process key strokes collisions etc
        exit_game = game.run()
        # run at 60pfs
        clock.tick(60)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
