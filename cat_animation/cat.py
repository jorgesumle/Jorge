#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __init__ import WIDTH
from pygame.locals import *
import pygame


class Cat:

    def __init__(self):
        self.x_speed = -7
        self.frame1 = pygame.image.load('images/cat-walk-1.png')
        self.frame2 = pygame.image.load('images/cat-walk-2.png')
        self.img = self.frame1
        self.frame = 1
        self.FRAME_CHANGE_RATE = 4
        self.frame_counter = 0
        self.rect = self.img.get_rect()
        self.rect.x = 50
        self.rect.y = 43

    def turn_back(self):
        self.x_speed *= -1
        self.img = pygame.transform.flip(self.img, True, False)

    def walk(self):
        if self.rect.left < 0:
            self.turn_back()
        elif self.rect.right > WIDTH:
            self.turn_back()
        self.rect.x += self.x_speed
        self.change_frame()

    def change_frame(self):
        self.frame_counter += 1

        if self.frame_counter >= self.FRAME_CHANGE_RATE:
            self.frame_counter = 0
            if self.frame == 1:
                self.img = self.frame1
                self.frame = 2
            elif self.frame == 2:
                self.img = self.frame2
                self.frame = 1

            if self.x_speed > 0:
                self.img = pygame.transform.flip(self.img, True, False)