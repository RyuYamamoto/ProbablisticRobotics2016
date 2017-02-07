#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import copy
import pygame
from pygame.locals import *

MASU        = 45

class MapDisplay:
    def __init__(self, map_info):
        pygame.init()
        self.map_info           = map_info
        self.row, self.colmun   = map_info.shape

        self.filed_x            = MASU * self.colmun
        self.filed_y            = MASU * self.row
        self.filed_size         = Rect(0,0,self.filed_x,self.filed_y)
        self.screen             = pygame.display.set_mode(self.filed_size.size)
        self.font               = pygame.font.SysFont("timesnewroman",22)
        pygame.display.set_caption("Q-Learning")

    def draw(self, state):
        y, x = state
        for j in range(self.row):
            for i in range(self.colmun):
                if self.map_info[j,i] == 0:
                    pygame.draw.rect(self.screen, (255,255,255), Rect(i*MASU,j*MASU,MASU,MASU))
                elif self.map_info[j,i] == -1:
                    pygame.draw.rect(self.screen, (0,0,0), Rect(i*MASU,j*MASU,MASU,MASU))
                elif self.map_info[j,i] == 3:
                    pygame.draw.rect(self.screen, (0,0,255), Rect(i*MASU,j*MASU,MASU,MASU))
                pygame.draw.rect(self.screen, (50,50,50), Rect(i*MASU,j*MASU,MASU,MASU),1)
        pygame.draw.rect(self.screen, (255,0,0), Rect(x*MASU,y*MASU,MASU,MASU),5)

    def show_policy(self, q_table):
        for x in range(self.row):
            for y in range(self.colmun):
                action = np.array(q_table[:,x,y])
                max_q_action = action.argmax()
                direction = ""
                if max_q_action == 0:
                    direction = u"←"
                elif max_q_action == 1:
                    direction = u"↓"
                elif max_q_action == 2:
                    direction = u"→"
                elif max_q_action == 3:
                    direction = u"↑"
                self.screen.blit(self.font.render(direction, True, (125,125,125)), (y*MASU+MASU/3,x*MASU+MASU/4))
