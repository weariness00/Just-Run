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
        self.skillName = '[강인한 체력]'
        self.explain.text = '모든 목숨을 회복, 추가로 +1 만큼의 목숨을 얻습니다.'
        # 능력 초기화
        pass

    def __del__(self):
        pass

    def OnSkill(self):
        for life in Player.this.lifeObject[Player.this.life:]:
            life.mainAnimation = life.redFireAni

        Player.this.maxLife += 1
        Player.this.life = Player.this.maxLife

        newLife = Life([100 * Player.this.maxLife - 50, Instance.windowSize[1] - 50])

        newLife.redFireAni.count = random.randint(0,4)

        Player.this.lifeObject.append(newLife)
        Life.renderList.AddObject(newLife)
        pass

    def LevelUp(self):
        super(StrongStrength, self).LevelUp()
        pass
    pass