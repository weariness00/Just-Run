from Afx import *


class Tile(Object):

    def __init__(self, image, image_type):
        super(Tile, self).__init__()
        self.image = image
        self.image_type = image_type    #sheet에서의 이미지 위치
        self.tileSize = 0

        pass

    def Draw(self):
        if not self.isActive:
            return

        self.transform.Position *= self.tileSize
        x, y = self.transform.Position[0], self.transform.Position[1]
        self.image.clip_draw(self.image_type[0],self.image_type[1], self.image_type[2], self.image_type[3], x, y)
        # print(x,y)
        pass
    pass