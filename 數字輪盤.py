import pygame
import os
from pygame.locals import *
import random
pygame.init()

screen=pygame.display.set_mode((404,258))
pygame.display.set_caption("數字輪盤")
clock=pygame.time.Clock()

num = pygame.image.load(os.path.join("數字盤.png")).convert()
背景 =pygame.image.load(os.path.join("背景.png")).convert()

font_name = os.path.join("font.ttf")
def draw_text(surf, text, size, x, y):#畫面 文字 大小 座標
    font = pygame.font.Font(font_name, size)#字體字體 大小
    text_surface = font.render(text, True, 640)
    text_rect = text_surface.get_rect()
    text_rect.center = x,y
    surf.blit(text_surface, text_rect)

class number1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=num
        self.rect = self.image.get_rect()
        self.rect.left=x*96+10
        if y==-1:
            self.rect.top=-1870+45*x
            self.speedy=x+1
        else:
            self.rect.top=-1870+188*y
            self.speedy=0
    def update(self):
        
        if(self.rect.top<10):
            self.rect.top +=self.speedy
        else:
            self.rect.top=-1869
            
class back(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=背景
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.left=0
        self.rect.top=0
        
numbers = pygame.sprite.Group()
backs = pygame.sprite.Group()
numbers.add(number1(0,-1))
numbers.add(number1(1,-1))
numbers.add(number1(2,-1))
numbers.add(number1(3,-1))

backs.add(back())
running=True
y=-1880
choose=False
turn=0

while running:
    
    waiting = True
    clock.tick(10000)
    
    numbers.draw(screen)
    backs.draw(screen)
    numbers.update()
    draw_text(screen, '100-200 50% 200-400 30%', 15,100,223)
    draw_text(screen, '500-900 15% 900-1000 5%', 15,100,243)
    if turn==0:
        draw_text(screen, '取號', 20,300,233)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_x,mouse_y = event.pos
                print(mouse_x,mouse_y)
                if((mouse_x>250)&(mouse_x<350)&(mouse_y>218)&(mouse_y<248)):
                    turn=1
    
    if turn==1:
        choose=True
        turn=2
        
    while choose:
        d=random.randrange(1,101)
        if d>50:
            r=random.randrange(100,201)
        elif d>20:
            r=random.randrange(200,501)
        elif d>5:
            r=random.randrange(500,901)
        elif d>0:
            r=random.randrange(900,1001)
        print(r)
        k1=r//1000%10
        k2=r//100%10
        k3=r//10%10
        k4=r%10
        print(k1,k2,k3,k4)
        numbers.empty()
        numbers.add(number1(0,k1))
        numbers.add(number1(1,k2))
        numbers.add(number1(2,k3))
        numbers.add(number1(3,k4))
        choose=False
        
    if turn==2:
        draw_text(screen, '開始', 20,300,233)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_x,mouse_y = event.pos
                print(mouse_x,mouse_y)
                if((mouse_x>250)&(mouse_x<350)&(mouse_y>218)&(mouse_y<248)):
                    turn=0
                    numbers.empty()
                    
                    numbers.add(number1(0,-1))
                    numbers.add(number1(1,-1))
                    numbers.add(number1(2,-1))
                    numbers.add(number1(3,-1))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
pygame.quit()