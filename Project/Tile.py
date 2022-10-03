from Afx import *


class Tile(Object):

    def __init__(self, image, image_type):
        super(Tile, self).__init__()
        self.image = image
        self.image_type = image_type    #sheet에서의 이미지 위치
        self.tileSize = None

        pass

    def Draw(self):
        if not self.isActive:
            return

        x, y = self.transform.Position[0], self.transform.Position[1]
        self.image.draw(x, y)
        pass
    pass