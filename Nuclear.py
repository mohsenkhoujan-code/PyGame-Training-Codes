# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:48:02 2023

@author: Rayan Game
"""

import pygame,sys

import pygame.locals as local
import pygame.event as event

pygame.init()

win=pygame.display.set_mode((600,500))
pygame.display.set_caption("Nuclear")

class seq:
    def items(self):
        self.x = 100
        self.y = 30
    def draw(self):
        pygame.draw.ellipse(win,(255,255,255),(200,200,self.x,self.y),1)
        self.x -= 3
        self.y += 40
seq=seq()
seq.items()
seq.draw()
    
    
    
while True:
    for em in event.get():
        if em.type == local.QUIT:
            pygame.quit()
            sys.exit()
        if em.type == local.KEYDOWN:        
            seq.draw()
    pygame.display.update()