from Scripts.Afx import *

class Animation:
    def __init__(self):
        self.frame = 0
        self.__count = 0

        self.countSpeed = 0

        # image
        self.image = None
        self.image_type = None

        pass

    def __del__(self):
        pass

    def OnAnimation(self, frameTime):
        self.image_type[0] = (int(self.__count) % self.frame) * self.image_type[2]
        self.__count += frameTime * self.countSpeed
        # self.__count -= int(self.__count) % self.frame
        pass

    pass