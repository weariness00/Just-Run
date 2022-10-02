from Afx import *


class Collide:
    def __init__(self):
        self.colliderBox = numpy.zeros((2, 2), dtype=int)

        self.transform = None

        self.isCollide = False
        self.isMouseCollide = False
        pass

    def __del__(self):
        pass

    def InitTransform(self, transform):
        self.transform = transform
        pass

    def SetCollideBox(self, box):
        self.colliderBox = box * self.transform.Scale + self.transform.Position
        pass

    def Show(self):
        print("\nCollider\n",self.colliderBox)
        print(self.isCollide, " = isCollide")
        print(self.isMouseCollide, " = isMouseCollide")
        pass

    pass
