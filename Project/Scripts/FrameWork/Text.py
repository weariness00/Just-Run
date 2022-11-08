from Scripts.FrameWork.Transform import *

class Text:
    def __init__(self, size = 20):
        # 객체 초기화
        self.transform = Transform()
        self.text = 'None'

        self.font_Name = load_font('Font/Name.ttf', size)
        self.font_Explain = load_font('Font/Explain.ttf', size)
        self.font = self.font_Name
        self.color = [255, 255, 255]
        pass

    def __del__(self):
        pass

    def ReSize(self, size):
        del self.font_Name, self.font_Explain

        self.font_Name = load_font('Font/Name.ttf', size)
        self.font_Explain = load_font('Font/Explain.ttf', size)

        self.font = self.font_Name
        pass

    def Copy(self):
        t = Text()
        t.text = self.text
        t.font = self.font
        t.color = self.color
        return t
    pass