from Scripts.FrameWork.Camera import *
from Scripts.UI.Text import *

# 클래스의 멤버 변수가 파일 분할시 적용이 안되는 이유 찾아봅시다
class Render:
    def __init__(self):
        self.name = "Render"
        self.RendererObjectList = []
        self.maxDeath = 0
        pass

    def __del__(self):
        self.Clear()
        pass

    def Draw(self):
        for layer in self.RendererObjectList:
            for obj in layer:
                if not obj.isActive or not obj.isDraw:
                    continue

                pos = obj.transform.Position - Camera.MainCamera.transform.Position + Instance.windowSize // 2
                scale = obj.transform.Scale * numpy.array([obj.image_type[2], obj.image_type[3]])
                obj.image.clip_composite_draw(*obj.image_type,
                                              obj.image_radian, obj.image_dir,
                                              *pos, *scale)
                pass
            pass
        pass

    def UIDraw(self):
        for layer in self.RendererObjectList:
            for ui in layer:
                if not ui.isActive or not ui.isDraw:
                    continue
                pos = ui.transform.Position
                scale = ui.transform.Scale * numpy.array([ui.image_type[2], ui.image_type[3]])
                ui.image.clip_composite_draw(*ui.image_type,
                                             ui.image_radian, ui.image_dir,
                                             *pos, *scale)
                pass
            pass
        pass

    def TextDraw(self):
        for layer in self.RendererObjectList:
            for text in layer:
                if not text.isActive or not text.isDraw:
                    continue

                if type(text.text) is list:
                    for i, t in enumerate(text.text):
                        if text.type is 'Left':typePos = [0, 0]
                        elif text.type is 'Middle':typePos = [-len(t), 0]
                        elif text.type is 'Right':typePos = [len(t), 0]
                        pos = text.transform.Position + [0,-text.lineSpacing * i] + typePos
                        text.font.draw(*pos,
                                       t,
                                       text.color)
                    pass
                else:
                    if text.type is 'Left': typePos = [-len(text.text)* text.lineSpacing,0]
                    elif text.type is 'Middle': typePos = [-len(text.text) * text.lineSpacing/2, 0]
                    elif text.type is 'Right' : typePos = [0, 0]

                    text.font.draw(*text.transform.Position + typePos,
                                   text.text,
                                   text.color)
                pass
        pass

    def AddObject(self, obj, depth=0):
        if self.maxDeath <= depth:
            for i in range(depth - self.maxDeath + 1):
                self.RendererObjectList.append([])
            self.maxDeath = len(self.RendererObjectList)

        if type(obj) == list: self.RendererObjectList[depth] += obj
        else: self.RendererObjectList[depth].append(obj)
        pass

    def RemoveObject(self, obj):
        for layer in self.RendererObjectList:
            if len(layer) == 0:
                continue
            if obj in layer:
                layer.remove(obj)
                del obj
                break
        pass

    def RemoveLayer(self, death):
        layer = self.RendererObjectList[death]
        for obj in layer.copy():
            layer.remove(obj)
            del obj
        self.RendererObjectList.remove(layer)
        pass

    def Clear(self):
        for layer in self.RendererObjectList:
            for obj in layer:
                layer.remove(obj)
                del obj
            self.RendererObjectList.remove(layer)
    pass