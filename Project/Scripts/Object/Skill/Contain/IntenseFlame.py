# 강렬한 화염
from Scripts.Object.Skill.Skill import *
from Scripts.Object.Monster.Monster import Monster


class IntenseFlame(Skill):

    def __init__(self):
        super(IntenseFlame, self).__init__()
        # 객체 초기화
        self.image = load_image('image/UI/Skill/IntenceFlame.png')
        self.image_type = [0, 0, 64, 64]
        self.skill_Type = 'Passive'
        self.transform.Scale *= 0.7

        # Text 초기화
        self.skillName = '[강렬한 화염]'
        self.explain[0].text = '몬스터가 Level 만큼 빨리 소멸됩니다.'
        self.explain.append(Text())
        self.explain[1].font = self.explain[1].fontList['Explain']
        self.explain[1].text = '최대 Level = 3'
        pass

    def __del__(self):
        super(IntenseFlame, self).__del__()
        pass

    def OnSkill(self):
        Monster.addLifeTime -= 1
        pass

    def LevelUp(self):
        super(IntenseFlame, self).LevelUp()
        if self.level >= 3:
            self.isMaxLevel = True
        pass
    pass