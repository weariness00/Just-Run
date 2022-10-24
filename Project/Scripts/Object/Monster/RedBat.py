from Scripts.Object.Monster.Monster import *
from Scripts.FrameWork.Animation import *


class RedBat(Monster):
    def __init__(self, target):
        # Objcet
        super(RedBat, self).__init__(target)
        self.name = 'RedBat'
        self.isActive = False
        self._speed = 100
        self._targetPlayer = target

        # Transform
        self.transform.Scale = self.transform.Scale * 0.15

        # Collide
        self.collider.SetCollideBox(numpy.array([[0,0],[230,200]]))
        self.collider.isTrigger = True

        # Animation
        frame = 8
        image_type = [0, 0, 534, 419]
        countSpeed = 3
        self.workingAni = Animation()
        self.workingAni.image = load_image('image/Monster/RedBat Monster/Working.png')
        self.workingAni.image_type = image_type
        self.workingAni.frame = frame
        self.workingAni.countSpeed = countSpeed

        self.attackAni = Animation()
        self.attackAni.image = load_image('image/Monster/RedBat Monster/Attack.png')
        self.attackAni.image_type = image_type
        self.attackAni.frame = frame
        self.attackAni.countSpeed = countSpeed

        self.deathAni = Animation()
        self.deathAni.image = load_image('image/Monster/RedBat Monster/Death.png')
        self.deathAni.image_type = image_type
        self.deathAni.frame = frame
        self.deathAni.countSpeed = countSpeed

        self.mainAnimation = self.workingAni

        # Timer
        pass

    def __del__(self):
        super(RedBat, self).__del__()
        pass

    def Update(self):
        if self.isActive is False:
            return

        super(RedBat, self).MoveMent()
        super(RedBat, self).CheckLifeTime()
        super(RedBat, self).OnAnimation()
        self.time.start = time.time()
        pass

    def OnCollide(self):
        if self.collider.isCollide is False:
            return

        self.collider.isTrigger = True
        onColliderList = self.collider.OnCollider()

        for collider in onColliderList:
            if collider.tag == "Player":
                self.collider.isCollide = False
                self.isMoveMent = False
                self.mainAnimation = self.deathAni
                self.deathStart = time.time()
            if collider.tag == 'Tile':
                self.collider.isTrigger = False

            pass
        pass
    pass

    def Copy(self):
        return RedBat(self._targetPlayer)

    pass