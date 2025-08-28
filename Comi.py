# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:18:03 2023

@author: Rayan Game
"""
import pygame,sys,random
import pygame.locals as pgl
import pygame.event as pge

pygame.init()

win = pygame.display.set_mode((600,400))
pygame.display.set_caption('Animes')
def draw(x,y):
    colorR = random.randint(0, 255)
    colorG = random.randint(0, 255)
    colorB = random.randint(0, 255)
    pygame.draw.rect(win,(colorR,colorG,colorB),(x,y,30,50),1)

x_,y_=10,10
draw(x_,y_)


while True:
    for event in pge.get():
        if event.type == pgl.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pgl.MOUSEBUTTONDOWN:
            x_  += 35
            if x_ >= 570:
                y_ += 55
                x_ -= 560
            draw(x_,y_)
        if event.type == pgl.KEYDOWN:
            x_  += 35
            if x_ >= 570:
                y_ += 55
                x_ -= 560
            draw(x_,y_)
            
    pygame.display.update()
