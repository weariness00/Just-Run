from Scripts.Object.Monster.Monster import *
from Scripts.FrameWork.Effect import Effect

class Limbo(Monster):
    workingImage = load_image('image/Monster/Limbo Monster/Working.png')
    deathImage = load_image('image/Monster/Limbo Monster/Death.png')

    effectImage = load_image('Effect/Sparkling/fireball-small-wind.png')

    def __init__(self):
        # Objcet
        super(Limbo, self).__init__()
        self.name = 'Limbo'
        self.speed = 150

        self.hitVelum = 100

        # Transform
        self.transform.Scale = self.transform.Scale * 0.2

        # Collide
        self.collider.Pivot += [0, -30]
        self.collider.SetCollideBox(numpy.array([[0,0],[230,200]]))
        self.collider.isTrigger = True

        # Animation
        frame = 2
        image_type = [0, 0, 305, 280]
        self.workingAni.image = Limbo.workingImage
        self.workingAni.image_type = image_type
        self.workingAni.frame = frame
        self.workingAni.countSpeed = 2.25

        self.deathAni.image = Limbo.deathImage
        self.deathAni.image_type = image_type
        self.deathAni.frame = frame
        self.deathAni.countSpeed = 4

        self.mainAnimation = self.workingAni

        # Effect
        self.effect = Effect()
        self.effect.image = Limbo.effectImage
        self.effect.image_type = [0,0,2048//8,1792//7]
        self.effect.frame_X, self.effect.frame_Y = 8, 6
        self.effect.countSpeed = 100
        self.effect.isOneCycle = True
        pass

    def __del__(self):
        super(Limbo, self).__del__()
        pass

    def Enable(self):
        self.mainAnimation = self.workingAni
        self.lifeTime = random.randint(7, 12 + 1)
        self.lifeStart = time.time()
        pass

    def Disable(self):
        super(Limbo, self).Disable()

        pass

    def Update(self):
        super(Limbo, self).MoveMent()
        super(Limbo, self).CheckLifeTime()
        super(Limbo, self).OnAnimation()
        pass

    def OnCollide(self):
        if self.collider.isCollide is False:
            return

        self.collider.isTrigger = True
        onColliderList = self.collider.OnCollider()

        for collider in onColliderList:
            super(Limbo, self).OnCollide(collider)
            if collider.tag == "Player":
                self.effect.OnEffect(self.transform)
                self.effect.transform.Position[1] += 30
            pass
        pass
    pass
    def Copy(self):
        return Limbo()

    pass