import numpy

from Scripts.Object.Monster.Monster import *

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
        self.collider.Pivot = numpy.array([0, -30], dtype= float)
        self.collider.SetCollideBox(numpy.array([[0,0],[230,200]]))
        self.collider.isTrigger = True

        # Animaiton
        self._defaultName = 'image/Monster/Limbo Monster/'
        self.ChangeSprite('Working')

        # Timer
        self.start = time.time()

        pass

    def __del__(self):
        super(Limbo, self).__del__()
        pass

    def Update(self):
        super(Limbo, self).Update()
        self.Animation()
        self.time.start = time.time()
        pass

    def OnCollide(self):
        if self.isActive is False:
            return

        self.collider.OnCollider()

        for collider in self.collider.onColliderList:
            if collider.tag == "Player":
                self.collider.isCollide = False
                self.ChangeSprite('Death')

            pass
        pass
    pass

    def Animation(self):
        self.image_type[0] = (int(self._ani_Count) % self._ani_Frame) * self.image_type[2]
        self._ani_Count += self.time.OneFrameTime() * 2.5

        if self.transform.direction[0] > 0:
            self.image_dir = 'h'
        elif self.transform.direction[0] < 0:
            self.image_dir = 'None'

        if self._sprite_Name == 'Death' and time.time() - self.start > 1:
            self.isActive = False
            self.collider.isCollide = True
            self.isMoveMent = True
            self.ChangeSprite('Working')
        pass

    def ChangeSprite(self, state):
        self._sprite_Name = state
        if state == "Idle":
            self.image_type = [0, 0, 312, 269]
            self._ani_Frame = 2
        elif state == "Working":
            self.image_type = [0, 0, 305, 280]
            self._ani_Frame = 2
            pass
        elif state == 'Death':
            self.image_type = [0, 0, 305, 280]
            self._ani_Frame = 2
            self.start = time.time()
            self.isMoveMent = False
            pass

        ani_Name = Instance.SetPngName(self._defaultName, self._sprite_Name)
        self.image = load_image(ani_Name)

    def Copy(self):
        return Limbo(self._targetPlayer)

    pass