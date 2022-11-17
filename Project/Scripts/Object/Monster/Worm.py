from Scripts.Object.Monster.Monster import *


class Worm(Monster):
    spawnImage = load_image('image/Monster/UnderWorm/Spawn.png')
    workImage = load_image('image/Monster/UnderWorm/Working.png')
    deathImage = load_image('image/Monster/UnderWorm/Death.png')
    def __init__(self):
        # Objcet
        super(Worm, self).__init__()
        self.name = 'RedBat'
        self.isActive = False
        self._speed = 70

        # Transform
        self.transform.Scale *= 0.2

        # Collide
        self.collider.SetCollideBox(numpy.array([[0,0],[300,500]]))

        # Animation
        image_type = [0, 0, 459, 507]
        self.workingAni.image = Worm.workImage
        self.workingAni.image_type = image_type
        self.workingAni.frame = 7
        self.workingAni.countSpeed = 10

        self.spawnAni = Animation()
        self.spawnAni.image = Worm.spawnImage
        self.spawnAni.image_type = image_type
        self.spawnAni.frame = 14
        self.spawnAni.countSpeed = 5

        self.deathAni.image = Worm.deathImage
        self.deathAni.image_type = image_type
        self.deathAni.frame = 14
        self.deathAni.countSpeed = 8

        self.mainAnimation = self.spawnAni
        pass

    def __del__(self):
        super(Worm, self).__del__()
        pass

    def Enable(self):
        self.mainAnimation = self.spawnAni
        self.lifeTime = random.randint(10, 15 + 1)
        self.lifeStart = time.time()
        pass

    def Disable(self):
        super(Worm, self).Disable()
        pass

    def Update(self):
        if self.mainAnimation == self.spawnAni:
            if self.mainAnimation.count >= self.mainAnimation.frame:
                self.mainAnimation = self.workingAni
            pass

        self.transform.LookAt(0)
        super(Worm, self).CheckLifeTime()
        super(Worm, self).OnAnimation()
        pass

    def OnCollide(self):
        if self.collider.isCollide is False:
            return

        onColliderList = self.collider.OnCollider()

        for collider in onColliderList:
            super(Worm, self).OnCollide(collider)
        pass
    pass


    def Copy(self):
        return Worm()

    pass