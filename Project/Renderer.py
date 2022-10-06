from Camera import *

# 클래스의 멤버 변수가 파일 분할시 적용이 안되는 이유 찾아봅시다
class Renderer:
    MainRender = None

    def __init__(self):
        self.P = None
        self.RendererObjectList = []
        pass

    def Update(self):
        #self.Player
        for obj in self.RendererObjectList:
            if not obj.isActive:
                continue

            pos = obj.transform.Position #- Camera.MainCamera.transform.Position
            scale = obj.transform.Scale * numpy.array([obj.image_type[2], obj.image_type[3]])
            obj.image.clip_draw(obj.image_type[0], obj.image_type[1], obj.image_type[2], obj.image_type[3], pos[0], pos[1], scale[0], scale[1])
            pass

        obj = self.P
        obj.transform.Info()
        pos = obj.transform.Position  # - Camera.MainCamera.transform.Position
        scale = obj.transform.Scale * numpy.array([obj.image_type[2], obj.image_type[3]])
        obj.image.clip_draw(obj.image_type[0], obj.image_type[1], obj.image_type[2], obj.image_type[3],
                            pos[0], pos[1], scale[0], scale[1])
        pass

    pass

Renderer.MainRender = Renderer()

def AddRenderObject(obj):
    Renderer.MainRender.RendererObjectList += [obj]
    pass