from Scripts.FrameWork.Object import *

class Number(Object):
    renderList = None
    yellow_image = load_image('image/Number/Yellow_Number.png')
    def __init__(self):
        super(Number, self).__init__()
        self.numberObjects = []

        self.name = 'Number'
        pass

    def __del__(self):
        super(Number, self).__del__()
        pass

    def ChangeNumber(self, number):
        for obj in self.numberObjects:
            Number.renderList.RemoveRenderObject(obj)

        number_str = number.__str__()
        number_count = len(number_str)
        numbers = [int(number_str[i]) for i in range(number_count)]

        self.numberObjects = [Object() for i in range(number_count)]

        for i in range(number_count):
            self.numberObjects[i].image = Number.yellow_image
            self.numberObjects[i].image_type = [numbers[number_count - i - 1] * 120, 0, 120, 146]
            self.numberObjects[i].transform.Position = self.transform.Position - [i * 50, 0]
            self.numberObjects[i].transform.Scale = self.transform.Scale
            self.numberObjects[i].name = self.name

        Number.renderList.RendererObjectList += self.numberObjects
        pass

    pass