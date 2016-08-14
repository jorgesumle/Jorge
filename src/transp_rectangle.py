#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygame.locals import *
import pygame

pygame.init()

#Resolution
WIDTH = 800
HEIGHT = 500

#Colors
BLUE = ((0, 0, 255))
RED = ((255, 0, 0))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Transparent rectangle')
screen.fill(BLUE)

font = pygame.font.Font('freesansbold.ttf', 22)
text_surf = font.render('Text', True, RED)
text_rect = text_surf.get_rect()
text_rect.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(text_surf, text_rect)

surface = pygame.Surface((100, 60))
surface.set_alpha(200)
surface_rect = surface.get_rect()
surface_rect.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(surface, surface_rect)

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            running = False

