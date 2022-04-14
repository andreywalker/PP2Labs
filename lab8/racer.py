import pygame, sys
from pygame.locals import *
import random
 
pygame.init()
 
FPS = 40
FramePerSec = pygame.time.Clock()

f1 = pygame.font.Font(None, 60)
text2 = f1.render("FAILURE", True,(200,15,15))

 
fonsurf=pygame.image.load("fon.png")
fonsurf= pygame.transform.scale(fonsurf,(400,600))
fonrect=fonsurf.get_rect()



DISPLAYSURF = pygame.display.set_mode((400,600))


isDead=False
coins=0
f2 = pygame.font.Font(None, 40)


pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.surf= pygame.transform.scale(self.image,(60,90))
        self.rect=self.surf.get_rect()
        self.rect.center=(random.randint(40,360),0) 
 
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.surf, self.rect) 

      def getRect(self):
            return self.rect 
 
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.surf= pygame.transform.scale(self.image,(20,30))
        self.rect=self.surf.get_rect()
        self.rect.center=(random.randint(40,360),0) 
 
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.surf, self.rect) 

      def getRect(self):
            return self.rect 
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.surf= pygame.transform.scale(self.image,(60,90))
        self.rect=self.surf.get_rect()
        self.rect.center = (160, 520)
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < 400:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.surf, self.rect)   

    def getRect(self):
        return self.rect  
 
         
P1 = Player()
E1 = Enemy()
C1=Coin()


DISPLAYSURF.blit(fonsurf,fonrect)
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if P1.getRect().colliderect(E1.getRect()):isDead=True
    if P1.getRect().colliderect(C1.getRect()): 
        coins=coins+1
        C1=Coin()
        print(coins)
    if not isDead:
        P1.update()
        E1.move()
        C1.move()
     
    DISPLAYSURF.blit(fonsurf,fonrect)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    C1.draw(DISPLAYSURF)


    if isDead:
        DISPLAYSURF.blit(text2,(0,300))


    text1 = f2.render(str(coins), True,(250,200,50))
    DISPLAYSURF.blit(text1,(350,0))


    pygame.display.update()
    FramePerSec.tick(FPS)       