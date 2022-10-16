from Scripts.Afx import *

class FrameTime:
    def __init__(self):
        self.start = time.time()
        self.end = None
        pass

    def __del__(self):
        pass

    def OneFrameTime(self):
        fTeim = time.time() - self.start
        return float(fTeim)
        pass
    pass