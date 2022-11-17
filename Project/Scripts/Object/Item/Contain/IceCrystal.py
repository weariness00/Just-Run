from Scripts.Object.Item.Item import *


class IceCrystal(Item):
    image = load_image('image/UI/Item/Ice_Crystal.png')
    def __init__(self):
        super(IceCrystal, self).__init__()

        self.image = IceCrystal.image
        self.image_type = [0, 0, 32, 32]
        pass

    def __del__(self):
        super(IceCrystal, self).__del__()
        pass

    def Disable(self):
        Item.renderList.RemoveObject(self)
        pass

    def Update(self):
        super(IceCrystal, self).Update()
        pass


    def Copy(self):
        return IceCrystal()

    pass