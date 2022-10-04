from Afx import *

#Draw에서 1번 Object를 호출 뒤 2번 Object를 호출하면 1번 Object의 값을 그대로 가져다 쓴다 -> 왜?

class Object:
    Count = 0

    def __init__(self, Color=[1, 1, 1, 1], transform=Transform(), collider=Collide(), name = None):
        self.transform = transform
        self.collider = collider
        self.collider.InitTransform(self.transform)

        self.image = None
        self.image_type = None
        self.Color = Color

        self.isActive = True

        self.name = name
        self.ID = Object.Count
        Object.Count += 1
        pass

    def __del__(self):
        pass

    def Info(self):
        print(self.ID, " : ", self.name)
        pass

    def Draw(self):
        if not self.isActive:
            return

        #Camera.MainCamera.transform.Info()

        pos = self.transform.Position #- Camera.MainCamera.transform.Position
        scale = self.transform.Scale * numpy.array([self.image_type[2], self.image_type[3]])
        self.image.clip_draw(self.image_type[0],self.image_type[1], self.image_type[2], self.image_type[3], pos[0], pos[1],scale[0],scale[1])
        pass
    pass
