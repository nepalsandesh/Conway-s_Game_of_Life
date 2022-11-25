import numpy
import pygame
import random
# from numba import jit


class Grid:
    """Grid class"""
    # @jit    
    def __init__(self, width, height, scale, offset):
        
        self.columns = int(height//scale)
        self.rows = int(width//scale)
        self.scale = scale
        self.offset = offset
        self.size = (self.rows, self.columns)
        self.grid_array = numpy.ndarray(shape=(self.size)) 
    
    # @jit  
    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)
     
    # @jit           
    def Conway(self, off_color, on_color, surface, pause):
        for x in range(self.rows):
            for y in range(self.columns):
                x_pos = x * self.scale
                y_pos = y * self.scale
                if self.grid_array[x][y] == 1:
                    rect = pygame.Rect(x_pos, y_pos, self.scale-self.offset, self.scale-self.offset)
                    pygame.draw.rect(surface, on_color, rect)
                else:
                    rect = pygame.Rect(x_pos, y_pos, self.scale-self.offset, self.scale-self.offset)
                    pygame.draw.rect(surface, off_color, rect)
        
        next = numpy.ndarray(shape=(self.rows, self.columns))
        if pause == False:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid_array[x][y]
                    neighbours = self.get_neighbours(x, y)
                    if state == 0 and neighbours == 3:
                        next[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours >3):
                        next[x][y] = 0
                    else:
                        next[x][y] = state
            self.grid_array = next
                    
     
    # @jit(nopython=False)                        
    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]
        total -= self.grid_array[x][y]
        return total
    
    def handle_mouse(self, x, y):
        _x = x//self.scale
        _y = y//self.scale

        
        if self.grid_array[_x][_y] != None:
            self.grid_array[_x][_y] = 1
    