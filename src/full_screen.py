#!/usr/bin/env python
from pygame.locals import *
import pygame

#Resolution
HEIGHT = 700
WIDTH = 700

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fullscreen demo')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

#Creates the text
font = pygame.font.Font('freesansbold.ttf', 22)
fullscreen_str = 'Press F11 to change between full screen and normal mode'
text_surf = font.render(fullscreen_str, True, WHITE, GREEN)
text_rect = text_surf.get_rect()
text_rect.center = (WIDTH / 2, HEIGHT / 2)

#Draws the text
screen.blit(text_surf, text_rect)

fullscreen = False
running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_F11:
                if pygame.display.get_driver() == 'x11':
                    pygame.display.toggle_fullscreen()
                else:
                    screen_copy = screen.copy()
                    if fullscreen:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    else:
                        screen = pygame.display.set_mode((WIDTH , HEIGHT), pygame.FULLSCREEN)
                    fullscreen = not fullscreen
                    screen.blit(screen_copy, (0, 0))
            elif event.key == K_ESCAPE:
                running = False


