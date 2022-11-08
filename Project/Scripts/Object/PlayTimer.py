from Scripts.FrameWork.Object import *
from Scripts.UI.Number import Number

class PlayTimer(Object):

    def __init__(self):
        super(PlayTimer, self).__init__()
        self.minute = Number()
        self.second = [Number(), Number()]

        self.Init()
        pass

    def __del__(self):
        super(PlayTimer, self).__del__()
        pass

    def Init(self):
        w = Instance.windowSize[0]
        h = Instance.windowSize[1]
        self.minute.transform.Scale *= 0.5
        self.minute.transform.Position += [w//2 - 60, h - 80]
        self.second[0].transform.Scale *= 0.5
        self.second[0].transform.Position += [w//2 + 10, h - 80]
        self.second[1].transform.Scale *= 0.5
        self.second[1].transform.Position += [w//2 + 60, h - 80]
        pass

    pass