import pygame

pygame.init()

# draw window
win = pygame.display.set_mode((602,722))#402
# setting the fps or init the fps.
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

matrix_copy=[[0,0,0,0,0,0,0,0,0,0], #[[1,1,1]
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



# each square is 40X40 pixel
obj1=[[0,0,1],
     [0,0,1],
     [1,1,1]]

obj2=[[1,1,1],
     [1,1,1],
     [1,1,1]]

# experimental

#obj=[[1,0,0],
#     [1,1,0],
 #    [0,1,0]]

#obj_right=[[0,1,0],
 #    [0,1,1],
  #   [0,0,1]]

#obj_trans=[[0,0,0],
 #           [0,1,1],
  #          [1,1,0]]
# ///////\\\\\\\\\


obj_color=[['#fee440','#9b5de5','#00f5d4'],
     [0,'#84a59d',0],
     ['#fee440','#9b5de5','#00f5d4']]


# to draw grid function
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
# ////////\\\\\\\\

def square(f,g,matrix):
    obj = [[0,0],
        [1, 1],
           [1, 1]]


    for i in range(3):
        for j in range(2):
            if obj[i][j] == 1:
                matrix[i + f][g + j] = 1
           # g = 7

    return '#f72585'



def half_n_object(f,g,if_trans,matrix,matrix_copy):

    obj = [[1, 0, 0],
           [1, 1, 0],
           [0, 1, 0]]

    obj_right = [[0, 1, 0],
                 [0, 1, 1],
                 [0, 0, 1]]

    obj_trans = [[0, 0, 0],
                 [0, 1, 1],
                 [1, 1, 0]]

    if f>=15 :
        if not if_trans:
            if g > 7:

                for i in range(3):
                    for j in range(3):
                        if obj_right[i][j] == 1:
                            matrix_copy[i + f][7 + j] = 1
            # g = 7
            else:
                for i in range(3):
                    for j in range(3):
                        if obj[i][j] == 1:
                            matrix_copy[i + f][g + j] = 1
        else:
            if g > 7:
                g = 7
            for i in range(3):
                for j in range(3):
                    if obj_trans[i][j] == 1:
                        matrix_copy[i + f][g + j] = 1

    if not if_trans:
        if g>7:

            for i in range(3):
                for j in range(3):
                    if obj_right[i][j] == 1:
                        matrix[i + f][7 + j] = 1
           # g = 7
        else:
            for i in range(3):
                for j in range(3):
                    if obj[i][j]==1:
                        matrix[i+f][g+j]=1
    else:
        if g>7:

            g=7
        for i in range(3):
            for j in range(3):
                if obj_trans[i][j]==1:
                    matrix[i+f][g+j]=1


    return ['#e63946',g]



def straight_line(f,g,if_trans,matrix):
    if g>8:
        g=9
    obj = [1,1,1]


    obj_trans = [[0, 0, 0],
                 [0, 0, 0],
                 [1, 1, 1]]
    if not if_trans:

        for i in range(3):

            if obj[i]==1:
                matrix[i+f][g]=1
        print(g)
    else:
        if g>7:

            g=7
        for i in range(3):
            for j in range(3):
                if obj_trans[i][j]==1:
                    matrix[i+f][g+j]=1
    return ['#06d6a0',g]


def stool_object(f,g,toggel,matrix ):
    if g > 7:
        g = 8


    obj = [[0, 0, 0],
           [1, 1, 1],
           [0, 1, 0]]


    obj_trans_1 = [[0, 1, 0],
                 [0, 1, 1],
                 [0, 1, 0]]

    obj_trans_2 = [[0, 1, 0],
                   [1, 1, 1],
                   [0, 0, 0]]

    obj_trans_3 = [[0, 1, 0],
                 [1, 1, 0],
                 [0, 1, 0]]
    if toggel==1:
        if g>7:
            g=7
        for i in range(3):
            for j in range(3):
                if obj[i][j]==1:
                    matrix[i+f][g+j]=1
    elif toggel==2:
        if g>7:
            g=7
        for i in range(3):
            for j in range(3):
                if obj_trans_1[i][j]==1:
                    matrix[i+f][g+j]=1

    elif toggel==3:
        if g>7:
            g=7
        for i in range(3):
            for j in range(3):
                if obj_trans_2[i][j]==1:
                    matrix[i+f][g+j]=1
    elif toggel==4:

        for i in range(3):
            for j in range(3):
                if obj_trans_3[i][j]==1:
                    matrix[i+f][g+j]=1
    return ['#390099',g]





run=True

y=0

t=0

# experimental
right_extreme=False
f=0
g=0
delay=0
if_trans=False
toggel=1
# //////\\\\\\\

while run:
    # experimental
    if f>=16:
        f=0
    # //////\\\\\\\

    # experimental
    if delay>20:
        delay=0
    # //////\\\\\\\

    clock.tick(30)



   # win.fill((34, 177, 76))
    win.fill("#edf2f4")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        # experimental

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if_trans=not if_trans
                toggel+=1
                if toggel>4:
                    toggel=1
            if event.key == pygame.K_RIGHT:
                # large matrix x_axis control
                g+=1

            if event.key == pygame.K_LEFT:
                g -= 1
                if g<=0:
                    g=0
        # //////\\\\\\\

    # experimental
    color=half_n_object(f,g,if_trans,matrix,matrix_copy)
    #color = straight_line(f, g, if_trans, matrix)
    #color=stool_object(f,g,toggel,matrix)
    g=color[1]

    #color=square(f,g,matrix)



    # grid function
    draw_grid()
    #/////\\\\\
    grid_y=0
    for i in range(18):

        grid_x=0
        for j in range(10):

            # experimental
            if matrix[i][j]==1 :
                matrix[i][j]=0
                pygame.draw.rect(win, color[0], (grid_x+3, grid_y+3, 35, 35), 0)
            # //////\\\\\\\
            # gap between each grid (vertical)
            grid_x+=40
        # gap between each grid (horizontal)
        grid_y+=40

    # experimental
    if delay==20 :
        f+=1
    delay+=1
    # //////\\\\\\\
    # matrix_copy displayer
    yy=0
    for i in range(18):

        xx=0
        for j in range(10):
            if matrix_copy[i][j]==1 :
                pygame.draw.rect(win, color[0], (xx+3, yy+3, 35, 35), 0)
            # //////\\\\\\\
            # gap between each grid (vertical)
            xx+=40
        # gap between each grid (horizontal)
        yy+=40

    pygame.display.update()
pygame.quit()

