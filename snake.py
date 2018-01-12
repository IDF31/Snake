import pygame
from pygame.locals import *
import sys
import random
#init
pygame.init()
x,y = 400,300
green = (0,255,0)
dark_green = (0,155,0)
red = (255,0,0)
speed = 7
up = 10
left = 0
length = 3
tail = []
head = Rect(x,y,10,10)
fx = random.randrange(10,580,10)
fy = random.randrange(10,780,10)
food = Rect(fx,fy,10,10)
window = pygame.display.set_mode((680,480))

#game loop 
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(speed)
    head = pygame.Rect(x,y,10,10)
     #input
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_UP and up==0:
                up=10
                left=0
            elif event.key == K_DOWN and up==0:
                up=-10
                left=0
            if event.key == K_LEFT and left==0:
                left=10
                up=0
            elif event.key == K_RIGHT and left==0:
                left=-10
                up=0
        
    x-=left
    y-=up
    
    #snake
    head = Rect(x,y,10,10)
    tail.insert(0,Rect(x+left,y+up,10,10))
    if len(tail) > length:
        tail.pop()
    
    #collision and food
    if head.colliderect(food):
        length+=1
        speed+=1
        fx = random.randrange(10,580,10)
        fy = random.randrange(10,780,10)
        food = Rect(fx,fx,10,10)
    if head.collidelist(tail) > -1:
        print("You lost!")
        running = False
    #draw
    window.fill(0)
    pygame.draw.rect(window,dark_green,head)
    for t in tail:
        pygame.draw.rect(window,green,t)
        
    pygame.draw.rect(window,red,food)
    pygame.display.update()
    
pygame.quit()
sys.exit()
