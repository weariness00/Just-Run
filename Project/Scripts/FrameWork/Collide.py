from Scripts.FrameWork.Transform import *

class Collide:
    AllCollider = []
    MainCamera = None
    def __init__(self):
        self.colliderBox = None

        self.transform = None
        self.object = None

        self.Pivot = numpy.array([0, 0])

        self.isCollide = False
        self.isMouseCollide = False

        self.tag = None

        Collide.AllCollider.append(self)
        pass

    def __del__(self):
        pass

    def InitTransform(self, transform):
        self.transform = transform
        pass

    def SetCollideBox(self, box):
        findDot = numpy.array(box)
        for i in range(0,2):
            if findDot[0, 0] > box[i, 0]:
                findDot[0, 0] = box[i, 0]
            if findDot[0, 1] > box[i, 0]:
                findDot[0, 1] = box[i, 1]

            if findDot[1, 0] < box[i, 0]:
                findDot[1, 0] = box[i, 0]
            if findDot[1, 1] < box[i, 1]:
                findDot[1, 1] = box[i, 1]
            pass

        collidePivot = numpy.array([self.object.image_type[2], self.object.image_type[3]])//2       #현재 이미지의 Pivot을 구한뒤
        self.Pivot = numpy.array([findDot[1]//2 - collidePivot]) # 제일 큰점을 2로 나누고 중점을 빼준뒤
        self.colliderBox = numpy.array([[self.Pivot - collidePivot],[self.Pivot + collidePivot]]) * self.transform.Scale # 충돌박스를 중점을 기준으로 정해진 크기만큼 배정후 크기를 곱한다.
        pass

    def OnCollider(self): #모든 Collider를 검사후 충돌 된 것들을 반환
        collides = []
        if (self.colliderBox == None).all():
            return collides

        for collider in Collide.AllCollider:
            if collider == self or (self.colliderBox is None) or (collider.colliderBox is None):
                continue
            #두 개의 콜라이더의 피봇끼리의 거리를 구한 후  (선분)AB
            #각 콜라이더의 피봇이 다른 콜라이더의 피봇을 향해 백터 방향으로 증가하다가 자신의 박스 경계선을 만나는 곳과의 거리 계산후 r(A) r(B)
            # (선분)AB <= r(A) + r(B) 일씨 충돌로 간주

            pass

        return collides

        # this_Box = (self.colliderBox + self.Pivot) * self.transform.Scale + self.transform.Position- Collide.MainCamera.transform.Position + Instance.windowSize//2
        # for collider in Collide.AllCollider:
        #     if collider == self or (self.colliderBox is None) or (collider.colliderBox is None):
        #         continue
        #
        #     other_Box = (collider.colliderBox + collider.Pivot) * collider.transform.Scale + collider.transform.Position - Collide.MainCamera.transform.Position + Instance.windowSize//2
        #     if this_Box[0][0] <= other_Box[0][0] <= this_Box[1][0] or this_Box[0][0] <= other_Box[1][0] <= this_Box[1][0]:
        #         if (other_Box[0][1] <= this_Box[1][1] <= other_Box[1][1]) or \
        #                 (this_Box[0][1] <= other_Box[1][1] <= this_Box[1][1]):
        #             collides.append(collider)
        #     elif this_Box[0][1] <= other_Box[0][1] <= this_Box[1][1] or this_Box[0][1] <= other_Box[1][1] <= this_Box[1][1]:
        #         if (other_Box[1][0] >= this_Box[0][0] >= other_Box[0][0]) or \
        #                 (this_Box[0][0] <= other_Box[0][0] <= this_Box[1][0]):
        #             collides.append(collider)
        #     pass
        # return collides

    def Info(self):
        print("\nCollider\n", self.colliderBox)
        print(self.tag)
        print(self.isCollide, " = isCollide")
        print(self.isMouseCollide, " = isMouseCollide")
        pass

    pass
