from Scripts.FrameWork.Transform import *

class Collide:
    AllCollider = []
    AllColliderX = None
    AllColliderY = None
    MainCamera = None

    image = load_image('colliderBox.png')
    def __init__(self):
        self.colliderBox = None
        self.colliderSize = None
        self.Pivot = numpy.array([0,0], dtype= float)
        self.rDistance = None # box의 x, y 반지름

        self.transform = None
        self.object = None

        self.isCollide = True # 현재 콜라이더 박스가 켜진 상태인지

        self.onColliderList = []
        self.index = [-1, -1]

        self.isTrigger = False #이게 켜진 Objcet가 충돌하면 충돌한 거리만큼 뒤로 간다.
        self.isMouseCollide = False

        self.tag = None

        self.image = Collide.image

        Collide.AllCollider.append(self)
        pass

    def __del__(self):
        del self
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

    def OnCollider(self):
        self.onColliderList.clear()

        if self.isCollide is False or self.object.isActive is False:
            return self.onColliderList

        # n * n 크기만큼만 Collider 검사
        collides = []
        for i in range(1, 4 + 1):
            collides.append(Collide.AllColliderX[self.index[0] - i])
            collides.append(Collide.AllColliderY[self.index[1] - i])
            collides.append(Collide.AllColliderX[(self.index[0] + i) % len(Collide.AllColliderX)])
            collides.append(Collide.AllColliderY[(self.index[1] + i) % len(Collide.AllColliderY)])
            pass

        if len(collides) == 0:
            return self.onColliderList

        # 중복되는것들 제거
        for i in range(0, len(collides) - 1):
            for n in range(i + 1, len(collides)):
                if collides[i].object.ID == collides[n].object.ID:
                    collides.remove(collides[n])
                    break

        cameraPos = -Collide.MainCamera.transform.Position + Instance.windowSize//2
        thisBox = self.colliderBox * self.transform.Scale + self.transform.Position + cameraPos

        for collider in collides:
            if collider.object.isActive is False or collider.isCollide is False:
                continue

            otherBox = collider.colliderBox * collider.transform.Scale + collider.transform.Position + cameraPos

            if thisBox[0][0] > otherBox[1][0]: continue
            if thisBox[1][0] < otherBox[0][0]: continue
            if thisBox[1][1] < otherBox[0][1]: continue
            if thisBox[0][1] > otherBox[1][1]: continue

            self.onColliderList.append(collider)
            pass
        del collides
        return self.onColliderList
        pass

    def OnTrigger(self):
        if self.isCollide is False or self.object.isActive is False:
            return

        cameraPos = - Collide.MainCamera.transform.Position + Instance.windowSize//2
        this_Pos = self.Pivot * self.transform.Scale + self.transform.Position + cameraPos
        thisRDis = self.rDistance * self.transform.Scale

        for collider in self.onColliderList:
            if not collider.object.isActive or not collider.isCollide:
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

    @staticmethod
    def SortAllCollide():
        del Collide.AllColliderX
        del Collide.AllColliderY
        # Collider 의 Pivot을 기준으로 X, Y로 정렬
        cameraPos = - Collide.MainCamera.transform.Position + Instance.windowSize // 2

        # 비활성화 콜라이더들 제외
        AllCollider = []
        for collider in Collide.AllCollider:
            if collider.isCollide is False or collider.object.isActive is False:
                continue
            AllCollider.append(collider)
            pass

        Collide.AllColliderX = sorted(AllCollider, key=lambda c: c.Pivot[0] * c.transform.Scale[0] + c.transform.Position[0] + cameraPos[0])
        for i in range(len(Collide.AllColliderX)):
            Collide.AllColliderX[i].index[0] = i
        Collide.AllColliderY = sorted(AllCollider, key=lambda c: c.Pivot[1] * c.transform.Scale[1] + c.transform.Position[1] + cameraPos[1])
        for i in range(len(Collide.AllColliderY)):
            Collide.AllColliderY[i].index[1] = i

        del AllCollider
        pass
    def Info(self):
        print("\nCollider\n", self.colliderBox)
        print(self.tag)
        print(self.isCollide, " = isCollide")
        print(self.isMouseCollide, " = isMouseCollide")
        pass

    pass
