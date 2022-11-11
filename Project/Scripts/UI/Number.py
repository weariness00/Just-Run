from Scripts.FrameWork.Object import *

class Number(Object):
    renderList = None
    yellow_image = load_image('image/Number/Yellow_Number.png')
    red_image = load_image('image/Number/Red_Number.png')
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
            Number.renderList.RemoveObject(obj)

        number_str = number.__str__()
        number_count = len(number_str)
        numbers = [int(number_str[i]) for i in range(number_count)]

        self.numberObjects = [Object() for i in range(number_count)]

        for i in range(number_count):
            self.numberObjects[i].image = Number.yellow_image
            self.numberObjects[i].image_type = [numbers[i] * 120, 0, 120, 146]
            self.numberObjects[i].transform.Position = self.transform.Position + [i * 100, 0] * self.transform.Scale
            self.numberObjects[i].transform.Scale = self.transform.Scale
            self.numberObjects[i].name = self.name

        Number.renderList.RendererObjectList += self.numberObjects
        pass

    pass