from Scripts.FrameWork.Object import *

class Monster(Object):
    def __init__(self, target):
        super(Monster, self).__init__()

        self.__idle = dict()
        self._speed = None
        self._targetPlayer = target
        self.isMoveMent = True
        self.isDeath = False

        # 생명주기
        self.lifeTime = 10
        self.lifeStart = 0

        # Collider
        self.collider = Collide()
        self.collider.InitTransform(self.transform)
        self.collider.tag = "Monster"
        self.collider.object = self

        # Animaiton
        self.mainAnimation = None
        self.workingAni = None
        self.attackAni = None
        self.deathAni = None

        # Timer
        self.deathStart = time.time()
        pass

    def __del__(self):
        super(Monster, self).__del__()
        pass

    def MoveMent(self):
        if self.isMoveMent is False:
            return

        realspeed = self._speed * self.time.OneFrameTime()
        self.transform.LooAtTarget(self._targetPlayer.transform, realspeed)
        pass

    def OnAnimation(self):
        self.mainAnimation.OnAnimation(self.time.OneFrameTime())

        self.image = self.mainAnimation.image
        self.image_type = self.mainAnimation.image_type

        if self.transform.direction[0] > 0:
            self.image_dir = 'None'
        elif self.transform.direction[0] < 0:
            self.image_dir = 'hd'

        if self.isDeath is True and time.time() - self.deathStart > 1:
            self.isActive = False
            self.isDeath = False
            self.collider.isCollide = True
            self.isMoveMent = True
            self.mainAnimation = self.workingAni
        pass

    def CheckLifeTime(self):  # 생명주기 체크
        if self.collider.isCollide is False:
            return

        lTime = time.time() - self.lifeStart
        if lTime > self.lifeTime:
            self.collider.isCollide = False
            self.isMoveMent = False
            self.isDeath = True
            self.mainAnimation = self.deathAni
            self.deathStart = time.time()
            pass
        pass
    pass
