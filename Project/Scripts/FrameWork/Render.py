from Scripts.FrameWork.Camera import *
from Scripts.FrameWork.Text import *

# 클래스의 멤버 변수가 파일 분할시 적용이 안되는 이유 찾아봅시다
class Render:
    def __init__(self):
        self.RendererObjectList = []
        pass

    def __del__(self):
        self.Clear()
        pass

    def Draw(self):
        for obj in self.RendererObjectList:
            if not obj.isActive:
                continue

            pos = obj.transform.Position - Camera.MainCamera.transform.Position + Instance.windowSize//2
            scale = obj.transform.Scale * numpy.array([obj.image_type[2], obj.image_type[3]])
            obj.image.clip_composite_draw(*obj.image_type,
                                obj.image_radian, obj.image_dir,
                                *pos, *scale)
            pass
        pass

    def UIDraw(self):
        for obj in self.RendererObjectList:
            if not obj.isActive:
                continue

            pos = obj.transform.Position
            scale = obj.transform.Scale * numpy.array([obj.image_type[2], obj.image_type[3]])
            obj.image.clip_composite_draw(*obj.image_type,
                                obj.image_radian, obj.image_dir,
                                *pos, *scale)
            pass
        pass

    def TextDraw(self):
        for text in self.RendererObjectList:
            text.font.draw(*text.transform.Position,
                           text.text,
                           text.color)
        pass

    def AddObject(self, obj):
        if type(obj) == list: self.RendererObjectList += obj
        else: self.RendererObjectList.append(obj)
        pass

    def RemoveObject(self, obj):
        if obj in self.RendererObjectList:
            self.RendererObjectList.remove(obj)
            del obj

        pass

    def Clear(self):
        for obj in self.RendererObjectList:
            del obj
        del self.RendererObjectList

    pass