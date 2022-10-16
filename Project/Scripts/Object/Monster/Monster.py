from Scripts.FrameWork.Object import *

class Monster(Object):
    def __init__(self, target):
        super(Monster, self).__init__()


        self.__idle = dict()
        self._speed = None
        self._targetPlayer = target

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
        realspeed = self._speed * self.time.OneFrameTime()
        self.transform.LooAtTarget(self._targetPlayer.transform, realspeed)

        self.time.start = time.time()
        pass

    def OnCollide(self):
        if self.isActive is False:
            return

        collides = self.collider.OnCollider()

        for collider in collides:
            if collider.tag == "Player":
                collider.object.life -= 1
                self.isActive = False

            pass
        pass
    pass