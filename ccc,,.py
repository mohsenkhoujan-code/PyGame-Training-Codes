# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 21:51:10 2023

@author: Rayan Game
"""

import pygame,sys
import pygame.locals as local
import pygame.event as event

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption('Save')
x_get = 5
y_get = 5
R = 0
G = 0
B = 0
run = False
place = []

getup = False

valup = 20
disc = 0
for ix in range(10,400):
    place.append(ix)
Href = 50
while True:
    win.fill((0,0,0))
    pygame.draw.line(win,(255,255,255),(10,300),(400,300),5)
    pygame.draw.rect(win,(R,G,B),(x_get,y_get,40,40))
    pygame.draw.circle(win,(255,255,255),(50,Href),10)
    for em in event.get():
        if em.type == local.QUIT:
            pygame.quit()
            sys.exit()
        if em.type == local.KEYDOWN:
            run = True
        if em.type == local.KEYUP:
            run = False
    if run:
        x_get += 0.01
        if R >= 253:
            R = 10
            G += 5
        elif B >= 253:
            B = 10
            G += 5
        elif G >= 250:
            G = 10
        else:
            R += 1
            B += 1
    if Href in place:
        getup = True
    if getup:
        Href -= 1
        disc -= 1
        if disc >= valup:
            getup = False
            valup -= 5
    else:
        Href += 1
    print(Href)
    pygame.display.update()