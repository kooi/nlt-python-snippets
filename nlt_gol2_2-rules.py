import pygame
import random

# grid = [
#          [0, 1, 0, 1, 0, 1],
#          [1, 1, 1, 1, 1, 1],
#        ]
# cell = grid[y vanaf boven][x vanaf links]
# cell = grid[0][1]
# print(grid[0][1])

PALETTE = [
            (255, 255, 255), # dood
            (  0,   0,   0), # levend
            (255, 255,   0), # 2
            (  0, 255, 255), # 3
            (255,   0, 255), # 4
            (128, 128,   0), # 5
            (  0, 128, 128), # 6
            (128,   0, 128), # 7
            (128, 128, 128), # 8
            (255, 255, 255), # achtergrond
          ]

PIXEL_SIZE = 30
PIXEL_MARGIN = 5
GRID_SIZE_X = 20
GRID_SIZE_Y = 10

#petridish = [[random.randint(0,1) for x in range(GRID_SIZE_X)]
#                  for y in range(GRID_SIZE_Y)]

petridish = [[0 for x in range(GRID_SIZE_X)] for y in range(GRID_SIZE_Y)]

def count_neighbours(x, y, p):
    sum = 0
    sum = sum + p[(y-1)%GRID_SIZE_Y][(x-1)%GRID_SIZE_X]
    sum = sum + p[(y-1)%GRID_SIZE_Y][(x  )%GRID_SIZE_X]
    sum = sum + p[(y-1)%GRID_SIZE_Y][(x+1)%GRID_SIZE_X]
    sum = sum + p[(y  )%GRID_SIZE_Y][(x+1)%GRID_SIZE_X]
    sum = sum + p[(y+1)%GRID_SIZE_Y][(x+1)%GRID_SIZE_X]
    sum = sum + p[(y+1)%GRID_SIZE_Y][(x  )%GRID_SIZE_X]
    sum = sum + p[(y+1)%GRID_SIZE_Y][(x-1)%GRID_SIZE_X]
    sum = sum + p[(y  )%GRID_SIZE_Y][(x-1)%GRID_SIZE_X]
    return sum

def life_or_death(state, neighbours):
    """
    1. Any live cell with two or three live neighbors survives.
    2. Any dead cell with three live neighbors becomes a live cell.
    3. All other live cells die in the next generation.
       Similarly, all other dead cells stay dead.
    """
    if state == 1:
        if neighbours == 2 or neighbours == 3:
            return 1
        else:
            return 0
    else: # state = 0
        if neighbours == 3:
            return 1
        else:
            return 0

def update_petridish(old):
    new = [[0 for x in range(GRID_SIZE_X)] for y in range(GRID_SIZE_Y)]
    for j in range(GRID_SIZE_Y):
        for i in range(GRID_SIZE_X):
            new[j][i] = life_or_death( old[j][i], count_neighbours(i, j, old) )
    return new




pygame.init()
screen = pygame.display.set_mode([
    GRID_SIZE_X*(PIXEL_SIZE+PIXEL_MARGIN)+PIXEL_MARGIN,
    GRID_SIZE_Y*(PIXEL_SIZE+PIXEL_MARGIN)+PIXEL_MARGIN,
    ])
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // (PIXEL_SIZE+PIXEL_MARGIN)
            row = pos[1] // (PIXEL_SIZE+PIXEL_MARGIN)
            if event.button == 1:
                petridish[row][col] = 1
            elif event.button == 3:
                petridish[row][col] = 0
            print("mouseclick(", pos, ") -> (", row,",", col, ")")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            petridish = update_petridish(petridish)
            
    # teken petrischaal naar scherm
    screen.fill( PALETTE[9] )
    for j in range(GRID_SIZE_Y):
        for i in range(GRID_SIZE_X):
            pygame.draw.rect( screen, PALETTE[petridish[j][i]],
                [(PIXEL_SIZE + PIXEL_MARGIN)*i + PIXEL_MARGIN,
                 (PIXEL_SIZE + PIXEL_MARGIN)*j + PIXEL_MARGIN,
                 PIXEL_SIZE, PIXEL_SIZE] )
    
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
