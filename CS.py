# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 23:27:41 2023

@author: Rayan Game
"""

import pygame,sys,random

import pygame.locals as local
import pygame.event as event

pygame.init()
window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Walls")
x = 800

y = random.randint(0, 600)
xrc = random.randint(0, 20)
sx = random.randint(0, 40)
sy = random.randint(0, 40)

y1 = random.randint(0, 600)
xrc1 = random.randint(0, 20)
sx1 = random.randint(0, 40)
sy1 = random.randint(0, 40)

y2 = random.randint(0, 600)
xrc2 = random.randint(0, 20)
sx2 = random.randint(0, 40)
sy2 = random.randint(0, 40)

y3 = random.randint(0, 600)
xrc3 = random.randint(0, 20)
sx3 = random.randint(0, 40)
sy3 = random.randint(0, 40)

y4 = random.randint(0, 600)
xrc4 = random.randint(0, 20)
sx4 = random.randint(0, 40)
sy4 = random.randint(0, 40)

y5 = random.randint(0, 600)
xrc5 = random.randint(0, 20)
sx5 = random.randint(0, 40)
sy5 = random.randint(0, 40)

y6 = random.randint(0, 600)
xrc6 = random.randint(0, 20)
sx6 = random.randint(0, 40)
sy6 = random.randint(0, 40)

y7 = random.randint(0, 600)
xrc7 = random.randint(0, 20)
sx7 = random.randint(0, 40)
sy7 = random.randint(0, 40)

y8 = random.randint(0, 600)
xrc8 = random.randint(0, 20)
sx8 = random.randint(0, 40)
sy8 = random.randint(0, 40)

y9 = random.randint(0, 600)
xrc9 = random.randint(0, 20)
sx9 = random.randint(0, 40)
sy9 = random.randint(0, 40)
one = True
ownx = 400

up = False
down = False
copy = 0
Fire = False
speed = 900
speedGame = pygame.time.Clock()
#Refresh
one_ = 1

class fireplay:
    
    def old_ownxP01(self):
        self.old_ownx = ownx
    def items(self):
        self.copy = 40
        self.ownx = ownx
        self.turn = True
    def creat(self):
        if self.turn:
            pygame.draw.circle(window,(100,100,0),(self.copy,self.ownx),5)
            self.turn = False
            self.old_ownx = self.ownx
        else:
            pygame.draw.circle(window,(100,100,0),(self.copy,self.old_ownx),5)
            
    #turn2
    def items02(self):
        self.copy02 = 40
        self.ownx02 = ownx
        self.turn02 = True
    def creat02(self):
        if self.turn02:
            pygame.draw.circle(window,(100,100,0),(self.copy02,self.ownx02),5)
            self.turn02 = False
            self.old_ownx = self.ownx02
        else:
            pygame.draw.circle(window,(100,100,0),(self.copy02,self.old_ownx),5)
    #turn3
    def items03(self):
        self.copy03 = 40
        self.ownx03 = ownx
        self.turn03 = True
    def creat03(self):
        if self.turn03:
            pygame.draw.circle(window,(100,100,0),(self.copy03,self.ownx03),5)
            self.turn03 = False
            self.old_ownx = self.ownx03
        else:
            pygame.draw.circle(window,(100,100,0),(self.copy03,self.old_ownx),5)
        
    #turn4
    def items04(self):
        self.copy04 = 40
        self.ownx04 = ownx
        self.turn04 = True
    def creat04(self):
        if self.turn04:
            pygame.draw.circle(window,(100,100,0),(self.copy04,self.ownx04),5)
            self.turn04 = False
            self.old_ownx = self.ownx04
        else:
            pygame.draw.circle(window,(100,100,0),(self.copy04,self.old_ownx),5)
    #turn5
    def items05(self):
        self.copy05 = 40
        self.ownx05 = ownx
        self.turn05 = True
    def creat05(self):
        if self.turn05:
            pygame.draw.circle(window,(100,100,0),(self.copy05,self.ownx05),5)
            self.turn05 = False
            self.old_ownx = self.ownx05
        else:
            pygame.draw.circle(window,(100,100,0),(self.copy05,self.old_ownx),5)
    #turn6
    def items06(self):
        self.copy06 = 40
        self.ownx06 = ownx
        self.turn06 = True
    def creat06(self):
        if self.turn06:
            pygame.draw.circle(window,(100,100,0),(self.copy06,self.ownx06),5)
            self.turn06 = False
            self.old_ownx = self.ownx06
        else:
            pygame.draw.circle(window,(100,100,0),(self.copy06,self.old_ownx),5)
    def at(self):
        self.copy += 0.2
        self.copy02 += 0.3
        self.copy03 += 0.4
        self.copy04 += 0.5
        self.copy05 += 0.6
        self.copy06 += 0.7
cpu = fireplay()
cpu.old_ownxP01()
cpu.items()
cpu.items02()
cpu.items03()
attac = False
numberturn = 0
pygame.mixer.music.load('gun1.mp3')
while True:    
    window.fill((255,255,255))
    pygame.draw.circle(window,(255,0,255),(40,ownx),10)
    if Fire:
        cpu.items()
        cpu.items02()
        cpu.items03()
        cpu.items04()
        cpu.items05()
        cpu.items06()
        copy = cpu.copy
        Fire = False
        attac = True
    if attac:
        
        pygame.mixer.music.play(0,0.0)
        if numberturn == 0:
            cpu.at()
            cpu.creat()
            numberturn += 1
            
        if numberturn == 1:
            cpu.at()
            cpu.creat02()
            numberturn += 1
            
        if numberturn == 2:
            cpu.at()
            cpu.creat03()
            numberturn += 1
            
        if numberturn == 3:
            cpu.at()
            cpu.creat04()
            numberturn += 1
            
        if numberturn == 4:
            cpu.at()
            cpu.creat05()
            numberturn += 1
        
        if numberturn == 5:
            cpu.at()
            cpu.creat06()
            numberturn -= 5
        
    if one:
        xrc = xrc*-one_
        x += xrc
    pygame.draw.rect(window,(0,0,0),(x,y,sx,sy))
    if one:
        xrc1 = xrc1*-one_
        x += xrc1
    pygame.draw.rect(window,(0,0,0),(x,y1,sx1,sy1))
    if one:
        xrc2 = xrc2*-one_
        x += xrc2
    pygame.draw.rect(window,(0,0,0),(x,y2,sx2,sy2))
    if one:
        xrc3 = xrc3*-one_
        x += xrc3
    pygame.draw.rect(window,(0,0,0),(x,y3,sx3,sy3))
    if one:
        xrc4 = xrc4*-one_
        x += xrc4
    pygame.draw.rect(window,(0,0,0),(x,y4,sx4,sy4))
    if one:
        xrc5 = xrc5*-one_
        x += xrc5
    pygame.draw.rect(window,(0,0,0),(x,y5,sx5,sy5))
    if one:
        xrc6 = xrc6*-one_
        x += xrc6
    pygame.draw.rect(window,(0,0,0),(x,y6,sx6,sy6))
    if one:
        xrc7 = xrc7*-one_
        x += xrc7
    pygame.draw.rect(window,(0,0,0),(x,y7,sx7,sy7))
    if one:
        xrc8 = xrc8*-one_
        x += xrc8
    pygame.draw.rect(window,(0,0,0),(x,y8,sx8,sy8))
    if one:
        xrc9 = xrc9*-one_
        x += xrc9
    pygame.draw.rect(window,(0,0,0),(x,y9,sx9,sy9))
    if one:
        one = False
    for even in event.get():
        if even.type == local.QUIT:
            pygame.quit()
            sys.exit()
        if even.type == local.KEYDOWN:
            if even.key == pygame.K_UP:
                up = True
                down = False
            if even.key == pygame.K_DOWN:
                down = True
                up = False
        if even.type == local.KEYDOWN:
            if even.key == pygame.K_UP:
                up = True
                down = False
            if even.key == pygame.K_DOWN:
                down = True
                up = False 
        if even.type == local.KEYUP:
            if even.key == pygame.K_UP:
                up = False
            if even.key == pygame.K_DOWN:
                down = False
        if even.type == local.KEYDOWN:
            if even.key == pygame.K_SPACE:
                Fire = True
                
    x -= 0.1
    if up:
        if ownx <= 10.0:
            ownx = 10
        else:
            ownx -= 0.5
        
    if down:
        if ownx >= 600.0-10:
            ownx = 600-10
        else:
            ownx += 0.5
    if x <= 10:
        x = 800
        y = random.randint(0, 600)
        xrc = random.randint(0, 20)
        sx = random.randint(0, 40)
        sy = random.randint(0, 40)

        y1 = random.randint(0, 600)
        xrc1 = random.randint(0, 20)
        sx1 = random.randint(0, 40)
        sy1 = random.randint(0, 40)

        y2 = random.randint(0, 600)
        xrc2 = random.randint(0, 20)
        sx2 = random.randint(0, 40)
        sy2 = random.randint(0, 40)

        y3 = random.randint(0, 600)
        xrc3 = random.randint(0, 20)
        sx3 = random.randint(0, 40)
        sy3 = random.randint(0, 40)

        y4 = random.randint(0, 600)
        xrc4 = random.randint(0, 20)
        sx4 = random.randint(0, 40)
        sy4 = random.randint(0, 40)

        y5 = random.randint(0, 600)
        xrc5 = random.randint(0, 20)
        sx5 = random.randint(0, 40)
        sy5 = random.randint(0, 40)

        y6 = random.randint(0, 600)
        xrc6 = random.randint(0, 20)
        sx6 = random.randint(0, 40)
        sy6 = random.randint(0, 40)

        y7 = random.randint(0, 600)
        xrc7 = random.randint(0, 20)
        sx7 = random.randint(0, 40)
        sy7 = random.randint(0, 40)

        y8 = random.randint(0, 600)
        xrc8 = random.randint(0, 20)
        sx8 = random.randint(0, 40)
        sy8 = random.randint(0, 40)

        y9 = random.randint(0, 600)
        xrc9 = random.randint(0, 20)
        sx9 = random.randint(0, 40)
        sy9 = random.randint(0, 40)
        one = True
    pygame.display.update()
    speedGame.tick(speed)
    speed += 200
    