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
            (255,   0,   0), # dood
            (  0,   0,   0), # levend
            (255, 255, 255), # achtergrond
          ]

PIXEL_SIZE = 30
PIXEL_MARGIN = 5
GRID_SIZE_X = 20
GRID_SIZE_Y = 10

petridish = [[random.randint(0,1) for x in range(GRID_SIZE_X)]
                  for y in range(GRID_SIZE_Y)]

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
            petridish[row][col] = 1
            print("mouseclick(", pos, ") -> (", row,",", col, ")")

    screen.fill( PALETTE[2] )
    
    for j in range(GRID_SIZE_Y):
        for i in range(GRID_SIZE_X):
            pygame.draw.rect( screen, PALETTE[petridish[j][i]],
                [(PIXEL_SIZE + PIXEL_MARGIN)*i + PIXEL_MARGIN,
                 (PIXEL_SIZE + PIXEL_MARGIN)*j + PIXEL_MARGIN,
                 PIXEL_SIZE, PIXEL_SIZE] )
    
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
