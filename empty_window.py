#!/usr/bin/env python
import pygame
import sys
from pygame.locals import *

game_icon = pygame.image.load('images/icon.png')
pygame.init()
DISPLAYSURF = pygame.display.set_mode((200, 300))
pygame.display.set_caption('Empty window')
pygame.display.set_icon(game_icon)

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            running = False

