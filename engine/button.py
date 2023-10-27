import pygame

class button:
    def __init__(self, display_surface, image_path='', scale=1):
        self.display_surface = display_surface
        self.image_path = image_path
        self.button_image = pygame.image.load(self.image_path)
        self.button_hover_image = pygame.image.load(self.image_path)
        self.width = self.button_image.get_width()
        self.height = self.button_image.get_height()
        self.button_image = pygame.transform.scale(self.button_image, (self.width*scale, self.height*scale))
        self.pos_x = 0
        self.pos_y = 0
        self.button_rect = self.button_image.get_rect()
        self.hover = False
        

    def draw_and_get_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            self.hover = True
            self.display_surface.blit(self.button_hover_image, [self.pos_x, self.pos_y])
            if pygame.mouse.get_pressed()[0]==1:
                return True
        else:
            self.display_surface.blit(self.button_image, [self.pos_x, self.pos_y])
            self.hover = False

        return False
        

    def set_position(self, pos_x=0, pos_y=0):
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.button_rect.update(self.pos_x, self.pos_y, self.width, self.height)

    def set_btn_image(self, image_path=''):
        self.image_path = image_path
        self.button_image = pygame.image.load(self.image_path)
        self.width = self.button_image.get_width()
        self.height = self.button_image.get_height()
        self.button_rect.update(self.pos_x, self.pos_y, self.width, self.height)
    
    def set_hover_image(self, image_path=''):
        self.button_hover_image = pygame.image.load(image_path)

    def is_hover(self):
        return self.hover