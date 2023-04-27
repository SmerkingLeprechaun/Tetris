import pygame
import math
import time
# init pygame
pygame.init()
# draw window
win = pygame.display.set_mode((800,600))
# setting the fps or init the fps.
clock = pygame.time.Clock()
# load image
bullet=pygame.image.load("Bullet_1.png")
# funct to update the game window
direction = 'RIGHT'
change_to = direction
set_red=False

#speed=ds/dt
length_of_snake=7
run = True
list =[[30,80],[40,80],[50,80]]
x=0
y=40
a=1
hitbox = (100, 100, 40, 40)
#b=(100,y)
b=40
go_up=False
go_down=True
no_of_frames=0
left=False
right=True
up=False
down=False
bullets=[[10,300],[11,100],[5,500]]
yb=0
while run:
    clock.tick(30)
    pi=math.pi
    print(math.sin(pi/6))
   # win.fill((34, 177, 76))
    win.fill("#b5e48c")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #change_to = 'UP'
                direction = 'UP'
            if event.key == pygame.K_DOWN:
                #change_to = 'DOWN'
                direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                #change_to = 'LEFT'
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
               # change_to = 'RIGHT'
                direction = 'RIGHT'
            if event.key==pygame.K_SPACE:
                bullets.append([0,yb])
        if event.type==pygame.KEYDOWN:
            kp=True


    list.append([list[-1][0], list[-1][1]])
   # if change_to == 'UP' and direction != 'DOWN':
    #    direction = 'UP'
    #if change_to == 'DOWN' and direction != 'UP':
     #   direction = 'DOWN'
    #if change_to == 'LEFT' and direction != 'RIGHT':
     #   direction = 'LEFT'
    #if change_to == 'RIGHT' and direction != 'LEFT':
     #   direction = 'RIGHT'

        # Moving the snake
    if direction == 'UP':
        list[-1][1] -= 10
    if direction == 'DOWN':
        list[-1][1] += 10

    if direction == 'LEFT':
        list[-1][0] -= 10
    if direction == 'RIGHT':
        list[-1][0] += 10

    if list[-1][0]>810 or list[-1][0]<20 or list[-1][1]>590 or list[-1][1]<0 :
        list.pop()
    for i in bullets:
        win.blit(bullet,i)
        i[0]+=7




    #if hitbox[0]==list[-1][0] and hitbox[1]==list[-1][1]:
     #   length_of_snake+=10
      #  set_red=not(set_red)
       # print("got it")
        #set_red=not(set_red)



    #if x top of snake head lies in range of food x coor

  #     list[-1][1]+=10
   # else:
    #    list[-1][0]+=10
        #list.append([list[-1][0]+10,list[-1][1]])

    for i in list:
        if set_red:
            color=(200,0,0)
        else:
            color=(0,0,0)

        pygame.draw.rect(win, color, (i[0] -20, i[1], 10, 10))
        #pygame.draw.circle(win, (0, 0, 0), (i, 100), 20)
        #pygame.draw.rect(win, (200, 0, 0),( i-20,80, 40, 40), 1)


    if len(list)>length_of_snake:
        list.pop(0)




    #pygame.draw.rect(win, (200, 0, 0), hitbox,1)

    no_of_frames+=1
    pygame.display.update()
pygame.quit()
# if going right
# only up and down ctrl is active and left is inactive
# if going left
# only up and down ctrl is active and right is inactive
# if going up
# only left and right ctrl is active and down is inactive
# by default go right
# right=True

# if "d" pressed:
# right=True
#
# if "w" pressed:
# up=True
# if "s" pressed:
# down=True
# if "a" pressed:
# left=True
# if right==True:
#  list.append((x+10,y))
#  left=False
# if left==True:
#  list.append((x-10,y))
# if up==True:
# list.append((x,y-10))
# if down==True:
# list.append((x,y+10))


