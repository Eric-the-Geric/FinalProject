
import numpy as np
import random
import pygame
import rules

width = 1920
height = 1080
size = (width, height)
scale = 30
offset = 1
dead_colour = (40, 40, 40)
alive_colour = (88, 101, 242)
black = (0, 0, 0)
fps = 60

def main():
    pygame.init()
    pygame.display.set_caption("John Conway's Game Of Life")
    surface = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Grid = rules.Grid(width, height, scale, offset)
    Grid.blank_array()
    pause = True
    run = True
    random_colour_toggle = True
    while run:
        surface.fill(black)
        Grid.rules(dead_colour=dead_colour, alive_colour=alive_colour, surface=surface, pause=pause, random_colour_toggle=random_colour_toggle)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    pause = not pause
            elif pygame.mouse.get_pressed()[0]:
                mouse_X, mouse_Y = pygame.mouse.get_pos()
                Grid.mouse_click_left(mouse_X, mouse_Y)
            elif pygame.mouse.get_pressed()[2]:
                mouse_X, mouse_Y = pygame.mouse.get_pos()
                Grid.mouse_click_right(mouse_X, mouse_Y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                random_colour_toggle = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_t:
                random_colour_toggle = True
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                Grid.blank_array()
                pause = True
                random_colour_toggle = True
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                Grid.random_array()
                pause = False
        
        pygame.display.update()
        clock.tick(fps)



if __name__ == '__main__':
    main()




