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
dark_blue = (10, 10, 60)

scale = 20 # scale-offset would be the actual width/height of each cell
offset = 1 # for spacing between cells


Grid = grid.Grid(width, height, scale, offset)


pause = False
frame_count = 0

while True:
    clock.tick(FPS)
    # clock.tick()
    
    pygame.display.set_caption("{}th-Frame, FPS-{}".format(frame_count, clock.get_fps()))
    # pygame.display.set_caption("Conway's Game of Life")
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
                
    Grid.Conway(white, dark_blue, screen, pause)
    
    if pygame.mouse.get_pressed()[0]:
        x_pos, y_pos = pygame.mouse.get_pos()
        Grid.handle_mouse(x_pos, y_pos)
        
    # frame_count += 1
    # filename = "captures/%04d.png" % ( frame_count ) # name with four decimals
    # pygame.image.save( screen, filename )
    
    pygame.display.flip()