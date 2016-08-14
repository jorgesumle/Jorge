#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygame.locals import *
import cat
import pygame

WIDTH = 1000
HEIGHT = 170
FPS = 30
LIGHT_BROWN = (111, 109, 81)

if __name__ == '__main__':
    pygame.init()
    fps_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Cat animation')

    cat = cat.Cat()

    running = True
    while running:
        pygame.display.update()
        fps_clock.tick(FPS)

        cat.walk()
        screen.fill(LIGHT_BROWN)
        screen.blit(cat.img, cat.rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                running = False
