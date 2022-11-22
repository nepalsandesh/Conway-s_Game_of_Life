import pygame
import grid


width = 1920
height = 1080
resolution = (width, height)


pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
FPS = 20

# colors
black = (0,0,0)
white = (255, 255, 255)


Grid = grid.Grid(width, height, 5, 1)
Grid.random2d_array()

pause = False

while True:
    clock.tick(FPS)
    pygame.display.set_caption("{}".format(clock.get_fps()))
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