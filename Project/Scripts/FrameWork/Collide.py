import numpy

from Scripts.FrameWork.Transform import *

class Collide:
    AllCollider = []
    MainCamera = None
    def __init__(self):
        self.colliderBox = None
        self.colliderSize = None
        self.Pivot = numpy.array([0,0], dtype= float)
        self.rPos = None # box의 x, y 반지름

        self.transform = None
        self.object = None

        self.isTrigger = False #이게 켜진 Objcet가 충돌하면 충돌한 거리만큼 뒤로 간다.
        self.isCollide = False
        self.isMouseCollide = False

        self.tag = None

        self.image = load_image('colliderBox.png')

        Collide.AllCollider.append(self)
        pass

    def __del__(self):
        pass

    def InitTransform(self, transform):
        self.transform = transform
        pass

    def SetCollideBox(self, box):
        findDot = numpy.array(box)
        for i in range(0, 2):
            if findDot[0, 0] > box[i, 0]:
                findDot[0, 0] = box[i, 0]
            if findDot[0, 1] > box[i, 0]:
                findDot[0, 1] = box[i, 1]

            if findDot[1, 0] < box[i, 0]:
                findDot[1, 0] = box[i, 0]
            if findDot[1, 1] < box[i, 1]:
                findDot[1, 1] = box[i, 1]
            pass

        self.colliderBox = numpy.array([self.Pivot - findDot[1]//2, self.Pivot + findDot[1]//2]) # 충돌박스를 중점을 기준으로 정해진 크기만큼 배정
        self.colliderSize = self.colliderBox[1] - self.colliderBox[0]
        self.rPos = self.colliderSize/2
        pass

    def OnCollider(self): #모든 Collider를 검사후 충돌 된 것들을 반환
        collides = []
        if (self.colliderBox == None).all():
            return collides

        cameraPos = - Collide.MainCamera.transform.Position + Instance.windowSize//2
        this_Pos = self.Pivot * self.transform.Scale + self.transform.Position + cameraPos
        thisRPos = self.rPos * self.transform.Scale

        for collider in Collide.AllCollider:
            if collider == self or (self.colliderBox is None) or (collider.colliderBox is None) or collider.object.isActive is False:
                continue
            # 두 개의 콜라이더의 피봇끼리의 거리를 구한 후  (선분)AB
            # 각 콜라이더의 피봇이 다른 콜라이더의 피봇을 향해 백터 방향으로 증가하다가 자신의 박스 경계선을 만나는 곳과의 거리 계산후 r(A) r(B)
            # (선분)AB <= r(A) + r(B) 일씨 충돌로 간주
            other_Pos = collider.Pivot * collider.transform.Scale + collider.transform.Position + cameraPos
            otherRPos = collider.rPos * collider.transform.Scale

            xAB_Distance = Instance.Distance(this_Pos, [other_Pos[0], this_Pos[1]])
            yAB_Distance = Instance.Distance(this_Pos, [this_Pos[0], other_Pos[1]])

            if xAB_Distance <= otherRPos[0] + thisRPos[0] and yAB_Distance <= otherRPos[1] + thisRPos[1]:
                collides.append(collider)
                if self.isTrigger:
                    ABDis = numpy.array([xAB_Distance, yAB_Distance], dtype = float)
                    gapPos = self.rPos - ABDis

                    if gapPos[0] <= gapPos[1]:
                        self.transform.Position[0] -= self.transform.movePos[0]
                    if gapPos[0] >= gapPos[1]:
                        self.transform.Position[1] -= self.transform.movePos[1]
                    pass
            pass

        return collides

    @staticmethod
    def AllBoxDraw():
        cameraPos = Instance.windowSize // 2 - Collide.MainCamera.transform.Position
        for collider in Collide.AllCollider:
            if collider.colliderBox is None or collider.object.isActive is False:
                continue

            Pos = collider.Pivot * collider.transform.Scale + collider.transform.Position + cameraPos
            collider.image.clip_draw(0, 0, 100, 100, Pos[0], Pos[1],
                                     collider.colliderSize[0] * collider.transform.Scale[0], collider.colliderSize[1] * collider.transform.Scale[1])
        pass

    def Info(self):
        print("\nCollider\n", self.colliderBox)
        print(self.tag)
        print(self.isCollide, " = isCollide")
        print(self.isMouseCollide, " = isMouseCollide")
        pass

    pass
