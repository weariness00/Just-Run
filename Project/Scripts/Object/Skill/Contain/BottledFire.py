# 화염병
from Scripts.Object.Skill.Skill import *
from Scripts.Object.Player.Player import Player

class BottledFire(Skill):

    def __init__(self):
        super(BottledFire, self).__init__()
        # 객체 초기화
        self.image = load_image('image/UI/Skill/Bottled_Fire.png')
        self.image_type = [0, 0, 512, 512]
        self.skill_Type = 'Passive'
        self.transform.Scale *= 40/512

        # Text 초기화
        self.skillName = '[화염병]'
        self.explain[0].text = '화염의 정수를 담은 병이다.'
        self.explain.append(Text())
        self.explain[1].font = self.explain[1].fontList['Explain']
        self.explain[1].text = '이 병을 마시면 Level * 10 만큼 빨라진다.'
        self.explain.append(Text())
        self.explain[2].font = self.explain[1].fontList['Explain']
        self.explain[2].text = '최대 Level 10'
        pass

    def __del__(self):
        super(BottledFire, self).__del__()
        pass

    def OnSkill(self):
        Player.this.addSpeed += 10
        pass

    def LevelUp(self):
        super(BottledFire, self).LevelUp()
        if self.level >= 10:
            self.isMaxLevel = True
        pass
    pass