from Scripts.Object.Item.Item import *


class FireJewelry(Item):
    image = load_image('image/UI/Item/Fire_Jewelry.png')
    def __init__(self):
        super(FireJewelry, self).__init__()
        self.image = FireJewelry.image
        self.image_type = [0, 0, 32, 32]
        self.rotateSpeed = 60 # 초당 60도 회전
        pass

    def __del__(self):
        super(FireJewelry, self).__del__()
        pass

    def Update(self):
        self.image_radian = (self.image_radian + self.rotateSpeed * FrameTime.fTime) % 360.0


    def Copy(self):
        return FireJewelry()

    pass
