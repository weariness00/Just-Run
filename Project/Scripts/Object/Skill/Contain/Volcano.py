# 화산 대폭발
from Scripts.Object.Skill.Skill import *
from Scripts.Object.Monster.Monster import Monster


class Volcano(Skill):

    def __init__(self):
        super(Volcano, self).__init__()
        # 객체 초기화
        self.image = load_image('image/UI/Skill/Volcano.png')
        self.image_type = [0, 0, 512, 512]
        self.skill_Type = 'Passive'
        self.transform.Scale *= 40/512

        # Text 초기화
        self.skillName = '[화산 대폭발]'
        self.explain[0].text = '화염의 정렬이 화산을 자극 했다.'
        self.explain.append(Text())
        self.explain[1].font = self.explain[1].fontList['Explain']
        self.explain[1].text = '모든 Monster이 위축된다. Monster들의 크기가 소폭 작아진다.'
        self.explain.append(Text())
        self.explain[2].font = self.explain[1].fontList['Explain']
        self.explain[2].text = '최대 Level 5'
        pass

    def __del__(self):
        super(Volcano, self).__del__()
        pass

    def OnSkill(self):
        for monster in Monster.AllMonster:
            monster.transform.Scale *= 0.95

        pass

    def LevelUp(self):
        super(Volcano, self).LevelUp()
        if self.level >= 5:
            self.isMaxLevel = True
        pass
    pass