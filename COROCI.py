# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 16:49:03 2023

@author: Rayan Game
"""

import pygame,sys

import pygame.locals as local
import pygame.event as event
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Town")
win.fill((255,255,255))
class objects:
    def items(self):
        self.x1,self.y1 = 100,100
        self.x2,self.y2 = 200,100
        self.x3,self.y3 = 100,200
        self.x4,self.y4 = 200,200
        
    def obj1(self):
        pygame.draw.polygon(win,(255,255,255),((self.x1,self.y1),(self.x2,self.y2),(self.x3,self.y3),(self.x4,self.y4)),5)
        self.x1 += 2
        self.x2 += 2
        self.x3 += 2
        self.x4 += 2
        pygame.draw.polygon(win,(0,0,0),((self.x1,self.y1),(self.x2,self.y2),(self.x3,self.y3),(self.x4,self.y4)),5)
obs = objects()
obs.items()
obs.obj1()
while True:
    for ev in event.get():
        if ev.type == local.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == local.MOUSEBUTTONDOWN:
            obs.obj1()
            if obs.x4 == 500:
                pygame.draw.polygon(win,(255,255,255),((obs.x1,obs.y1),(obs.x2,obs.y2),(obs.x3,obs.y3),(obs.x4,obs.y4)),5)
                obs.x1 = 0
                obs.x2 = 100
                obs.x3 = 0
                obs.x4 = 100
    pygame.display.update()
    