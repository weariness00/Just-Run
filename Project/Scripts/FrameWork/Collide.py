from Scripts.FrameWork.Transform import *

# OnCollider 부분에서 왜 에러인지 모르겠음

class Collide:
    def __init__(self, transform = None):
        self.colliderBox = numpy.zeros((2, 2), dtype=int)

        self.transform = transform

        self.isCollide = False
        self.isMouseCollide = False
        pass

    def __del__(self):
        pass

    def InitTransform(self, transform):
        self.transform = transform
        pass

    def SetCollideBox(self, box):
        findDot = box
        for i in range(0,2):
            if findDot[0][0] < box[i][0]:
                findDot[0][0] = box[i][0]
            if findDot[0][1] > box[i][1]:
                findDot[0][1] = box[i][1]

            if findDot[1][0] > box[i][0]:
                findDot[1][0] = box[i][0]
            if findDot[1][1] < box[i][1]:
                findDot[1][1] = box[i][1]
            pass
        self.colliderBox = findDot * self.transform.Scale + self.transform.Position
        pass

    def OnCollider(self, other):
        self.isCollide = False

        this_Box = self.colliderBox * self.transform.Scale + self.transform.Position
        other_Box = other.colliderBox * other.transform.Scale + other.transform.Position

        if this_Box[0][0] <= other_Box[0][0] <= this_Box[1][0] or this_Box[0][0] <= other_Box[1][0] <= this_Box[1][0]:
            if other_Box[0][1] >= this_Box[0][1] >= other_Box[1][1] or this_Box[0][1] >= other_Box[0][1] >= this_Box[1][1]:
                self.isCollide = True
        elif this_Box[0][1] >= other_Box[0][1] >= this_Box[1][1] or this_Box[0][1] >= other_Box[1][1] >= this_Box[1][1]:
            #if this_Box[0][0] >= other_Box[0][0] => other_Box[1][0] or this_Box[0][0] <= other_Box[0][0] <= this_Box[1][0]:
                self.isCollide = True

        return self.isCollide

    def Info(self):
        print("\nCollider\n",self.colliderBox)
        print(self.isCollide, " = isCollide")
        print(self.isMouseCollide, " = isMouseCollide")
        pass

    pass
