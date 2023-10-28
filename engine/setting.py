import json

class setting:

    def __init__(self, path_file=""):
        self.path_file = path_file
        self.data = {
            "window_width":720,
            "window_height":480,
            "FPS_target": 60,
            "Mute_music": False,
            "Mute_sfx": False,
            "difficult":{
                'easy':True,
                'normal':False,
                'hard':False
            }
        }

    def write_out(self, data):
        self.data=data
        with open(self.path_file, 'w') as setting_file:
            json.dump(self.data, setting_file)

    def read_in(self):
        try:
            with open(self.path_file) as setting_file:
                self.data = json.load(setting_file)
        except:
            print('No setting file created yet')
        return self.data