from Scripts.FrameWork.Object import *
from Scripts.UI.Number import Number
import Scripts.State.LevelUp_State as LevelUP
import Scripts.State.GameWInner_State as GameWinner
import Scripts.FrameWork.game_framework as game_framework


class PlayTimer(Number):

    def __init__(self):
        super(PlayTimer, self).__init__()
        self.startTime = 0
        self.nowTime = 0
        self.winTime = 1000
        self.levelUpLengthTime = 30
        self.levelUpCount = 0
        self.isLevelUp = False # 난이도 상승을 위해 사용하는 임시 변수

        self.alignmentType = "Middle"

        self.Init()
        pass

    def __del__(self):
        super(PlayTimer, self).__del__()
        pass

    def Resume(self):
        self.startTime += FrameTime.diffTime
        pass

    def Update(self):
        t = math.ceil(time.time() - self.startTime)
        self.nowTime = t + t // 60 * 40

        self.ChangeNumber(t + t // 60 * 40)
        self.OnMark()
        if t % self.levelUpLengthTime >= self.levelUpLengthTime - 10:
            self.mark.image = Number.red_image
            for number in self.numberObjects:
                number.image = Number.red_image

        if t // self.levelUpLengthTime - self.levelUpCount > 0:
            self.levelUpCount += 1
            game_framework.push_state(LevelUP)
            self.isLevelUp = True

        if t >= self.winTime:
            game_framework.change_state(GameWinner)

        pass

    def Init(self):
        w = Instance.windowSize[0]
        h = Instance.windowSize[1]

        self.transform.Position += [w//2, h - 70]
        self.transform.Scale *= 0.5
        self.startTime = time.time()
        pass

    pass