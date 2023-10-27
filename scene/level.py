import engine.button as button

class level:
    def __init__(self, display, director):
        self.display = display
        self.director = director
        self.back_button = button.button(self.display, 'assets/img-gui/btn-green.png')
        self.back_button.set_position(200, 200)
        self.back_button.set_hover_image('assets/img-gui/btn-yellow.png')
    def run(self):
        self.display.fill('blue')
        if self.back_button.draw_and_get_pressed()==True:
            self.director.change_to_scene('start')