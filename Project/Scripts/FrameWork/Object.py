from Scripts.FrameWork.Collide import *
from Scripts.FrameWork.FrameTIme import *

#Draw에서 1번 Object를 호출 뒤 2번 Object를 호출하면 1번 Object의 값을 그대로 가져다 쓴다 -> 왜?
#Draw를 Render클래스를 만들어 추가 후 Camera나 기타 등등을 인스턴스 변수로 받는다.

class Object:
    Count = 0
    AllObject = []
    def __init__(self):
        self.transform = Transform()
        self.collider = None
        self.time = FrameTime()

        # Aniamtion 관련
        self._defaultName = None
        self._sprite_Name = 'Idle'
        self._ani_Frame = 0
        self._ani_Count = 0
        self.image = None
        self.image_type = None
        self.image_dir = 'None'
        self.image_radian = 0

        self.Color = numpy.array([1,1,1,1])

        self.isActive = True

        self.name = None
        self.ID = Object.Count
        Object.Count += 1
        Object.AllObject.append(self)
        pass

    def __del__(self):
        # self.transform.__del__()
        # self.collider.__del__()
        # del self.Color
        pass

    def Info(self):
        print(self.ID, " : ", self.name)
        pass

    # def Draw(self):
    #     if not self.isActive:
    #         return
    #
    #     pos = self.transform.Position - Camera.MainCamera.transform.Position
    #     scale = self.transform.Scale * numpy.array([self.image_type[2], self.image_type[3]])
    #     self.image.clip_draw(self.image_type[0],self.image_type[1], self.image_type[2], self.image_type[3], pos[0], pos[1],scale[0],scale[1])
    #     pass
    pass
