import pygame,sys,random

import pygame.locals as local
import pygame.event as event

pygame.init()
window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Walls")
click = False
distor = 0
askey = False
numb = 0
font = pygame.font.Font("COPRGTL.ttf",50)
text = font.render(f'{numb}',True,(0,0,0))

pygame.mixer.music.load('Zang Zadi   WENITMAN.mp3')
pygame.mixer.music.play(1,1.1)
def Set():
    global distor
    pygame.draw.rect(window,(255,0,255),(5 + distor,500,50,50))
xrect = 750/2
yrect = 550/2
window.fill((255,255,255))
while True:    
    window.fill((255,255,255))
    text = font.render(f'{numb}',True,(0,0,0))
    
    pygame.draw.rect(window,(255,0,255),(xrect,yrect,100,100))
    window.blit(text,(10,10))
    posm = pygame.mouse.get_pos()
    for ev in event.get():
        if ev.type == local.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed()[0] == True:
            click = True
            askey = True
        else:
            click = False
            askey = False
        if askey:
            pygame.mouse.set_visible(0)
            xrect = posm[0] - 50
            yrect = posm[1] - 50
        else:
            pygame.mouse.set_visible(1)
        
        if click:
            if posm[0] >= xrect and posm[0] <= (750/2)+100 and posm[1] >= 550/2 and posm[1] <= (550/2)+100:
                
                Set()
                distor += 55
    numb += 1
    pygame.display.update()
        