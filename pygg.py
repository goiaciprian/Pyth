import pygame as pyg
import sys

run = True

size = width, height = 420, 340
speed = [1, 1/2]
black = 0, 0, 0

screen = pyg.display.set_mode(size)

ball = pyg.image.load("./img/download.jpg")
ballrect = ball.get_rect()

while run:
    for event in pyg.event.get():
        if event.type == pyg.QUIT: sys.exit()

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pyg.display.flip()
