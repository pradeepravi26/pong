import pygame
import sys
import random

def text_objects(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

def message_display(text, text_x, text_y, text_size, color):
        largeText = pygame.font.Font('freesansbold.ttf',text_size)
        TextSurf, TextRect = text_objects(text, largeText, color)
        TextRect.center = (text_x, text_y)
        gameDisplay.blit(TextSurf, TextRect)

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pong')

blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
leftPaddle_y = 250
rightPaddle_y = 250
leftPaddle_change = 0
rightPaddle_change = 0
crashed = False
clock = pygame.time.Clock()


# One iter of this while loop = basically 1 frame
while not crashed:

    # On a single frame, this for goes through each event made because multiple events could have been made
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rightPaddle_change = -4
            elif event.key == pygame.K_DOWN:
                rightPaddle_change = 4
            elif event.key == pygame.K_w:
                leftPaddle_change = -4
            elif event.key == pygame.K_s:
                leftPaddle_change = 4
            elif event.key == pygame.K_r:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rightPaddle_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                leftPaddle_change = 0

    # If it should run every frame it should be under this



    rightPaddle_y += rightPaddle_change
    leftPaddle_y += leftPaddle_change

    # All drawing should be under this
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, white, [30, leftPaddle_y, 20, 100])
    pygame.draw.rect(gameDisplay, white, [750, rightPaddle_y, 20, 100])
    pygame.draw.circle(gameDisplay, white, (400,300), 13)


    pygame.display.update()
    clock.tick(60)