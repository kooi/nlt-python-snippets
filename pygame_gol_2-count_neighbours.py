"""
 A python implementation of Conway's Game of Life in Python/Pygame
"""
import pygame
import math

PALETTE = [
            (255, 255, 255),
            (  0,   0,   0),
            (  0, 255,   0),
            (255,   0,   0)
          ]

PIXEL_SIZE = 20
PIXEL_MARGIN = 5

GRID_SIZE_X = 12
GRID_SIZE_Y = 8

petridish = [[0 for x in range(GRID_SIZE_X)] for y in range(GRID_SIZE_Y)]
# petri_old[10][1] = 1 # y,x


def update_petri(petri):
    # petridish_new = [y[:] for y in petri_old]
    for j in range(GRID_SIZE_Y):
        for i in range(GRID_SIZE_X):
            count_neighbours(j,i, petri)
        print()


def count_neighbours(x, y, petri):
    sum = 0
    for j in [-1, 0, 1]:
        for i in [-1, 0, 1]:
            sum += petri[(y+j)%GRID_SIZE_Y][(x+i)%GRID_SIZE_X]
    print(sum, end='')
    return sum

pygame.init()

WINDOW_SIZE = (255, 255)
screen = pygame.display.set_mode([
    GRID_SIZE_X*(PIXEL_SIZE+PIXEL_MARGIN)+PIXEL_MARGIN,
    GRID_SIZE_Y*(PIXEL_SIZE+PIXEL_MARGIN)+PIXEL_MARGIN,
    ])
pygame.display.set_caption("Game of Life")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # we hadden hier ook een break kunnen gebruiken
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            col = pos[0] / (PIXEL_SIZE+PIXEL_MARGIN)
            row = pos[1] / (PIXEL_SIZE+PIXEL_MARGIN)
            if event.button == 1:
                petridish[math.floor(row)][math.floor(col)] = 1
            elif event.button == 3:
                petridish[math.floor(row)][math.floor(col)] = 0
            print("mouseclick(", pos, ") -> (", row,",", col, ")")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            update_petri(petridish)
 
    screen.fill( PALETTE[0] )
 
    for j in range(GRID_SIZE_Y):
        for i in range(GRID_SIZE_X):
            pygame.draw.rect(
                screen, PALETTE[ petridish[j][i] ],
                [(PIXEL_SIZE+PIXEL_MARGIN) * i + PIXEL_MARGIN,
                 (PIXEL_SIZE+PIXEL_MARGIN) * j + PIXEL_MARGIN,
                 PIXEL_SIZE, PIXEL_SIZE])
 
    clock.tick(60) # max 60 fps
    pygame.display.flip()
 
pygame.quit()