from Scripts.FrameWork.Object import *
from Scripts.FrameWork.Animation import *

class Life(Object):
    renderList = None  # 동적할당해주는 것들은 자체적으로 렌더를 가짐
    updateList = None
    def __init__(self, position):
        super(Life, self).__init__()
        self.name = 'Life'


        # Transform
        self.transform.Position += position
        self.transform.Scale *= 5

        count = random.randint(0, 4)
        # Animation
        self.redFireAni = Animation()
        self.redFireAni.image = load_image('image/UI/Life/Fire.png')
        self.redFireAni.image_type = [0, 0, 15, 20]
        self.redFireAni.frame = 4
        self.redFireAni.countSpeed = 5
        self.redFireAni.count = count

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
        pass

    def OnAnimation(self):
        self.mainAnimation.OnAnimation(FrameTime.fTime)

        self.image = self.mainAnimation.image
        self.image_type = self.mainAnimation.image_type
        pass

    pass