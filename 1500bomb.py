# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:50:43 2023

@author: Rayan Game
"""

import pygame,sys,random
import pygame.locals as local
import pygame.event as events

pygame.init()

win = pygame.display.set_mode((1500,600))
pygame.display.set_caption(('1500bomb'))
class numb:
    numbe = 0
    print(numbe)
    border = 10
    
    stop = 50
def bombs():
    if numb.numbe >= numb.stop:
        numb.border += 100
        numb.stop += 1
    col1 = random.randint(0,255)
    col2 = random.randint(0,255)
    col3 = random.randint(0,255)
    x = random.randint(0,1500)
    y = random.randint(0,600)
    border = random.randint(0,100)
    line = random.randint(-1,100)
    pygame.draw.circle(win,(col1,col2,col3),(x,y),border,line)
    pygame.draw.ellipse(win,(col1,col2,col3),(x,y,x,y),border)
    
    numb.numbe + 1
    
    
while True:
    for en in events.get():
        if en.type == local.QUIT:
            pygame.quit()
            sys.exit()
        if en.type == local.MOUSEBUTTONDOWN:
            bombs()
    pygame.display.update()