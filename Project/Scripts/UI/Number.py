from Scripts.FrameWork.Object import *

class Number(Object):
    yellow_image = load_image('image/Number/Yellow_Number.png')
    def __init__(self):
        super(Number, self).__init__()
        self.image = Number.yellow_image
        self.image_type = [0, 0, 120, 146]
        pass

    def __del__(self):
        super(Number, self).__del__()
        pass

    def ChangeNumber(self, number):
        self.image_type[0] = self.image_type[2] * number
        pass

    pass