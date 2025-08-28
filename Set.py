import pygame,sys

import pygame.locals as local
import pygame.event as event

pygame.init()


Set = pygame.display.set_mode((800,700))
pygame.display.set_caption("Image")

image = pygame.image.load('xc.png')
setx = 10
sety = 10

left = False
up = False
down = False
right = False

up_left = False
down_left = False

up_right = False
down_right = False


while True:
    Set.fill((255,255,255))
    Set.blit(image,(setx,sety))
    for ev in event.get():
        if ev.type == local.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_UP:
                up = True
            if ev.key == pygame.K_DOWN:
                down = True
            if ev.key == pygame.K_LEFT:
                left = True
            if ev.key == pygame.K_RIGHT:
                right = True
                
            if ev.key == pygame.K_LEFT and pygame.K_UP:
                up_left = True
            if ev.key == pygame.K_LEFT and pygame.K_DOWN:
                down_left = True
            
            if ev.key == pygame.K_RIGHT and pygame.K_UP:
                up_right = True
            if ev.key == pygame.K_RIGHT and pygame.K_DOWN:
                down_right = True
                
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_UP:
                up = False
            if ev.key == pygame.K_DOWN:
                down = False
            if ev.key == pygame.K_LEFT:
                left = False
            if ev.key == pygame.K_RIGHT:
                right = False
                
            if ev.key == pygame.K_LEFT and pygame.K_UP:
                up_left = False
            if ev.key == pygame.K_LEFT and pygame.K_DOWN:
                down_left = False
            
            if ev.key == pygame.K_RIGHT and pygame.K_UP:
                up_right = False
            if ev.key == pygame.K_RIGHT and pygame.K_DOWN:
                down_right = False
                
    if up:
        sety -= 0.5
    if down:
        sety += 0.5
    if right:
        setx += 0.5
    if left:
        setx -= 0.5
    
    if up_left:
        setx -= 0.5
        sety -= 0.5
        
    if down_left:
        setx -= 0.5
        sety += 0.5
        
    if up_right:
        setx += 0.5
        sety -= 0.5
        
    if down_right:
        setx += 0.5
        sety += 0.5
        
        
    pygame.display.update()
    
