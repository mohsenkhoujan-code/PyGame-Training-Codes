# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 19:01:28 2023

@author: Rayan Game
"""

import pygame,sys
from random import randint as rt
import pygame.locals as pgl
import pygame.event as pge

pygame.init()

win = pygame.display.set_mode((700,700))
pygame.display.set_caption('Dance')

class it:
    def items(self):
        self.x,self.y = rt(0,600),rt(0,600)
        self.x1,self.y1 = rt(0,600),rt(0,600)
        self.x2,self.y2 = rt(0,600),rt(0,600)
        self.x3,self.y3 = rt(0,600),rt(0,600)
    def draw(self):
         pygame.draw.lines(win,(0,0,0),False,((self.x,self.y),(self.x1,self.y1),(self.x2,self.y2),(self.x3,self.y3)),3)
         self.x,self.y = rt(0,600),rt(0,600)
         self.x1,self.y1 = rt(0,600),rt(0,600)
         self.x2,self.y2 = rt(0,600),rt(0,600)
         self.x3,self.y3 = rt(0,600),rt(0,600)
         pygame.draw.lines(win,(255,255,255),False,((self.x,self.y),(self.x1,self.y1),(self.x2,self.y2),(self.x3,self.y3)),3)


its = it()
its.items()        
#draw()
import time
#gameIcon=pygame.image.load('icon.jpg')
#pygame.display.set_icon(gameIcon)
while True:
    for event in pge.get():
        if event.type == pgl.QUIT:
            pygame.quit()
            sys.exit()
    its.draw()
    time.sleep(0.01)
    pygame.display.update()
    