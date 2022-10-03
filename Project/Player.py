from Afx import *

class Player(Object):
    def __init__(self):
        super(Player, self).__init__()
        self.image = load_image('image/player/Player.png')
        self.image_type = [0,0,46,70]
        self.idle = None
        pass

    pass