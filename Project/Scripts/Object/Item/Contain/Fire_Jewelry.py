from Scripts.Object.Item.Item import *


class FireJewelry(Item):
    image = load_image('image/UI/Item/Fire_Jewelry.png')
    def __init__(self):
        super(FireJewelry, self).__init__()

        self.image = FireJewelry.image
        self.image_type = [0, 0, 32, 32]
        pass

    def __del__(self):
        super(FireJewelry, self).__del__()
        pass

    def Disable(self):
        Item.renderList.RemoveObject(self)
        pass

    def Update(self):
        super(FireJewelry, self).Update()
        pass


    def Copy(self):
        return FireJewelry()

    pass
