from random import randint, randrange
from pygame.locals import *
import random
import pygame
import psycopg2
import time

conn = psycopg2.connect(dbname='postgres', user='postgres', password='53515759sql', host='localhost')
cursor = conn.cursor()

tname="st0"

cursor.execute("CREATE TABLE IF NOT EXISTS "+tname+"(nick text, score int)")

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

nick=""
score=0

#prepairing text for screen of death (not blue))
f1 = pygame.font.Font(None, 60)
text2 = f1.render("FAILURE", True,(200,15,15))

#snake's parts array
snake=[]
snake.append((x0,y0))
snake.append((x0-im,y0))


#eaten apples counter
eatenApples=0

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
    aim=pygame.image.load("apple.png")
    aim2=pygame.image.load("apple2.png")
    image = random.choice((aim,aim2))
    is1=False
    if image==aim:
        is1=True
        surf= pygame.transform.scale(image,(im,im))
    else:
        is1=False
        surf= pygame.transform.scale(image,(1.5*im,1.5*im))
    return (x,y,surf, is1)

def insert(nick, num):
    cursor.execute("INSERT INTO "+tname+" VALUES ('"+nick+"' , "+str(num)+")")

def update(nick,num):
    if f[0][0]<num:
        cursor.execute("UPDATE "+tname+" SET score = "+str(num)+" WHERE nick = '"+nick+"'")
    


#some magic with framerate
fr=10
c = pygame.time.Clock()
its=0
itss=0



#cleaning the screen
screen.fill((0,0,0))
#print("filled")

#some welcome text
f3 = pygame.font.Font(None, 30)

text3 = f3.render("eNtэr your NickNAme u$iNg TERMINAl", True,(200,70,50))
#print("texted")
    
screen.blit(text3, (400,600))
#print("blited")
mim=pygame.image.load("Menu.png")
surf= pygame.transform.scale(mim,(600,400))
rect=surf.get_rect()
rect.center=(400,200) 
#print("rected")
screen.blit(surf,rect)
#print("drawed")
pygame.display.update()

nick=input("Write YouR NickName Here: ")
text3 = f3.render("Wэlcome "+nick, True,(50,200,70))
#cleaning the screen
screen.fill((0,0,0))
screen.blit(surf,rect)
screen.blit(text3, (400,600))

pygame.display.update()
cursor.execute("SELECT score FROM "+tname+" WHERE EXISTS (SELECT nick FROM "+tname+" WHERE nick = '"+nick+"')")
f=cursor.fetchall()

pygame.time.delay(4000)


def save(nick, num):
    if not f:
        insert(nick,eatenApples )
    else:
        update(nick, eatenApples)
    screen.fill((0,0,0))
    screen.blit(surf,rect)
    #print("drawed")
    
    text3 = f3.render(nick+", your Score is "+str(num), True,(50,200,70))
    screen.blit(text3, (400,600))
    pygame.display.update()
    pygame.time.delay(3500)
    cursor.execute("COMMIT")
    

while running:


    #some another magic this code to work
    c.tick(fr)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            save(nick, eatenApples)
    
    #snake ate apple variables
    ate=False
    eatenApple=()

    #cleaning the screen
    screen.fill((0,0,0))

    f1 = pygame.font.Font(None, 20)
    text1 = f1.render(str(eatenApples), True,(0, 200, 250))
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
            if apples[i][3]:
                eatenApples=eatenApples+1
                print(1)
            else:
                eatenApples=eatenApples+2
        elif di ==2 and x0-im==apples[i][0] and y0==apples[i][1]:
            ate=True
            eatenApple=i
            if apples[i][3]:
                eatenApples=eatenApples+1
                print(1)
            else:
                eatenApples=eatenApples+2
                print(2)
        elif di ==1 and x0==apples[i][0] and y0-im==apples[i][1]:
            ate=True
            eatenApple=i
            if apples[i][3]:
                eatenApples=eatenApples+1
                print(1)
            else:
                eatenApples=eatenApples+2
                print(2)
        elif di ==3 and x0==apples[i][0]  and y0+im==apples[i][1]:
            ate=True
            eatenApple=i
            if apples[i][3]:
                eatenApples=eatenApples+1
                print(1)
            else:
                eatenApples=eatenApples+2
                print(2)


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
        save(nick, eatenApples)
        running=False

    #making apple disappear after eating
    if ate:
        apples.pop(eatenApple)
    
    if itss>=50 and len(apples)>0:
        itss=0
        apples.pop(randint(0,len(apples)-1))
    else:
        itss=itss+1

    #drawing walls
    for i in range(0,len(walls)-1):
        pygame.draw.rect(screen,(170,170,80),walls[i])


    #drawing the head
    pygame.draw.circle(screen,(170,120,90),snake[0],im/2)

    #drawing the tail
    for i in range(1, len(snake)):
        pygame.draw.circle(screen,(60,180,160),snake[i],im/2)

    #print(str(ate)+"         "+str(eatenApple)+"      "+str(apples))

    #drawing apples
    for i in range(0,len(apples)-1):
        screen.blit(apples[i][2],(apples[i][0]-im,apples[i][1]-im))
    

    #making faster
    if eatenApples>=30 and fr==5:
        fr=20

    pygame.display.update()
    if not isDead:
        if its<= 20:
            its=its+1
        else:
            its=0
            apples.append(genApple())
'''
else:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu=False

    #cleaning the screen
    screen.fill((0,0,0))

    #some welcome text
    f3 = pygame.font.Font(None, 30)
    
    text3 = f3.render("eNtэr your NickNAme u$iNg TERMINAl", True,(200,70,50))
        
    screen.blit(text3, (400,600))

    mim=pygame.image.load("Menu.png")
    surf= pygame.transform.scale(mim,(600,400))
    rect=surf.get_rect()
    rect.center=(400,200) 
    screen.blit(surf,rect)

    nick=input()
    text1 = f3.render("Wэlcome "+nick, True,(50,200,70))
    #cleaning the screen
    screen.fill((0,0,0))
    screen.blit(surf,rect)
    screen.blit(text3, (400,600))
    menu=False
    running=True

'''
