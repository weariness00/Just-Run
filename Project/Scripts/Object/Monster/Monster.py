from Scripts.FrameWork.Object import *

class Monster(Object):
    def __init__(self, target):
        super(Monster, self).__init__()

        self.__idle = dict()
        self._speed = None
        self._targetPlayer = target
        self.isMoveMent = True

        # Collider
        self.collider = Collide()
        self.collider.InitTransform(self.transform)
        self.collider.tag = "Monster"
        self.collider.object = self
        pass

    def __del__(self):
        super(Monster, self).__del__()
        pass

    def Update(self):
        self.MoveMent()
        pass

    def MoveMent(self):
        if self.isMoveMent is False:
            return

        realspeed = self._speed * self.time.OneFrameTime()
        self.transform.LooAtTarget(self._targetPlayer.transform, realspeed)
        pass