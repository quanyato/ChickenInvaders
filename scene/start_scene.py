import engine.button as button

class start:
    def __init__(self, display, director):
        self.display = display
        self.director = director
        self.start_button = button.button(self.display, 'assets/img-gui/btn-green.png')
        self.start_button.set_position(300, 300)
        self.start_button.set_hover_image('assets/img-gui/btn-yellow.png')
    def run(self):
        self.display.fill('red')
        if self.start_button.draw_and_get_pressed()==True:
            self.director.change_to_scene('level')