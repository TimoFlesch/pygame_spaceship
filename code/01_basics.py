# this code snippet explains how to open a window and log information

import pygame


# initialise pygame (required for every project)
pygame.init()

# open display/ "surface object"
xres = 640
yres = 480
gameDisplay = pygame.display.set_mode((xres, yres))
pygame.display.set_caption('hello world')


# set up game clock (counts FPS)
clock = pygame.time.Clock()

# each pygame app runs until it crashes
quitGame = False

while not quitGame:
    # create event listener (allows me to print neat info to stdout)
    for event in pygame.event.get():
        # if user closes window, terminate loop
        if event.type == pygame.QUIT:
            quitGame = True
        # if user presses the escape key, do the same:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitGame = True
        # print said info to stdout
        print(event)

    # update screen content
    # note: without arguments, this updates entire screen and is
    # quasi equivalent to Display.flip
    pygame.display.update()

    # lock game refresh rate to 30FPS
    clock.tick(30)

pygame.quit()
quit()
