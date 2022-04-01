from unittest import runner
import pygame
pygame.init()


screen = pygame.display.set_mode((800,800))

mksurf=pygame.image.load("mick.png").convert_alpha()
mksurf= pygame.transform.scale(mksurf,(800,800))
mkrect=mksurf.get_rect()

handisurf=pygame.image.load("hand.png").convert_alpha()
handisurf=pygame.transform.scale(handisurf,(600,75))
handisurf.set_colorkey((255, 255, 255))
handirect=handisurf.get_rect(center=(400,400))

handmsurf=pygame.image.load("hand.png").convert_alpha()
handmsurf=pygame.transform.scale(handmsurf,(400,50))
handmsurf.set_colorkey((255, 255, 255))
handmrect=handmsurf.get_rect(center=(400,400))

roti=handisurf

#screen.blit(handmsurf,handmrect)

ti=pygame.time.Clock()

pygame.display.update()

running=True
m=0
i=0
while running:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
    ti.tick(1)

    roti =pygame.transform.rotate(handisurf,-6*i)
    rotm =pygame.transform.rotate(handmsurf,-0.1*i)
    roti.set_colorkey((255, 255, 255))
    rotm.set_colorkey((255, 255, 255))


    '''
    if i>=0 and i<15:
        rotrect=rot.get_rect(bottomleft=handmsurf.get_rect(bottomleft=(425,425)).bottomleft)
    elif i>=15 and i<30:
        rotrect=rot.get_rect(topleft=handmsurf.get_rect(topleft=(425,425)).topleft)
    elif i>=30 and i<45:
        rotrect=rot.get_rect(topright=handmsurf.get_rect(topright=(425,425)).topright)
    elif i>=45 and i<60:
        rotrect=rot.get_rect(bottomright=handmsurf.get_rect(bottomright=(425,425)).bottomright)

    '''

    rotrecti=roti.get_rect(center = handisurf.get_rect(center = (400,400)).center)
    rotrectm=rotm.get_rect(center = handmsurf.get_rect(center = (400,400)).center)

    screen.blit(mksurf,mkrect)
    screen.blit(roti,rotrecti)
    screen.blit(rotm, rotrectm)
    if not i==59:
        i+=1
    elif i==59 and not m==59: 
        i=0
        m+=1
    else:
        i=0
        m=0
    pygame.display.update()
    
        
    

