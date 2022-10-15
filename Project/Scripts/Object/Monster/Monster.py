from Scripts.FrameWork.Object import *

class Monster(Object):
    def __init__(self, target):
        super(Monster, self).__init__()
        self.image = load_image('image/Monster/Limbo Monster/transparent/idle/frame-1.png')
        self.image_type = [0,0,312,269]
        self.transform.Scale = self.transform.Scale * 0.3

        self.__speed = 300
        self.__idle = dict()
        self.__targetPlayer = target
        pass

    def __del__(self):
        pass

    def Update(self):
        self.MoveMent()
        pass

    def MoveMent(self):
        realspeed = self.__speed * Instance.FrameTime()
        self.transform.LooAtTarget(self.__targetPlayer.transform, realspeed)
        pass

    def OnCollide(self):
        pass
    pass