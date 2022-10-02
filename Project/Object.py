from Afx import *


class Object:
    Count = 0

    def __init__(self, Color=[1, 1, 1, 1], transform=Transform(), collider=Collide()):
        self.transform = transform
        self.collider = collider
        self.collider.InitTransform(self.transform)

        self.Color = Color

        self.isActive = True

        self.ID = Object.Count + 1
        Object.Count += 1
        pass

    def __del__(self):
        pass

    pass

