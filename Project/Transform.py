from Afx import *


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

    def Info(self):
        print(self.Position, " = Position")
        print(self.Rotation, " = Rotation")
        print(self.Scale, " = Scale")
        pass

    pass
