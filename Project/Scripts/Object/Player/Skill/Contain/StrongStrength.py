# 강인한 체력

from Scripts.Object.Player.Player import *

class StrongStrength(Skill):

    def __init__(self):
        super(StrongStrength, self).__init__()
        # 객체 초기화
        self.image = load_image('image/UI/Skill/StrongStrength.png')
        self.image_type = [0, 0, 32, 32]
        self.skill_Type = 'Passive'

        # Text 초기화
        self.skillName.text = '[강인한 체력]'
        self.explain.text = '모든 목숨을 회복, 추가로 +1 만큼의 목숨을 얻습니다.'
        # 능력 초기화
        pass

    def __del__(self):
        pass

    def OnSkill(self):
        i = 0
        for life in Player.this.lifeObject[Player.this.life:]:
            life.mainAnimation = life.redFireAni
            i += 1
        Player.this.life = Player.this.maxLife

        newLife = Life([100 * i + 50, Instance.windowSize[1] - 50])
        Player.this.lifeObject.append(newLife)
        pass

    pass