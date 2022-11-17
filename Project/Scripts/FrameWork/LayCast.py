from Scripts.FrameWork.Object import *

class Lay(Object):
    AllLay = []

    def __init__(self):
        super(Lay, self).__init__()

        Lay.AllLay.append(self)
        pass

    def __del__(self):
        super(Lay, self).__del__()
        pass

    @staticmethod
    def DrawLayCast():
        for lay in Lay.AllLay:
            if lay.isActive is False:
                continue

            lay.Draw()
            pass
        pass
    pass

class CircleLay(Lay):
    image = load_image('Circle.png')
    def __init__(self, transform, distance):
        super(CircleLay, self).__init__()
        self.distance = distance

        self.transform = transform

        pass

    def __del__(self):
        super(CircleLay, self).__del__()
        pass

    def OnLayCast(self):
        colliderList = []

        cameraPos = - Collide.MainCamera.transform.Position + Instance.windowSize // 2
        this_Pos = self.transform.Position + cameraPos

        for collider in Collide.AllCollider:
            if collider.isCollide is False or collider.object.isActive is False:
                continue

            other_Pos = collider.transform.Position + cameraPos

            dis = Instance.Distance(this_Pos, other_Pos)
            if dis <= self.distance:
                colliderList.append(collider)

            pass
        return colliderList
        pass

    def Draw(self):
        cameraPos = - Collide.MainCamera.transform.Position + Instance.windowSize // 2

        CircleLay.image.clip_draw(*[0,0,229,220],
                                  *(self.transform.Position + cameraPos),
                                 *(self.transform.Scale * self.distance))
        pass
    pass