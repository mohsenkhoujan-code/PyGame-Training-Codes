# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 18:25:51 2023

@author: Rayan Game
"""

import pygame,sys

import pygame.locals as local
import pygame.event as event

pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Town")
win.fill((255,255,255))
class gun:
    def items_gun(self):
        self.xg = 10
        self.yg = 220
        self.do = True
    def items_shoot(self):
        self.xs = 101
        self.ys = 226
    def objs(self):
        pygame.draw.rect(win,(255,255,255),(self.xg,self.yg,100,50))
        if self.do:
            self.yg += 10
            self.do = False
        else:
            self.yg -= 10 
            self.do = True
        pygame.draw.rect(win,(0,0,0),(self.xg,self.yg,100,50))
    def shoot(self):
        pygame.draw.line(win,(255,255,255),(self.xs,self.ys),(self.xs+10,self.ys))
        self.xs += 13
        pygame.draw.line(win,(0,0,0),(self.xs,self.ys),(self.xs+10,self.ys))
        if self.xs == 500:
            self.xs = 101
            
guns = gun()
guns.items_gun()
guns.items_shoot()
guns.objs()
while True:
    for ev in event.get():
        if ev.type == local.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == local.MOUSEBUTTONDOWN:
            guns.objs()
            guns.shoot()
       
    pygame.display.update()