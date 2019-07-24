# explains how to let the user move an image via arrow key presses
# and prevent them from moving image outside of screen

import pygame

pygame.init()
xres = 640
yres = 480
gameDisplay = pygame.display.set_mode((xres, yres))
pygame.display.set_caption('hello world')

clock = pygame.time.Clock()
quitGame = False

myImg = pygame.image.load('../assets/spaceship.png')
# make image smaller
imWidth = 60
imHeight = 100
myImg = pygame.transform.scale(myImg, (imWidth, imHeight))


def place_img(x, y):
    gameDisplay.blit(myImg, (x, y))


xImg = xres * .2
yImg = yres * .1

# define change of x and y (init to 0)
delta_x = 0
delta_y = 0
while not quitGame:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitGame = True

        # check if any key is currently being pressed
        if event.type == pygame.KEYDOWN:
            # if left key, move left
            if event.key == pygame.K_LEFT:
                delta_x = -2
            elif event.key == pygame.K_RIGHT:
                delta_x = 2
            elif event.key == pygame.K_UP:
                delta_y = -2
            elif event.key == pygame.K_DOWN:
                delta_y = 2
            elif event.key == pygame.K_ESCAPE:
                quitGame = True
        # if key released, stop moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                delta_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                delta_y = 0
        print(event)
    gameDisplay.fill((0, 0, 0))

    # update location
    xImg += delta_x
    yImg += delta_y
    place_img(xImg, yImg)

    if xImg < 0 or yImg < 0 or xImg > xres - imWidth or yImg > yres - imHeight:
        quitGame = True
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
