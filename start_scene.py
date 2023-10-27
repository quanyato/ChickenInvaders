import pygame

class start:
    def __init__(self, display, director):
        self.display = display
        self.director = director
    def run(self):
        self.display.fill('red')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.director.change_to_scene('level')