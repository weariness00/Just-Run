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

    def RemoveLay(self):
        Lay.AllLay.remove(self)
        del self
        pass

    @staticmethod
    def RemoveAll():
        for lay in Lay.AllLay:
            lay.RemoveLay()
        pass
    @staticmethod
    def DrawLayCast():
        for lay in Lay.AllLay:
            if not lay.isActive:
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
        self.cameraType = 'Object'
        self.colliderList = []
        pass

    def __del__(self):
        super(CircleLay, self).__del__()
        pass

    def OnLayCast(self):
        self.colliderList.clear()

        cameraPos = -Collide.MainCamera.transform.Position + Instance.windowSize // 2
        this_Pos = self.transform.Position + cameraPos

        for collider in Collide.AllCollider:
            if not collider.isCollide or not collider.object.isActive:
                continue

            other_Pos = collider.transform.Position + cameraPos

            dis = Instance.Distance(this_Pos, other_Pos)
            if dis <= self.distance:
                self.colliderList.append(collider)

            pass
        return self.colliderList
        pass

    def Draw(self):
        cameraPos = -Collide.MainCamera.transform.Position + Instance.windowSize // 2
        CircleLay.image.clip_draw(*[0,0,229,220],
                                  *(self.transform.Position + cameraPos),
                                  self.distance * 2,self.distance * 2)
        pass
    pass