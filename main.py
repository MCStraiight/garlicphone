import sys
import pygame
from pygame.locals import QUIT


pygame.init()
DISPLAYSURF = pygame.display.set_mode((1280, 720))
logo = pygame.image.load('images/logo.png')
pygame.display.set_icon(logo)
pygame.display.set_caption('Garlic Phone')
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
 
#main
