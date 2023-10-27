import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((960, 540))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()
    clock.tick(60)