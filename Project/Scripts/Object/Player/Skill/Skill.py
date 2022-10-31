from Scripts.FrameWork.Text import *
from Scripts.Object.Player.Player import *

class Skill(Object):
    def __init__(self):
        super(Skill, self).__init__()
        # 객체 초기화
        self.name = 'Skill'
        self.collTime = 5
        self.range = 0  # skill을 사용할 범위
        self.level = 0

        # 스킬에 대한 능력치 관련
        # 스킬에 쓸 떄 사용할 이미지 -> 이거는 skill들 만들떄 거기서 초기화
        self.skillName = Text(30)
        self.explain = Text()  # skill을 설명할 Text
        self.explain.font = self.explain.font_Explain

        # Timer
        pass

    def __del__(self):
        pass

    def OnSkill(self):
        pass

    def Handle_Event(self, event):
        pass

    pass