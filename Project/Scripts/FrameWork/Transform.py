from Scripts.Afx import *


class Transform:
    def __init__(self, Position=[0, 0], Rotation=0, Scale=[1, 1]):
        self.Position = numpy.array(Position)
        self.Rotation = Rotation
        self.Scale = numpy.array(Scale)
        pass

    def __del__(self):
        pass

    def LookAt(self, speed):
        self.Position += speed * numpy.array([math.cos(self.Rotation * math.pi / 180), math.sin(self.Rotation * math.pi / 180)])
        pass

    def LooAtTarget(self, target, speed):
        if self.Position[0] == target.Position[0] and self.Position[1] == target.Position[1]:
            return

        dir = target.Position - self.Position
        dir = dir/numpy.linalg.norm(dir)
        self.Position = self.Position + speed * dir
        pass

    def Info(self):
        print("Position : ", self.Position)
        print("Rotation : ", self.Rotation)
        print("Scale    : ", self.Scale)
        pass

    pass
