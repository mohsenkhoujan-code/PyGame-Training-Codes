# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 20:47:05 2023

@author: Rayan Game
"""

import pygame,sys
import pygame.locals as Lc
import pygame.event as Lv

pygame.init()

window = pygame.display.set_mode((500,600))
pygame.display.set_caption('Hotel de Paris')
window.fill((255,50,255))



while True:
    for event in Lv.get():
        if event.type == Lc.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()