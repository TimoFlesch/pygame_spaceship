# explains how to load and display an image file inside game window

import pygame

pygame.init()
xres = 640
yres = 480
gameDisplay = pygame.display.set_mode((xres, yres))
pygame.display.set_caption('hello world')

clock = pygame.time.Clock()
quitGame = False

# load image file
myImg = pygame.image.load('../assets/spaceship.png')
# make image smaller
imWidth = 60
imHeight = 100
myImg = pygame.transform.scale(myImg, (imWidth, imHeight))

# define function to place image
def place_img(x, y):
    gameDisplay.blit(myImg, (x, y))


# set location of image
xImg = xres * .2
yImg = yres * .1

while not quitGame:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitGame = True

        print(event)

    # place image
    gameDisplay.fill((0, 0, 0))
    place_img(xImg, yImg)
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
