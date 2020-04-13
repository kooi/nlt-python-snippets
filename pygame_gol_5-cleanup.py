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

PIXEL_SIZE = 5
PIXEL_MARGIN = 1

GRID_SIZE_X = 120
GRID_SIZE_Y = 80

petridish = [[0 for x in range(GRID_SIZE_X)] for y in range(GRID_SIZE_Y)]

def life_or_death(state, neighbours):
    """
    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overpopulation.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """
    if state == 1:
        if neighbours < 2:
            return 0
        elif neighbours == 2 or neighbours == 3:
            return 1
        elif neighbours > 3:
            return 0
    elif state == 0:
        if neighbours == 3:
            return 1
    return 0


def count_neighbours(x, y, petri):
    sum = 0 - petri[y][x]
    for j in [-1, 0, 1]:
        for i in [-1, 0, 1]:
            sum += petri[(y+j)%GRID_SIZE_Y][(x+i)%GRID_SIZE_X]
    return sum


def update_petri(petri):
    new = [[0 for x in range(GRID_SIZE_X)] for y in range(GRID_SIZE_Y)]
    for j in range(GRID_SIZE_Y):
        for i in range(GRID_SIZE_X):
            new[j][i] = life_or_death(petri[j][i], count_neighbours(i,j, petri))
    return new


pygame.init()

WINDOW_SIZE = (255, 255)
screen = pygame.display.set_mode([
    GRID_SIZE_X*(PIXEL_SIZE+PIXEL_MARGIN)+PIXEL_MARGIN,
    GRID_SIZE_Y*(PIXEL_SIZE+PIXEL_MARGIN)+PIXEL_MARGIN,
    ])
pygame.display.set_caption("Game of Life")

done = False
autorun = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # we hadden hier ook een break kunnen gebruiken
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // (PIXEL_SIZE+PIXEL_MARGIN)
            row = pos[1] // (PIXEL_SIZE+PIXEL_MARGIN)
            if event.button == 1:
                petridish[row][col] = 1
            elif event.button == 3:
                petridish[row][col] = 0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            autorun = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            autorun = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            petridish = update_petri(petridish)

    if autorun == True:
        petridish = update_petri(petridish)
 
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