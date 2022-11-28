from Scripts.FrameWork.Object import *

class Text(Object):
    list = ['Name', 'Explain', 'KR_HSGyeoulNoonkot', 'EN_Bafora', 'Stone_Head', 'Fire', 'Ghanachocolate']
    renderList = None
    def __init__(self, size = 20, death=0):
        # 객체 초기화
        self.transform = Transform()
        self.text = 'Text'
        self.type = 'Left'
        self.isActive = True
        self.isDraw = True

        self.fontList = dict()
        for font in Text.list:
            self.fontList[font] = load_font('Font/' + font + '.ttf', size)

        self.font = self.fontList[Text.list[0]]
        self.color = [255, 255, 255]

        self.lineSpacing = size

        Text.renderList.AddObject(self, death)
        pass

    def __del__(self):
        pass

    def SetTextBox(self, w, h, str):
        strSize = len(str)
        text = []
        for i in range(strSize//w + 1):
            if i >= h:
                break
            if (i + 1) * w >= strSize:
                text.append(str[i * w: strSize])
            else:
                text.append(str[i * w: (i + 1) * w])

        self.text = text
        pass

    def ReSize(self, size):
        for i, font in enumerate(self.fontList):
            if font == self.font:
                font = load_font('Font/' + Text.list[i] + '.ttf', size)
                self.font = font

        pass

    def Info(self):
        print(self.text)
        print(self.color)
        pass

    def Copy(self):
        t = Text()
        t.text = self.text
        t.font = self.font
        t.color = self.color
        return t
    pass