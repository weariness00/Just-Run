from Scripts.FrameWork.Transform import *

class Collide:
    AllCollider = []
    MainCamera = None
    def __init__(self):
        self.colliderBox = None
        self.colliderSize = None
        self.Pivot = numpy.array([0,0], dtype= float)
        self.rDistance = None # box의 x, y 반지름

        self.transform = None
        self.object = None

        self.isCollide = True # 현재 콜라이더 박스가 켜진 상태인지
        self.onColliderList = None
        self.isTrigger = False #이게 켜진 Objcet가 충돌하면 충돌한 거리만큼 뒤로 간다.
        self.isMouseCollide = False

        self.tag = None

        self.image = load_image('colliderBox.png')

        Collide.AllCollider.append(self)
        pass

    def __del__(self):
        # del self.colliderBox, self.colliderSize
        # del self.Piovt, self.rPos
        # del self.object
        # del self.image
        # del self
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
        self.rDistance = self.colliderSize/2
        pass

    def OnCollider(self): #모든 Collider를 검사후 충돌 된 것들을 반환
        self.onColliderList = []

        if self.isCollide is False or self.object.isActive is False:
            return self.onColliderList

        cameraPos = - Collide.MainCamera.transform.Position + Instance.windowSize//2
        this_Pos = self.Pivot * self.transform.Scale + self.transform.Position + cameraPos
        thisRDis = self.rDistance * self.transform.Scale

        for collider in Collide.AllCollider:
            if collider.object.ID == self.object.ID or collider.object.isActive is False or collider.isCollide is False:
                continue
            # 두 개의 콜라이더의 피봇끼리의 거리를 구한 후  (선분)AB
            # 각 콜라이더의 피봇이 다른 콜라이더의 피봇을 향해 백터 방향으로 증가하다가 자신의 박스 경계선을 만나는 곳과의 거리 계산후 r(A) r(B)
            # (선분)AB <= r(A) + r(B) 일씨 충돌로 간주
            other_Pos = collider.Pivot * collider.transform.Scale + collider.transform.Position + cameraPos
            otherRDis = collider.rDistance * collider.transform.Scale

            xAB_Distance = Instance.Distance(this_Pos, [other_Pos[0], this_Pos[1]])
            yAB_Distance = Instance.Distance(this_Pos, [this_Pos[0], other_Pos[1]])
            ABDis = numpy.array([xAB_Distance, yAB_Distance], dtype=float)

            if (ABDis > otherRDis + thisRDis).any():
                continue
            self.onColliderList.append(collider)
            pass
        return self.onColliderList

    #물리 충돌
    def OnTrigger(self):
        if self.isCollide is False or self.object.isActive is False:
            return

        cameraPos = - Collide.MainCamera.transform.Position + Instance.windowSize//2
        this_Pos = self.Pivot * self.transform.Scale + self.transform.Position + cameraPos
        thisRDis = self.rDistance * self.transform.Scale

        for collider in self.onColliderList:
            if collider.object.ID == self.object.ID or collider.object.isActive is False or collider.isCollide is False:
                continue
            # 두 개의 콜라이더의 피봇끼리의 거리를 구한 후  (선분)AB
            # 각 콜라이더의 피봇이 다른 콜라이더의 피봇을 향해 백터 방향으로 증가하다가 자신의 박스 경계선을 만나는 곳과의 거리 계산후 r(A) r(B)
            # (선분)AB <= r(A) + r(B) 일씨 충돌로 간주
            other_Pos = collider.Pivot * collider.transform.Scale + collider.transform.Position + cameraPos
            otherRDis = collider.rDistance * collider.transform.Scale

            xAB_Distance = Instance.Distance(this_Pos, [other_Pos[0], this_Pos[1]])
            yAB_Distance = Instance.Distance(this_Pos, [this_Pos[0], other_Pos[1]])
            ABDis = numpy.array([xAB_Distance, yAB_Distance], dtype=float)

            if (ABDis > otherRDis + thisRDis).any():
                continue

            if self.isTrigger:  # 물리 충돌
                # 박스기리 충돌된 공간만큼 뒤로 감
                # TODO Triger는 모든 Object의 OnCollider가 끝난뒤 실행
                gapDistance = (thisRDis + otherRDis) - ABDis
                moveDir = self.transform.direction

                if gapDistance[0] < gapDistance[1]:
                    if moveDir[0] > 0:
                        self.transform.Position[0] -= gapDistance[0] + 1
                    elif moveDir[0] < 0:
                        self.transform.Position[0] += gapDistance[0] + 1
                if gapDistance[0] > gapDistance[1]:
                    if moveDir[1] > 0:
                        self.transform.Position[1] -= gapDistance[1] + 1
                    elif moveDir[1] < 0:
                        self.transform.Position[1] += gapDistance[1] + 1
                pass
            pass

        pass

    @staticmethod
    def AllBoxDraw():
        cameraPos = Instance.windowSize // 2 - Collide.MainCamera.transform.Position
        for collider in Collide.AllCollider:
            if collider.colliderBox is None or collider.object.isActive is False or collider.isCollide is False:
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
