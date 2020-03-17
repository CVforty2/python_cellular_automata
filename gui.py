import grid
import pygame

class Gui:
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, row, height, color, margin):
        self.grid_obj = grid.Grid(row, height)
        self.color = color
        self.margin = margin
        self.draw_grid()

    def draw_grid(self):
        for column in range(self.grid_obj.height):
            for row in range(self.grid_obj.row):
                if self.grid_obj.grid[row][column] == 1:
                    RED = (255, 0, 0)
                    color = RED
                else:
                    WHITE = (255, 255, 255)
                    color = WHITE
                pygame.draw.rect(screen, color, [self.margin + (self.margin + width) * column, self.margin + (self.margin + height) * row, width, height])
