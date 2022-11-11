import numpy

from Scripts.FrameWork.Object import *

class Effect(Object):
    renderList = None
    def __init__(self):
        super(Effect, self).__init__()
        self.isLifeCycle = False # Effect가 lifeTime만큼 실행될지 계속 실행될지에 대한 여부
        self.isOneCycle = False # Effect가 정해진 프레임 수 만큼 한 번 실행될지에 대한 여부
        self.lifeTime = 0 # Effect가 몇 초 동안 실행될지에 대한 변수
        self.startTime = 0

        self.frame_X = 0
        self.frame_Y = 0
        self.count_X = 0
        self.count_Y = 0
        self.countSpeed = 0

        self.name = 'Effect'
        self.isActive = False

        Effect.renderList.AddObject(self)
        pass

    def __del__(self):
        super(Effect, self).__del__()
        pass

    def Update(self):
        if self.isActive is False:
            return

        if self.count_X >= self.frame_X:
            self.count_X = 0
            self.count_Y += 1
            pass

        self.image_type[0] = int(self.count_X) * self.image_type[2]
        self.image_type[1] = (self.frame_Y - self.count_Y - 1) * self.image_type[3]
        self.count_X += FrameTime.fTime * self.countSpeed

        if self.isOneCycle is True:
            if self.count_Y == self.frame_Y:
                self.isActive = False
            pass
        elif self.isLifeCycle is True:
            t = time.time() - self.startTime
            if t >= self.lifeTime:
                self.isActive = False
            pass

        if self.count_Y == self.frame_Y:
            self.count_Y = 0

        pass

    def OnEffect(self, transform):
        self.isActive = True
        self.startTime = time.time()

        self.transform.Position = numpy.copy(transform.Position)
        pass
    pass