import pygame
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


#speed=ds/dt
run = True
list =[(50,80),(60,80),(70,80)]
x=0
y=40
a=1
hitbox = (80, y-20, 40, 40)
#b=(100,y)
b=40
go_up=False
go_down=True
no_of_frames=0
while run:
    clock.tick(20)
   # win.fill((34, 177, 76))
    win.fill("#a5a58d")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y+=10

            if event.key== pygame.K_SPACE:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN  :
                y_c = 0


    if len(list)==0:
        b=40
    if list[-1][0]>700:
        list.append((list[-1][0] , list[-1][1]+10))
    else:
        list.append((list[-1][0]+10,list[-1][1]))

    for i in list:
        pygame.draw.rect(win, (0, 0, 0), (i[0] - 20, i[1], 10, 10))
        #pygame.draw.circle(win, (0, 0, 0), (i, 100), 20)
        #pygame.draw.rect(win, (200, 0, 0),( i-20,80, 40, 40), 1)

    if len(list)>20:
        list.pop(0)




    #pygame.draw.rect(win, (200, 0, 0), hitbox,1)

    no_of_frames+=1
    pygame.display.update()
pygame.quit()

