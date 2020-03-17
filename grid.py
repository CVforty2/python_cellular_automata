import numpy as np
import pygame
import copy
import sys

CELL_ALIVE = 1
CELL_DEAD = 0
HEIGHT = 32
WIDTH = 32

np.set_printoptions(threshold=sys.maxsize)

class Grid:

    def __init__(self, row, height):
        # Plus 2 for row and height because outter ring
        self.grid = [[0 for i in range(0, row)] for j in range(0, height)]
        self.row = row
        self.height = height

    def get_neighbors(self, y, x):
        count = 0
        if y <= self.height - 2 and y >= 1 and x <= self.row - 2 and x >= 1:
            # Top Row
            if self.grid[y-1][x-1] == 1:
                count += 1
            if self.grid[y-1][x] == 1:
                count += 1
            if self.grid[y-1][x+1] == 1:
                count += 1

            # Middle Row
            if self.grid[y][x-1] == 1:
                count += 1
            if self.grid[y][x+1] == 1:
                count += 1

            # Bottom Row
            if self.grid[y+1][x-1] == 1:
                count += 1
            if self.grid[y+1][x] == 1:
                count += 1
            if self.grid[y+1][x+1] == 1:
                count += 1

        return count

    def rules(self):
        temp_grid = copy.deepcopy(self)
        for column in range(1, self.height):
            for row in range(1, self.row):
                neighbors = temp_grid.get_neighbors(column, row)

                # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                if neighbors < 2 and self.grid[column][row] == CELL_ALIVE:
                    self.grid[column][row] = CELL_DEAD

                # Any live cell with more than three live neighbours dies, as if by overpopulation.
                if neighbors > 3 and self.grid[column][row] == CELL_ALIVE:
                    self.grid[column][row] = CELL_DEAD

                # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                if (neighbors == 3 or neighbors == 2) and self.grid[column][row] == CELL_ALIVE:
                    self.grid[column][row] = CELL_ALIVE

                if neighbors == 3 and self.grid[column][row] == CELL_DEAD:
                    self.grid[column][row] = CELL_ALIVE


    def templates(self, file):
        pass
        #parse txt file into template

    def spawn_gun(self, y, x):
        # Left sqaure
        self.grid[y][x] = 1
        self.grid[y][x+1] = 1
        self.grid[y+1][x] = 1
        self.grid[y+1][x+1] = 1

        # C shape
        self.grid[y][x+10] = 1
        self.grid[y+1][x+10] = 1
        self.grid[y+2][x+10] = 1
        self.grid[y-1][x+11] = 1
        self.grid[y-2][x+12] = 1
        self.grid[y-2][x+13] = 1
        self.grid[y+3][x+11] = 1
        self.grid[y+4][x+12] = 1
        self.grid[y+4][x+13] = 1

        # dot
        self.grid[y+1][x+14] = 1

        # triangle right of dot
        self.grid[y][x+16] = 1
        self.grid[y+1][x+16] = 1
        self.grid[y+1][x+17] = 1
        self.grid[y+2][x+16] = 1
        self.grid[y-1][x+15] = 1
        self.grid[y+3][x+15] = 1

        # rectangle with winged bits
        self.grid[y][x+20] = 1
        self.grid[y-1][x+20] = 1
        self.grid[y-2][x+20] = 1
        self.grid[y][x+21] = 1
        self.grid[y-1][x+21] = 1
        self.grid[y-2][x+21] = 1
        self.grid[y-3][x+22] = 1
        self.grid[y+1][x+22] = 1

        # blocks right of prev
        self.grid[y-4][x+24] = 1
        self.grid[y-3][x+24] = 1
        self.grid[y+1][x+24] = 1
        self.grid[y+2][x+24] = 1

        # right most sqaure
        self.grid[y-1][x+34] = 1
        self.grid[y-2][x+34] = 1
        self.grid[y-1][x+35] = 1
        self.grid[y-2][x+35] = 1
















    def spawn_glider(self, y, x):
        self.grid[y][x] = 1
        self.grid[y][x+1] = 1
        self.grid[y][x+2] = 1
        self.grid[y-1][x+2] = 1
        self.grid[y-2][x+1] = 1





    def print_grid(self):
        for column in range(1, self.height-1):
            for row in range(1, self.row-1):
                print(self.grid[column][row], end="")
            print()


if __name__ == "__main__":
    test_grid = Grid(10, 5)
    test_grid.grid[0][0] = 1
    test_grid.grid[0][1] = 1
    test_grid.grid[0][2] = 0
    test_grid.grid[1][0] = 1
    test_grid.grid[1][1] = 1
    test_grid.grid[1][2] = 1
    test_grid.grid[2][0] = 1
    test_grid.grid[2][1] = 1
    test_grid.grid[2][2] = 1
    print(test_grid.get_neighbors(1, 1))
    print(np.matrix(test_grid.grid))
