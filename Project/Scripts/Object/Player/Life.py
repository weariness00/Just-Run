from Scripts.FrameWork.Object import *
from Scripts.FrameWork.Animation import *

class Life(Object):
    
    def __init__(self, position):
        super(Life, self).__init__()
        # Transform
        self.transform.Position = position
        self.transform.Scale *= 5

        # Animation
        self.redFireAni = Animation()
        self.redFireAni.image = load_image('image/UI/Life/Fire.png')
        self.redFireAni.image_type = [0, 0, 15, 20]
        self.redFireAni.frame = 4
        self.redFireAni.countSpeed = 5

        self.blueFireAni = Animation()
        self.blueFireAni.image = load_image('image/UI/Life/BlueFire.png')
        self.blueFireAni.image_type = [0, 0, 15, 20]
        self.blueFireAni.frame = 4
        self.blueFireAni.countSpeed = 5

        self.mainAnimation = self.redFireAni
        pass
    
    def __del__(self):
        super(Life, self).__del__()
        pass

    def Update(self):
        self.OnAnimation()
        self.time.start = time.time()
        pass

    def OnAnimation(self):
        self.mainAnimation.OnAnimation(self.time.OneFrameTime())

        self.image = self.mainAnimation.image
        self.image_type = self.mainAnimation.image_type
        pass

    pass