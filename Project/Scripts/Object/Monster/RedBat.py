from Scripts.Object.Monster.Monster import *
from Scripts.Object.Monster.AttackBall import *
from Scripts.FrameWork.Animation import *


class RedBat(Monster):
    workImage = load_image('image/Monster/RedBat Monster/Working.png')
    attackImage = load_image('image/Monster/RedBat Monster/Attack.png')
    deathImage = load_image('image/Monster/RedBat Monster/Death.png')
    def __init__(self, target):
        # Objcet
        super(RedBat, self).__init__(target)
        self.name = 'RedBat'
        self.isActive = False
        self._speed = 100
        self._targetPlayer = target
        self.attackRange = 500
        self.attackObjectCount = 1

        # Transform
        self.transform.Scale = self.transform.Scale * 0.15

        # Collide
        self.collider.SetCollideBox(numpy.array([[0,0],[230,200]]))
        self.collider.isTrigger = True

        # Animation
        frame = 8
        image_type = [0, 0, 534, 419]
        countSpeed = 10
        self.workingAni = Animation()
        self.workingAni.image = RedBat.workImage
        self.workingAni.image_type = image_type
        self.workingAni.frame = frame
        self.workingAni.countSpeed = countSpeed

        self.attackAni = Animation()
        self.attackAni.image = RedBat.attackImage
        self.attackAni.image_type = image_type
        self.attackAni.frame = frame
        self.attackAni.countSpeed = 5

        self.deathAni = Animation()
        self.deathAni.image = RedBat.deathImage
        self.deathAni.image_type = image_type
        self.deathAni.frame = frame
        self.deathAni.countSpeed = 8

        self.mainAnimation = self.workingAni

        # Attack Object
        for i in range(self.attackObjectCount):
            self.attackObject += [AttackBall(target)]

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
        self.Attack()
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
                self.isDeath = True
                self.mainAnimation = self.deathAni
                self.deathStart = time.time()
            if collider.tag == 'Tile':
                self.collider.isTrigger = False
            if collider.tag == 'Monster Attack':
                self.collider.isTrigger = False

            pass
        pass
    pass

    def Attack(self):
        if self.mainAnimation is not self.attackAni:
            return

        if self.attackAni.count < 7:
            return

        self.attackAni.count = 0
        self.mainAnimation = self.workingAni
        self.isMoveMent = True

        for i in range(self.attackObjectCount):
            if self.attackObject[i].isActive is True:
                continue

            self.attackObject[i].transform.Position = numpy.array(self.transform.Position)

            self.attackObject[i].collider.isCollide = True
            self.attackObject[i].isActive = True
            self.attackObject[i].isMoveMent = True
            self.attackObject[i].lifeStart = time.time()
            self.attackObject[i].time.start = time.time()
            break

        pass

    def Copy(self):
        return RedBat(self._targetPlayer)

    pass