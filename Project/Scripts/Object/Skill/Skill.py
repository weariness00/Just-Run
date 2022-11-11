from Scripts.FrameWork.Text import *
from Scripts.Object.Player.Player import *

class Skill(Object):
    renderList = None
    def __init__(self):
        super(Skill, self).__init__()
        # 객체 초기화
        self.isSkillOn = False
        self.coolTime = 0   # 스킬 쿨타임
        self.onSkillTime = 0    # 스킬을 켰을때 재는 시간
        self.range = 0  # skill을 사용할 범위
        self.level = 0
        self.skill_Type = None    # Active, Passive

        self.name = 'Skill'

        # Transform
        self.transform.Scale *= 3

        # 스킬에 대한 능력치 관련
        # 스킬에 쓸 떄 사용할 이미지 -> 이거는 skill들 만들떄 거기서 초기화
        self.skillName = None
        self.nameText = Text(30)
        self.explain = Text()  # skill을 설명할 Text
        self.explain.font = self.explain.font_Explain

        Skill.renderList.AddObject(self)
        pass

    def __del__(self):
        pass

    def Update(self):
        skillTime = time.time() - self.onSkillTime
        if skillTime >= self.coolTime:
            self.isSkillOn = False

    def OnSkill(self):
        self.isSkillOn = True
        self.onSkillTime = time.time()
        pass

    def Handle_Event(self, event): # False 면 Event 실행 안함
        if time.time() - self.onSkillTime < self.coolTime:
            return False

        if self.isSkillOn is True:
            return False

        return True
        pass

    def LevelUp(self):
        self.level += 1
        self.nameText.text = self.skillName + ' (' + self.skill_Type + ') : ' + self.level.__str__()
        pass

    pass