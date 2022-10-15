from Scripts.FrameWork.Object import *

class Monster(Object):
    def __init__(self, target):
        super(Monster, self).__init__()

        self.__idle = dict()
        self._speed = None
        self._targetPlayer = target
        pass

    def __del__(self):
        pass

    def Update(self):
        self.MoveMent()
        pass

    def MoveMent(self):
        realspeed = self._speed * Instance.FrameTime()
        self.transform.LooAtTarget(self._targetPlayer.transform, realspeed)
        pass

    def OnCollide(self):
        pass
    pass