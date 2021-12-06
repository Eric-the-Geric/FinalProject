import pygame
import numpy as np
import random

class Grid:
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        self.rows = int(width/scale)
        self.columns = int(height/scale)
        self.offset = offset
        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=self.size)

    def random_array(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.grid_array[i][j] = random.randint(0, 1)

    def blank_array(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.grid_array[i][j] = 0


    def rules(self, dead_colour, alive_colour, surface, pause, random_colour_toggle):
        for i in range(self.rows):
            for j in range(self.columns):
                random_colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                i_pos = i * self.scale
                j_pos = j * self.scale
                
                if random_colour_toggle == False:
                    if self.grid_array[i][j] == 1:
                        pygame.draw.rect(surface, random_colour, [i_pos, j_pos, self.scale - self.offset, self.scale - self.offset])
                    else:
                        pygame.draw.rect(surface, dead_colour, [i_pos, j_pos, self.scale - self.offset, self.scale - self.offset])
                else:
                    if self.grid_array[i][j] == 1:
                        pygame.draw.rect(surface, alive_colour, [i_pos, j_pos, self.scale - self.offset, self.scale - self.offset])
                    else:
                        pygame.draw.rect(surface, dead_colour, [i_pos, j_pos, self.scale - self.offset, self.scale - self.offset])
        next = np.ndarray(shape=(self.size))
        if pause == False:
            for i in range(self.rows):
                for j in range(self.columns):
                    state = self.grid_array[i][j]
                    neighbors = self.get_neighbors(i, j)
                    if state == 0 and neighbors == 3:
                        next[i][j] = 1
                    elif state == 1 and (neighbors < 2 or neighbors > 3):
                        next[i][j] = 0
                    else:
                        next[i][j] = state
            self.grid_array = next

    def get_neighbors(self, i, j):
        total = 0
        for x in range (-1, 2):
            for y in range(-1, 2):
                x_edge = (i+x+self.rows)%self.rows
                y_edge = (j+y+self.columns)%self.columns
                total += self.grid_array[x_edge][y_edge]
        total -= self.grid_array[i][j]
        return total

    def mouse_click_left(self, x, y):
        m_x = x//self.scale
        m_y = y//self.scale
        if self.grid_array[m_x][m_y] == 0:
            self.grid_array[m_x][m_y] = 1
    
    def mouse_click_right(self, x, y):
        m_x = x//self.scale
        m_y = y//self.scale
        if self.grid_array[m_x][m_y] == 1:
            self.grid_array[m_x][m_y] = 0   


    







