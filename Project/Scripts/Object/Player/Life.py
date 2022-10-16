from Scripts.FrameWork.Object import *


class Life(Object):
    
    def __init__(self, MaxLife=3):
        super(Life, self).__init__()
        self.maxLife = MaxLife
        self.life = MaxLife
        
        # Animation 
        self.redFireObject = Object()
        self.blueFireObject = Object()
        self._defaultName = 'image/UI/Life/'
        self.redFireObject._sprite_Name = Instance.SetPngName(self._defaultName, 'Fire')
        self.blueFireObject._sprite_Name = Instance.SetPngName(self._defaultName, 'BlueFire')
        pass
    
    def __del__(self):
        super(Life, self).__del__()
        pass
    
    pass