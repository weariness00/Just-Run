from Scripts.FrameWork.Object import *
from Scripts.UI.Text import Text
from Scripts.FrameWork.UI import UI
from Scripts.UI.Number import Number

class Skill(Object):
    def __init__(self):
        super(Skill, self).__init__()
        # 객체 초기화
        self.isSkillOn = False
        self.isMaxLevel = False # 최대 레벨이 되면 레벨업 화면에 안뜨게함
        self.coolTime = 0   # 스킬 쿨타임
        self.onSkillTime = 0    # 스킬을 켰을때 재는 시간
        self.range = 0  # skill을 사용할 범위
        self.level = -1
        self.skill_Type = "None"    # Active, Passive

        self.name = 'Skill'

        # Transform
        self.transform.Scale *= 3

        # CollTime GUI
        self.coolTimeNumber = Number(3)
        self.coolTimeNumber.image = Number.blue_image
        self.coolTimeNumber.SetActive(False)
        self.coolTimeNumber.transform.Scale *= 0.7
        self.coolTimeNumber.transform.Position += [Instance.windowSize[0]//2, 100] # 위치 임의 지정

        # 스킬에 대한 능력치 관련
        # 스킬에 쓸 떄 사용할 이미지 -> 이거는 skill들 만들떄 거기서 초기화
        self.skillName = "None"
        self.nameText = Text(30)
        self.explain = [Text()]  # skill을 설명할 Text
        self.explain[0].font = self.explain[0].fontList['Explain']

        UI.renderList.AddObject(self, 2)
        pass

    def __del__(self):
        super(Skill, self).__del__()
        pass

    def Enable(self):
        self.coolTimeNumber.SetActive(True)
        self.image.opacify(1)
        pass

    def Disable(self):
        self.coolTimeNumber.SetActive(False)
        pass

    def Resume(self):
        self.onSkillTime += FrameTime.diffTime
        if self.isSkillOn:
            self.image.opacify(0.5)
        pass

    def Update(self):
        skillTime = time.time() - self.onSkillTime
        self.coolTimeNumber.ChangeNumber(int(abs(self.coolTime - skillTime)))
        if skillTime >= self.coolTime:
            self.isSkillOn = False
            self.image.opacify(1)
            self.coolTimeNumber.SetActive(False)
    def OnSkill(self):
        self.isSkillOn = True
        self.image.opacify(0.5)
        self.coolTimeNumber.SetActive(True)
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