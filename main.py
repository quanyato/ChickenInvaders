import pygame, sys
import engine.director as director
import scene.start_scene as start_scene
import scene.level as level

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((960, 540))

game_director = director.director('start')

scenes = {
    'start':start_scene.start(screen, game_director),
    'level':level.level(screen, game_director)
}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    scenes[game_director.get_current_scene()].run()
    
    pygame.display.flip()
    clock.tick(60)