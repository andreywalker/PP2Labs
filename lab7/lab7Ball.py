import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
running=True
x1=100
y1=100

x2=300
y2=300

fr=30
v0=600/fr

#ac=False
inv=True

c = pygame.time.Clock()

i=1
while running:
    '''
    if pygame.key.get_pressed()[pygame.K_o] and not a:
        a=True
    elif pygame.key.get_pressed()[pygame.K_o] and a:
        a=False'''
    if pygame.key.get_pressed()[pygame.K_i] and inv:
        inv=False
    elif pygame.key.get_pressed()[pygame.K_i] and not inv:
        inv=True
    c.tick(fr)
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
        
    screen.fill((110, 170, 140))

    v=v0

    x01=x1
    y01=y1

    x02=x2
    y02=y2
    f1 = pygame.font.Font(None, 20)
    text1 = f1.render(str(int(x1))+" "+str(int(y1))+"       UP, DWN, ->, <-", True,(0, 200, 250))
    text2 = f1.render(str(x2)+" "+str(y2)+"        W, S, D, A", True,(250, 180, 180))
    text3 = f1.render("To change mode (inverse/normal) press 'I'" , True,(250, 250, 250))

    screen.blit(text1, (10, 50))
    screen.blit(text2, (10, 75))
    screen.blit(text3, (500, 20))
    #if ac:
     #   v=v*i/50

    pygame.draw.circle(screen,(20,88,99),(x1,y1),50)
    if (pygame.key.get_pressed()[pygame.K_UP] and inv)or(pygame.key.get_pressed()[pygame.K_RIGHT] and not inv):
        if x1<=750:
            if i: x1+=v
    
    elif (pygame.key.get_pressed()[pygame.K_DOWN] and inv)or(pygame.key.get_pressed()[pygame.K_LEFT] and not inv):
        if x1>=50:
             x1-=v
    if (pygame.key.get_pressed()[pygame.K_RIGHT] and inv)or(pygame.key.get_pressed()[pygame.K_DOWN] and not inv):
        if y1<=750:
            y1+=v
    elif (pygame.key.get_pressed()[pygame.K_LEFT]and inv)or(pygame.key.get_pressed()[pygame.K_UP] and not inv):
        if y1>=50:
            y1-=v

    pygame.draw.circle(screen,(250, 180, 180),(x2,y2),50)
    if (pygame.key.get_pressed()[pygame.K_w] and inv)or(pygame.key.get_pressed()[pygame.K_d] and not inv):
        if x2<=750:
            x2+=v
    elif (pygame.key.get_pressed()[pygame.K_s] and inv)or(pygame.key.get_pressed()[pygame.K_a] and not inv):
        if x2>=50:
            x2-=v
    if (pygame.key.get_pressed()[pygame.K_d] and inv)or(pygame.key.get_pressed()[pygame.K_s] and not inv):
        if y2<=750:
            y2+=v
    elif (pygame.key.get_pressed()[pygame.K_a] and inv)or(pygame.key.get_pressed()[pygame.K_w] and not inv):
        if y2>=50:
            y2-=v
    #pygame.draw.circle(screen,(0,0,0), (x0,y0),50)
    pygame.display.update()
    if i<100:i+=1
    else:i=1