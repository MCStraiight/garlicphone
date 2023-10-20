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

logowt = pygame.image.load("images/logowt.png")
logowt = pygame.transform.scale(logowt, (300, 800))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(logowt, (100, 100))
    screen.fill((255,255,255))
    # You can use `render` and then blit the text surface ...
    text_surface, rect = GAME_FONT.render("Siwoo Company 2023. All Rights Reserved.", (0, 0, 0))
    screen.blit(text_surface, (835, 700))
    # or just `render_to` the target surface.
    GAME_FONT.render_to(screen, (3, 700), "Beta V0.0.1", (0, 0, 0))

    pygame.display.flip()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
  
pygame.quit()