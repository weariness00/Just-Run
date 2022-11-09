from Scripts.FrameWork.Collide import *
from Scripts.FrameWork.FrameTime import *

#Draw에서 1번 Object를 호출 뒤 2번 Object를 호출하면 1번 Object의 값을 그대로 가져다 쓴다 -> 왜?
#Draw를 Render클래스를 만들어 추가 후 Camera나 기타 등등을 인스턴스 변수로 받는다.

class Object:
    image = load_image('image/Bin.png')
    Count = 0
    AllObject = []
    events = []  # Hadle_Event

    updateList = None
    def __init__(self):
        self.transform = Transform()
        self.collider = None

        # Aniamtion 관련
        self.image = Object.image
        self.image_type = [0, 0, 0, 0]
        self.image_dir = 'None'
        self.image_radian = 0

        self.isActive = True

        self.name = None
        self.ID = Object.Count
        Object.Count += 1
        Object.AllObject.append(self)
        Object.updateList += [self]
        pass

    def __del__(self):
        pass

    def Update(self):
        pass

    def OnCollide(self):
        pass

    def Info(self):
        print(self.ID, " : ", self.name)
        pass

    pass
