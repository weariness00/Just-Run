from Scripts.FrameWork.Object import *

class Tile(Object):
    image = load_image("image\Tile\snow-expansion.png")

    def __init__(self, image_type, collider = None):
        super().__init__()
        self.image = Tile.image
        self.image_type = image_type    #sheet에서의 이미지 위치
        self.tileSize = 0
        self.collider = collider
        if self.collider is not None: self.collider.InitTransform(self.transform)

        self.typeIndex = 0
        pass

    def __del__(self):
        super(Tile, self).__del__()
        pass

    def changeTypeIndex(self, index):
        if self.typeIndex == index:
            return
        elif self.typeIndex == 0 and index == 1:
            self.image_type[0] += 128
            pass
        elif self.typeIndex == 1 and index == 0:
            self.image_type[0] -= 128
            pass
        pass

    pass