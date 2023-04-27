#https://novoresume.com/editor/resume/7540c870-3174-11ec-993e-e739c4a9e6c
import pygame
import time
# init pygame
pygame.init()
# draw window
WIDTH=800
HEIGHT=600
win = pygame.display.set_mode((WIDTH,HEIGHT))
# setting the fps or init the fps.
clock = pygame.time.Clock()
# load image
# funct to update the game window

points1=[[[(WIDTH//2)-200,(HEIGHT//2)-200],[(WIDTH//2)+200,(HEIGHT//2)-200],[(WIDTH//2)+200,(HEIGHT//2)+200],[(WIDTH//2)-200,(HEIGHT//2)+200]],[[(WIDTH//2)-125,(HEIGHT//2)-125],[(WIDTH//2)+125,(HEIGHT//2)-125],[(WIDTH//2)+125,(HEIGHT//2)+125],[(WIDTH//2)-125,(HEIGHT//2)+125]]]
points=[[[423-200,323-200], [376+200,323-200], [376+200 ,276+200],[423-200 ,276+200]],[[414-125,314-125],[386+125,	314-125],[386+125,	286+125],[414-125,	286+125]]]
#speed=ds/dt
run = True

while run:
    clock.tick(30)
    win.fill((34, 177, 76))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.line(win,(0,0,0), points[0][0],points[0][1],3)
    pygame.draw.line(win,(0,0,0), points[0][1], points[0][2],3)
    pygame.draw.line(win,(0,0,0), points[0][2], points[0][3],3)
    pygame.draw.line(win,(0,0,0), points[0][3], points[0][0],3)


    pygame.draw.line(win, (0, 0, 0), points[1][0], points[1][1], 3)
    pygame.draw.line(win, (0, 0, 0), points[1][1], points[1][2], 3)
    pygame.draw.line(win, (0, 0, 0), points[1][2], points[1][3], 3)
    pygame.draw.line(win, (0, 0, 0), points[1][3], points[1][0], 3)

    pygame.draw.line(win, (0, 0, 0), points[0][0], points[1][0], 3)
    pygame.draw.line(win, (0, 0, 0), points[0][1], points[1][1], 3)
    pygame.draw.line(win, (0, 0, 0), points[0][2], points[1][2], 3)
    pygame.draw.line(win, (0, 0, 0), points[0][3], points[1][3], 3)
    #pygame.draw.line(win,(0,0,0), (150, 30), (250, 130),3)
    #pygame.draw.line(win,(0,0,0), (650, 30), (550, 130),3)
    #pygame.draw.line(win,(0,0,0), (650, 530), (550, 430),3)
    #pygame.draw.line(win,(0,0,0), (150, 530), (250, 430),3)

    #pygame.draw.line(win, (0, 0, 0), (250, 130), (550, 130), 3)
    #pygame.draw.line(win, (0, 0, 0), (250, 130), (250, 430), 3)
    #pygame.draw.line(win, (0, 0, 0), (250, 430), (550, 430), 3)
    #pygame.draw.line(win, (0, 0, 0), (550, 430), (550, 130), 3)

    pygame.draw.circle(win, (0, 0, 0),[400, 300], 7, 0)




    pygame.display.update()
pygame.quit()


