import pygame, sys
import engine.director as director
import scene.start_scene as start_scene
import scene.level as level
import engine.setting as setting

pygame.init()

setting_manager = setting.setting('setting_data.txt')
setting_data = setting_manager.read_in()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((setting_data['window_width'], setting_data['window_height']))

game_director = director.director('start')

scenes = {
    'start':start_scene.start(screen, game_director),
    'level':level.level(screen, game_director)
}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setting_manager.write_out(setting_data)
            pygame.quit()
            sys.exit()
            
    scenes[game_director.get_current_scene()].run()
    
    pygame.display.flip()
    clock.tick(setting_data["FPS_target"])