import numpy

from Scripts.Afx import *


class Transform:
    def __init__(self, Position=[0, 0], Rotation=0, Scale=[1, 1]):
        self.Position = numpy.array(Position, dtype=float)
        self.Rotation = Rotation
        self.Scale = numpy.array(Scale)

        self.movePos = None # 이동하기 전 position
        pass

    def __del__(self):
        # del self.Position
        # del self.Rotation
        # del self.Scale
        # del self.movePos
        # del self
        pass

    def LookAt(self, speed):
        movePos = speed * numpy.array([math.cos(self.Rotation * math.pi / 180), math.sin(self.Rotation * math.pi / 180)])
        self.movePos = movePos
        self.Position += movePos
        pass

    def LooAtTarget(self, target, speed):
        if self.Position[0] == target.Position[0] and self.Position[1] == target.Position[1]:
            return

        dir = target.Position - self.Position
        dir = dir/numpy.linalg.norm(dir)

        self.movePos = speed * dir
        self.Position = self.Position + speed * dir
        pass

    def Info(self):
        print("Position : ", self.Position)
        print("Rotation : ", self.Rotation)
        print("Scale    : ", self.Scale)
        pass

    pass
