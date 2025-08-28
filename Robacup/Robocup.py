# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 12:48:49 2023

@author: Rayan Game
"""

import pygame,sys,time
from random import randint as repeat
import pygame.locals as local
import pygame.event as event

pygame.init()

win=pygame.display.set_mode((1000,700))
pygame.display.set_caption("Robocup")
icon = pygame.image.load('xc.JPG')
pygame.display.set_icon(icon)
win.fill((255,255,255))
class icx:
    def items(self):
        self.R = 255
        self.G = 10
        self.B = 40
    def rect(self):
        pygame.draw.rect(win,(self.R,self.G,self.B),(250,30,500,500))
        pygame.draw.circle(win,(255,255,255),(350,160),60)
        pygame.draw.circle(win,(255,255,255),(650,160),60)
    def tik(self,):
        pygame.draw.circle(win,(self.R,self.G,self.B),(350,155),60)
        pygame.draw.circle(win,(self.R,self.G,self.B),(650,155),60)
    def returned_tik(self):
        pygame.draw.circle(win,(255,255,255),(350,155),60)
        pygame.draw.circle(win,(255,255,255),(650,155),60)
    def tik_asked(self):
        pygame.draw.circle(win,(self.R,self.G,self.B),(650,155),60)
    
ic = icx()
ic.items()
ic.rect()
#ic.tik()
'''
class phrim:
    def items(self):
'''      

while True:
    
    
    print('f1')
    print('f2')
    for em in event.get():
        if em.type == local.QUIT:
           pygame.quit()
           sys.exit()
        
        if em.type == local.KEYDOWN:
           ic.tik_asked()
        if em.type == local.KEYUP:
           ic.rect()
        if em.type == local.MOUSEBUTTONDOWN:
            ic.R = repeat(0,255)
            ic.G = repeat(0,255)
            ic.B = repeat(0,255)
            ic.rect()
    
    
    pygame.display.update()