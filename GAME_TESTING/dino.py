import pygame

pygame.init()

x_window=800
y_window=600
win = pygame.display.set_mode((602,722))

clock = pygame.time.Clock()

matrix=[[0,0,0,0,0,0,0,0,0,0], #[[1,1,1]
        [0,0,0,0,0,0,0,0,0,0], #[1,1,1]
        [0,0,0,0,0,0,0,0,0,0], #[1,1,1]
        [0,0,0,0,0,0,0,0,0,0], #[1,1,1]
        [0,0,0,0,0,0,0,0,0,0], #[1,1,1]
        [0,0,0,0,0,0,0,0,0,0], #[1,1,1]
        [0,0,0,0,0,0,0,0,0,0], #[1,1,1]
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
        ]


def draw_grid():
    grid_y = 0
    for i in range(18):
        pygame.draw.rect(win, (0, 0, 0), (0,grid_y , 400, 2),0)
        # to draw vertical grids
        grid_x = 0
        for j in range(11):
            pygame.draw.rect(win, (0, 0, 0), (grid_x, 0, 2,720), 0)
            # gap between each grid (vertical)
            grid_x += 40
        # gap between each grid (horizontal)
        grid_y += 40

def stool(x,y,toggel):
    if toggel>4:
        toggel=1
    if toggel==1:
        cord=[[x,y],[x+40,y],[x+80,y],[x+40,y+40]]
        if y > 722 - 80:
            y = 0
    if toggel==2:
        cord = [[x+40, y], [x + 40, y+40], [x + 40, y+80], [x, y + 40]]
        if y > 722 - 120:
            y = 0
    if toggel == 3:
        cord = [[x , y], [x + 40, y ], [x + 80, y ], [x+40, y - 40]]
        if y > 722 - 40:
            y = 0
    if toggel == 4:
        cord = [[x, y], [x, y+40], [x, y+80], [x+40, y + 40]]
        if y > 722 - 120:
            y = 0

    for i in cord:
        pygame.draw.rect(win, "#2a9d8f", (i[0], i[1], 40, 40), 0)
    return [toggel,y]

def line(x,y,toggel):
    if toggel>2:
        toggel=1
    if toggel==1:
        cord=[[x,y],[x+40,y],[x+80,y],[x+120,y]]
        if y > 722 - 80:
            y = 0
    if toggel==2:
        cord = [[x, y], [x , y+40], [x , y+80], [x, y + 120]]
        if y > 722 - 160:
            y = 0

    for i in cord:
        pygame.draw.rect(win, "#2a9d8f", (i[0], i[1], 40, 40), 0)
    return [toggel,y]

def square(x,y,toggel):
    if toggel>1:
        toggel=1
    if y>722-80:
        y=0

    cord = [[x, y], [x + 40, y], [x , y+40], [x + 40, y+40]]
    for i in cord:
        pygame.draw.rect(win, "#2a9d8f", (i[0], i[1], 40, 40), 0)
    return [toggel,y]

def l_shape(x,y,toggel):
    if toggel>2:
        toggel=1
    if toggel==1:
        cord = [[x, y], [x+40 , y], [x+80, y], [x, y -40]]
        if y > 722 - 40:
            y = 0
    if toggel==2:
        cord = [[x, y], [x , y+40], [x, y + 80], [x + 40, y + 80]]
        if y > 722 - 120:
            y = 0
    for i in cord:
        pygame.draw.rect(win, "#dddf00", (i[0], i[1], 40, 40), 0)
    return [toggel,y]


x=0
y=0
toggel=1
run = True
delay=0
while run:
    clock.tick(30)


    if delay>20:
        delay=0

    win.fill("#edf2f4")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x+=40
            if event.key == pygame.K_LEFT:
                x -= 40
            if event.key==pygame.K_SPACE or event.key==pygame.K_DOWN:
                toggel+=1
    #info=stool(x,y,toggel)
    info=line(x,y,toggel)

    #info = square(x, y, toggel)
    #info = l_shape(x, y, toggel)


    toggel=info[0]
    y=info[1]
    if delay==20 :
        y+=40
    draw_grid()

    delay+=1
    #
    pygame.display.update()
pygame.quit()
