from Scripts.Object.Item.Item import *


class FireJewelry(Item):
    image = load_image('image/UI/Item/Fire_Jewelry.png')
    def __init__(self):
        super(FireJewelry, self).__init__()

        self.name.text = "불의 보석"
        self.explain[0].text = '내부에 불이 타오르고 있는 신비한 보석이다.'
        self.explain.append(Text())
        self.explain[1].text = '왠지 모르게 가지고 있으면 힘이 난다.'

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
