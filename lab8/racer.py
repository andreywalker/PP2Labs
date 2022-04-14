import pygame, sys
from pygame.locals import *
import random
 
pygame.init()
 
FPS = 30
FramePerSec = pygame.time.Clock()

f1 = pygame.font.Font(None, 60)
text2 = f1.render("FAILURE", True,(200,15,15))
 
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill('white')
isDead=False
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.surf= pygame.transform.scale(self.image,(120,180))
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
        self.surf= pygame.transform.scale(self.image,(120,180))
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
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if P1.getRect().colliderect(E1.getRect()):isDead=True

    if not isDead:
        P1.update()
        E1.move()
     
    DISPLAYSURF.fill('white')
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    if isDead:
        DISPLAYSURF.blit(text2,(0,300))
    pygame.display.update()
    FramePerSec.tick(FPS)       