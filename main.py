import pygame
import grid


width = 1920
height = 1080
resolution = (width, height)


pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
FPS = 30

# colors
black = (0,0,0)
white = (255, 255, 255)

scale = 30 # scale-offset would be the actual width or height of each cell
offset = 2  # for spacing between cells


Grid = grid.Grid(width, height, scale, offset)
Grid.random2d_array()

pause = False

while True:
    clock.tick(FPS)
    # pygame.display.set_caption("{}".format(clock.get_fps()))
    pygame.display.set_caption("Conway's Game of Life")
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
                
    Grid.Conway(white, black, screen, pause)
    
    if pygame.mouse.get_pressed()[0]:
        x_pos, y_pos = pygame.mouse.get_pos()
        Grid.handle_mouse(x_pos, y_pos)
    
    pygame.display.flip()