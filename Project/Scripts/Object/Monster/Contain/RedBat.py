from Scripts.Object.Monster.Contain.AttackBall import *
from Scripts.FrameWork.Effect import Effect


class RedBat(Monster):
    workImage = load_image('image/Monster/RedBat Monster/Working.png')
    attackImage = load_image('image/Monster/RedBat Monster/Attack.png')
    deathImage = load_image('image/Monster/RedBat Monster/Death.png')

    effectImage = load_image('Effect/Sparkling/explosion_pixelfied.png')

    HitSound = load_wav('Music/Monster/Hit/Flame.ogg')
    def __init__(self):
        # Objcet
        super(RedBat, self).__init__()
        self.name = 'RedBat'
        self.speed = 70
        self.attackRange = 500
        self.attackObjectCount = 2

        self.hitSound = RedBat.HitSound

        # Transform
        self.transform.Scale = self.transform.Scale * 0.15

        # Collide
        self.collider.SetCollideBox(numpy.array([[0,0],[230,200]]))
        self.collider.isTrigger = True

        # Animation
        frame = 8
        countSpeed = 10
        image_type = [0, 0, 534, 419]
        self.workingAni.image = RedBat.workImage
        self.workingAni.image_type = image_type
        self.workingAni.frame = frame
        self.workingAni.countSpeed = countSpeed

        self.attackAni.image = RedBat.attackImage
        self.attackAni.image_type = image_type
        self.attackAni.frame = frame
        self.attackAni.countSpeed = 5

        self.deathAni.image = RedBat.deathImage
        self.deathAni.image_type = image_type
        self.deathAni.frame = frame
        self.deathAni.countSpeed = 8

        self.mainAnimation = self.workingAni

        # Attack Object
        for i in range(self.attackObjectCount):
            self.attackObject += [AttackBall()]

        # Effect
        self.effect = Effect()
        self.effect.image = RedBat.effectImage
        self.effect.image_type = [0,0,128//4,128//4]
        self.effect.frame_X, self.effect.frame_Y = 4,4
        self.effect.countSpeed = 10
        self.effect.isOneCycle = True

        pass

    def __del__(self):
        super(RedBat, self).__del__()
        pass

    def Enable(self):
        self.mainAnimation = self.workingAni
        self.lifeTime = random.randint(7, 12 + 1)
        self.lifeStart = time.time()
        self.attackTimer = time.time()
        pass

    def Disable(self):
        super(RedBat, self).Disable()
        self.attackAni.count = 0
        pass

    def Update(self):
        super(RedBat, self).MoveMent()
        super(RedBat, self).CheckLifeTime()
        super(RedBat, self).OnAnimation()
        self.Attack()
        pass

    def OnCollide(self):
        if self.collider.isCollide is False:
            return

        self.collider.isTrigger = True
        onColliderList = self.collider.OnCollider()

        for collider in onColliderList:
            super(RedBat, self).OnCollide(collider)
            if collider.tag == "Player":
                self.deathStart = time.time()
                self.effect.OnEffect(self.transform)
            if collider.tag == 'Tile':
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
            self.attackObject[i].transform.Position = numpy.array(self.transform.Position)
            self.attackObject[i].SetActive(True)
            break

        pass

    def Copy(self):
        return RedBat()

    pass