from Scripts.Object.Monster.Monster import *

class Limbo(Monster):
    workingImage = load_image('image/Monster/Limbo Monster/Working.png')
    deathImage = load_image('image/Monster/Limbo Monster/Death.png')

    def __init__(self):
        # Objcet
        super(Limbo, self).__init__()
        self.name = 'Limbo'
        self.isActive = False
        self._speed = 150

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
        pass

    def __del__(self):
        super(Limbo, self).__del__()
        pass

    def Update(self):
        if self.isActive is False:
            return

        super(Limbo, self).MoveMent()
        super(Limbo, self).CheckLifeTime()
        super(Limbo, self).OnAnimation()
        pass

    def OnCollide(self):
        if self.collider.isCollide is False:
            return

        onColliderList = self.collider.OnCollider()

        for collider in onColliderList:
            if collider.tag == "Player":
                self.collider.isCollide = False
                self.isMoveMent = False
                self.isDeath = True
                self.mainAnimation = self.deathAni
                self.deathStart = time.time()
            if collider.tag == 'Monster Attack':
                self.collider.isTrigger = False
            pass
        pass
    pass
    def Copy(self):
        return Limbo()

    pass