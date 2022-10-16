from Scripts.FrameWork.Object import *


class Life(Object):
    
    def __init__(self, position):
        super(Life, self).__init__()
        # Transform
        self.transform.Position = position
        self.transform.Scale *= 5

        # Animation
        self.redFireObject = Object()
        self.blueFireObject = Object()

        self._defaultName = 'image/UI/Life/'
        self.ChangeSprite('Fire')


        pass
    
    def __del__(self):
        super(Life, self).__del__()
        pass

    def Update(self):
        self.__Animation()
        self.time.start = time.time()
        pass

    def __Animation(self):
        self.image_type[0] = (int(self._ani_Count) % self._ani_Frame) * self.image_type[2]
        self._ani_Count += self.time.OneFrameTime() * 10
        pass

    def ChangeSprite(self, state):
        self._sprite_Name = state
        self.image_type = [0, 0, 15, 20]
        self._ani_Frame = 4

        ani_Name = Instance.SetPngName(self._defaultName, self._sprite_Name)
        self.image = load_image(ani_Name)

        pass
    
    pass