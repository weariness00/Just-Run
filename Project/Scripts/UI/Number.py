from Scripts.FrameWork.UI import *

class Number(UI):
    yellow_image = load_image('image/Number/Yellow_Number.png')
    red_image = load_image('image/Number/Red_Number.png')
    blue_image = load_image('image/Number/Blue_Number.png')
    def __init__(self, depth = 0):
        super(Number, self).__init__()
        self.depth = depth

        self.image = Number.yellow_image

        self.alignmentType = "Left"
        self.numberObjects = []
        self.mark = Object()
        self.isMark = False
        # self.mark.SetActive(False)
        self.mark.image = Number.yellow_image
        self.mark.image_type = [120, 0, 40, 146]
        self.mark.SetActive(False)
        UI.renderList.AddObject(self.mark, self.depth)

        self.name = 'Timer Number'
        pass

    def __del__(self):
        super(Number, self).__del__()
        pass

    def Enable(self):
        if self.isMark: self.mark.SetActive(True)

        pass

    def Disable(self):
        if self.isMark: self.mark.SetActive(False)
        for obj in self.numberObjects:
            UI.renderList.RemoveObject(obj)
        self.numberObjects.clear()
        pass

    def ChangeNumber(self, number):
        for obj in self.numberObjects:
            UI.renderList.RemoveObject(obj)

        number_list = list(map(int, str(number)))

        self.numberObjects = [Object() for i in range(len(number_list))]
        numberObjLen = len(self.numberObjects) - 1

        for i, num in enumerate(number_list):
            self.numberObjects[i].SetActive(self.isActive)
            self.numberObjects[i].image = self.image
            self.numberObjects[i].image_type = [num * 120, 0, 120, 146]
            if self.alignmentType == "Left":
                linePos = self.transform.Scale * [i * 100, 0]
            elif self.alignmentType == "Middle":
                linePos = self.transform.Scale * [i * 100 - numberObjLen * 50, 0]
            self.numberObjects[i].transform.Position = self.transform.Position + linePos
            self.numberObjects[i].transform.Scale = self.transform.Scale
            self.numberObjects[i].name = self.name

        UI.renderList.AddObject(self.numberObjects, self.depth)
        pass

    def OnMark(self):
        self.isMark = True
        numberObjLen = len(self.numberObjects) - 1
        if numberObjLen > 1:
            self.mark.SetActive(True)
            self.mark.image = self.image
            self.mark.transform.Position = self.transform.Position + [-70, 0] * self.transform.Scale
            self.mark.transform.Scale = self.transform.Scale
            for i in range(numberObjLen + 1 - 2):
                self.numberObjects[i].transform.Position += [-10, 0]
        pass

    pass