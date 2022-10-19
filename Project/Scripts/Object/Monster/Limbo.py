from Scripts.Object.Monster.Monster import *
from Scripts.FrameWork.Animation import *

class Limbo(Monster):
    def __init__(self, target):
        # Objcet
        super(Limbo, self).__init__(target)
        self.name = 'Limbo'
        self.isActive = False
        self._speed = 100
        self._targetPlayer = target

        # Transform
        self.transform.Scale = self.transform.Scale * 0.2

        # Collide
        self.collider.Pivot += [0, -30]
        self.collider.SetCollideBox(numpy.array([[0,0],[230,200]]))
        self.collider.isTrigger = True

        # Animation
        self.workingAni = Animation()
        self.workingAni.image = load_image('image/Monster/Limbo Monster/Working.png')
        self.workingAni.image_type = [0, 0, 305, 280]
        self.workingAni.frame = 2
        self.workingAni.countSpeed = 2.25

        self.deathAni = Animation()
        self.deathAni.image = load_image('image/Monster/Limbo Monster/Death.png')
        self.deathAni.image_type = [0, 0, 305, 280]
        self.deathAni.frame = 2
        self.deathAni.countSpeed = 4

        self.mainAnimation = self.workingAni

        # Timer
        self.deathStart = time.time()
        pass

    def __del__(self):
        super(Limbo, self).__del__()
        pass

    def Update(self):
        if self.isActive is False:
            return

        super(Limbo, self).MoveMent()
        self.CheckLifeTime()
        self.OnAnimation()
        self.time.start = time.time()
        pass

    def OnCollide(self):
        if self.collider.isCollide is False:
            return

        self.collider.OnCollider()

        for collider in self.collider.onColliderList:
            if collider.tag == "Player":
                self.collider.isCollide = False
                self.isMoveMent = False
                self.mainAnimation = self.deathAni
                self.deathStart = time.time()
            pass
        pass
    pass

    def OnAnimation(self):
        self.mainAnimation.OnAnimation(self.time.OneFrameTime())

        self.image = self.mainAnimation.image
        self.image_type = self.mainAnimation.image_type

        if self.transform.direction[0] > 0:
            self.image_dir = 'h'
        elif self.transform.direction[0] < 0:
            self.image_dir = 'None'

        if self.mainAnimation == self.deathAni and time.time() - self.deathStart > 1:
            self.isActive = False
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
            self.mainAnimation = self.deathAni
            self.deathStart = time.time()
            pass
        pass

    def Copy(self):
        return Limbo(self._targetPlayer)

    pass