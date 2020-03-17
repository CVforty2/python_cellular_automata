import pygame
import numpy as np
import sys
import time
import grid
import gui



def main():
    width = 7
    height = 7
    margin = 1

    window_x = 800
    window_y = 800

    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)


    pygame.display.init()
    screen = pygame.display.set_mode((window_y, window_x))
    pygame.display.set_caption("Cellular Automata")


    ca_grid = grid.Grid(100, 100)
    ca_grid.grid[5][5] = 1
    ca_grid.grid[5][6] = 1
    ca_grid.grid[5][7] = 1
    ca_grid.grid[4][7] = 1
    ca_grid.grid[3][6] = 1

    drawing_type = 0
    begin = False
    quit = False
    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                # Debug prints
                print("Click ", pos, "Grid coordinates: ", row, column)
                if ca_grid.grid[row][column] == 0:
                    if drawing_type == 0:
                        ca_grid.grid[row][column] = 1
                    elif drawing_type == 1:
                        ca_grid.spawn_glider(row, column)
                    elif drawing_type == 2:
                        ca_grid.spawn_gun(row, column)

                elif ca_grid.grid[row][column] == 1:
                    ca_grid.grid[row][column] = 0
            elif event.type == pygame.KEYDOWN:
                # Start when key 's' is pressed.
                if event.key == pygame.K_s:
                    begin = True
                elif event.key == pygame.K_0:
                    drawing_type = 0
                elif event.key == pygame.K_1:
                    drawing_type = 1
                elif event.key == pygame.K_2:
                    drawing_type = 2



        pos = pygame.mouse.get_pos()



        screen.fill(BLACK)


        for column in range(ca_grid.height):
            for row in range(ca_grid.row):
                if ca_grid.grid[row][column] == 1:
                    color = WHITE
                else:
                    color = BLACK
                pygame.draw.rect(screen, color, [margin + (margin + width) * column, margin + (margin + height) * row, width, height])

        if begin:
            ca_grid.rules()

        pygame.time.Clock().tick(120)
        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    main()
