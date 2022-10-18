from Scripts.FrameWork.Object import *

class Camera:
    MainCamera = None

    def __init__(self, transform = Transform()):
        self.transform = transform

    pass

# Camera.MainCamera = Camera()