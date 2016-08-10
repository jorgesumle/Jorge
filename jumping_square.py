#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import QUIT, K_UP


# Colors
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

WIDTH = 320
HEIGHT = 240
GRAVITY = .9
FLOOR_Y_POS = 230
FPS = 60
SQUARE_SIZE = 40

square_surf = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
square_surf.fill(GREEN)
square_rect = square_surf.get_rect()
y_speed = 0
x_pos = WIDTH / 2
y_pos = FLOOR_Y_POS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jumping square')
fps_clock = pygame.time.Clock()

running = True
while running:

    key_pressed = pygame.key.get_pressed()
    if y_speed == 0:
        if key_pressed[K_UP]:
            y_speed -= 12
    else:
        y_pos += y_speed
        y_speed += GRAVITY

        if y_pos > FLOOR_Y_POS: # Stops falling when it hits the floor
            y_speed = 0
            y_pos = FLOOR_Y_POS

    # Update square coordinates
    square_rect.bottom = int(y_pos)
    square_rect.centerx = int(x_pos)

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (0, 230, WIDTH, HEIGHT - 230)) # Floor
    screen.blit(square_surf, square_rect)

    fps_clock.tick(FPS)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
