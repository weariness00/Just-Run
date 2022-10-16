import numpy

from Scripts.Object.Monster.Monster import *

class Limbo(Monster):
    def __init__(self, target):
        # Objcet
        super(Limbo, self).__init__(target)
        self.name = 'Limbo'
        self.isActive = False

        # Transform
        self.transform.Scale = self.transform.Scale * 0.2

        # Collide
        self.collider.Pivot = numpy.array([0, -30], dtype= float)
        self.collider.SetCollideBox(numpy.array([[0,0],[230,200]]))
        self.collider.isTrigger = True

        # Animaiton
        self._defaultName = 'image/Monster/Limbo Monster/'
        self.ChangeSprite('Idle')

        self._speed = 100

        self._targetPlayer = target
        pass

    def __del__(self):
        super(Limbo, self).__del__()
        pass

    def Update(self):
        super(Limbo, self).Update()
        self.OnCollide()
        pass

    def ChangeSprite(self, state):
        if state == "Idle":
            self._sprite_Name = 'Idle'
            self.image_type = [0, 0, 312, 269]
            self._ani_Frame = 2
        elif state == "Working":
            pass

        ani_Name = Instance.SetPngName(self._defaultName, self._sprite_Name)
        self.image = load_image(ani_Name)

    def Copy(self):
        return Limbo(self._targetPlayer)

    pass