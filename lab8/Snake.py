from random import randrange
import pygame
pygame.init()
screen=pygame.display.set_mode((800,800))
running=True

#вводим сеточную единицу измерения
im=40

#head's coordinates
x0=400
y0=400

#direction of motion
#0 right, 1 up, 2 left, 3 down
di=0

#collision happend variable
isDead=False

#prepairing text for screen of death (not blue))
f1 = pygame.font.Font(None, 60)
text2 = f1.render("FAILURE", True,(200,15,15))

#snake's parts array
snake=[]
snake.append((x0,y0))

snake.append((x0-im,y0))


#some walls
walls=[]
walls.append(pygame.Rect(300,100,im,im))
for i in range(1,9):
    walls.append(walls[i-1].move(im,0))

apples=[]


def genApple():
    x=randrange(0,800,im)
    y=randrange(0,800,im)
    for i in range(0,len(walls)-1):
        if walls[i].collidepoint(x,y):
            x=genApple()[0]
            y=genApple()[1]
    for i in range(0, len(snake)-1):
        if snake[i][0]==x and snake[i][1]==y:
            x=genApple()
            y=genApple()
    return (x,y)

#some magic with framerate
fr=5
c = pygame.time.Clock()
its=0

while running:

    
    #checking for direction buttons pressed
    if pygame.key.get_pressed()[pygame.K_UP] and not di==3:
        di=1
    elif pygame.key.get_pressed()[pygame.K_DOWN] and not di==1:
        di=3
    elif pygame.key.get_pressed()[pygame.K_RIGHT] and not di==2:
        di=0
    elif pygame.key.get_pressed()[pygame.K_LEFT] and not di ==0:
        di=2

    #some another magic this code to work
    c.tick(fr)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #snake ate apple variables
    ate=False
    eatenApple=()

    #cleaning the screen
    screen.fill((0,0,0))

    f1 = pygame.font.Font(None, 20)
    text1 = f1.render(str(x0)+" "+str(y0), True,(0, 200, 250))
    screen.blit(text1, (10, 50))

    #checking for collision with walls
    for i in range(0, len(walls)-1):
        if di==0 and walls[i].collidepoint(x0+im, y0):
            isDead=True
        elif di==2 and walls[i].collidepoint(x0-im,y0):
            isDead=True
        elif di==1 and walls[i].collidepoint(x0,y0-im):
            isDead=True
        elif di==3 and walls[i].collidepoint(x0,y0+im):
            isDead=True


    #checking for eating apples
    for i in range(0, len(apples)-1):
        if di ==0 and x0+im==apples[i][0] and y0==apples[i][1]:
            ate=True
            eatenApple=i
        elif di ==2 and x0-im==apples[i][0] and y0==apples[i][1]:
            ate=True
            eatenApple=i
        elif di ==1 and x0==apples[i][0] and y0-im==apples[i][1]:
            ate=True
            eatenApple=i
        elif di ==3 and x0==apples[i][0]  and y0+im==apples[i][1]:
            ate=True
            eatenApple=i


    #checking for collision with tail
    for i in range(0,len(snake)-1):
        if di ==0 and x0+im==snake[i][0] and y0==snake[i][1]:
            isDead=True
        elif di ==2 and x0-im==snake[i][0] and y0==snake[i][1]:
            isDead=True
        elif di ==1 and x0==snake[i][0] and y0-im==snake[i][1]:
            isDead=True
        elif di ==3 and x0==snake[i][0]  and y0+im==snake[i][1]:
            isDead=True


    if not isDead:
        #moving right
        if di==0 and not x0+im>=800:
            x0=x0+im
        elif di==0 and x0+im>=800:
            x0=0
        #moving left
        elif di==2 and not x0-im<=0:
            x0=x0-im
        elif di==2 and x0-im<=0:
            x0=800
        #moving up
        elif di==1 and not y0-im<=0:
            y0=y0-im
        elif di==1 and y0-im<=0:
            y0=800
        #moving down
        elif di==3 and not y0+im>=800:
            y0=y0+im
        elif di==3 and y0+im>=800:
            y0=0

        #moving tail of snake
        if not ate:
            for i in range(len(snake)-1,1,-1):
                snake[i]=snake[i-1]
            snake[1]=snake[0]
            #print(snake) 
        else:
            end=snake[len(snake)-1]
            for i in range(len(snake)-1,1,-1):
                snake[i]=snake[i-1]
            snake[1]=snake[0]
            snake.append(end)

        snake[0]=(x0,y0)
        
        #checking for direction buttons pressed
        if pygame.key.get_pressed()[pygame.K_UP] and not di==3:
            di=1
        elif pygame.key.get_pressed()[pygame.K_DOWN] and not di==1:
            di=3
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and not di==2:
            di=0
        elif pygame.key.get_pressed()[pygame.K_LEFT] and not di ==0:
            di=2

    else:
        screen.blit(text2,(400,400))

    #making apple disappear after eating
    if ate:
        apples.pop(eatenApple)
    

    #drawing walls
    for i in range(0,len(walls)-1):
        pygame.draw.rect(screen,(170,170,80),walls[i])


    #drawing the head
    pygame.draw.circle(screen,(170,120,90),snake[0],im/2)

    #drawing the tail
    for i in range(1, len(snake)):
        pygame.draw.circle(screen,(60,180,160),snake[i],im/2)

    print(str(ate)+"         "+str(eatenApple)+"      "+str(apples))

    #drawing apples
    for i in range(0,len(apples)-1):
        pygame.draw.circle(screen,(250,0,0),apples[i],im/2)

    pygame.display.update()
    if not isDead:
        if its<= 20:
            its=its+1
        else:
            its=0
            apples.append(genApple())
    
        