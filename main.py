import pygame
import sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1280, 720))
logo = pygame.image.load('images/logo.png')
pygame.display.set_icon(logo)
pygame.display.set_caption('Garlic Phone')

screen = pygame.display.set_mode((1280, 720))
GAME_FONT = pygame.freetype.Font("fonts/ProximaNova.ttf", 24)
running =  True

clock = pygame.time.Clock()
logowt = pygame.image.load("images/logowt.png").convert()
# coordinates of the image
x = 10;
y = 20;
screen.blit(logowt, (x, y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    GAME_FONT.render_to(screen, (835, 700), "Siwoo Company 2023. All Rights Reserved.", (0, 0, 0))
    GAME_FONT.render_to(screen, (3, 700), "Beta V0.0.1", (0, 0, 0))
    pygame.display.flip()
    
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
  
pygame.quit()
quit()