# 장난꾸러기 불꽃

from Scripts.UI.Text import Text
from Scripts.Object.Player.Player import *

class WildFlame(Object):
    def __init__(self):
        super(WildFlame, self).__init__()
        self.isActive = False
        pass

    def __del__(self):
        super(WildFlame, self).__del__()
        pass

    def Enable(self):
        self.transform.
        pass

class Clone_Techniqu(Skill):

    def __init__(self):
        super(Clone_Techniqu, self).__init__()
        # 객체 초기화
        self.skill_Type = 'Active'
        self.coolTime = 10

        self.image = load_image('image/UI/Skill/Clone_Techniqu.png')
        self.image_type = [0, 0, 64, 64]

        # Transform
        self.transform.Scale *= 0.5

        # Text 초기화
        self.skillName = '[장난꾸러기 불꽃]'
        self.explain[0].text = 'level 만큼의 시간동안 제멋대로 움직이다가 사라지는 불꽃을 소환합니다.'
        self.explain.append(Text())
        self.explain[1].font = self.explain[1].fontList['Explain']
        self.explain[1].text = '불꽃에 닿는 몬스터는 이동속도가 50%만큼 느려집니다.'
        self.explain.append(Text())
        self.explain[2].font = self.explain[2].fontList['Explain']
        self.explain[2].text = '사라진 후 5초뒤 나타납니다. 최대 Level 3'

        # 능력 초기화
        self.flame = WildFlame()

        pass

    def __del__(self):
        super(Clone_Techniqu, self).__del__()
        pass

    def Update(self):
        if time.time() - self.onSkillTime >= self.coolTime:
            self.onSkillTime = time.time()

        pass

    def OnSkill(self):
        super(Clone_Techniqu, self).OnSkill()
        self.flame.SetActive(True)
        pass

    def LevelUp(self):
        super(Clone_Techniqu, self).LevelUp()
        if self.level >= 2:
            self.isMaxLevel = True
        pass

    pass