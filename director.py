class director:
    def __init__(self, first_scene):
        self.current_scene = first_scene
    def change_to_scene(self, next_scene):
        self.current_scene = next_scene
    def get_current_scene(self):
        return self.current_scene