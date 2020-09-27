import pygame

from stellarobject import Stellar

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
yellow = (255, 255, 0)

screen_size = screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pylarsystem")

clock = pygame.time.Clock()
fps_limit = 60

while True:
    clock.tick(fps_limit)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
    screen.fill(black)  
    pygame.draw.circle(screen, yellow, ((int)(screen_width / 2), (int)(screen_height / 2)), 10)
    pygame.display.flip()
