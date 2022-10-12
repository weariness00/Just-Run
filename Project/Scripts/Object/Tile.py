from Scripts.FrameWork.Object import *

class Tile(Object):

    def __init__(self, image, image_type, collider = None):
        super().__init__()
        self.image = image
        self.image_type = image_type    #sheet에서의 이미지 위치
        self.tileSize = 0
        self.collider = collider
        if self.collider is not None: self.collider.InitTransform(self.transform)

        pass

    pass