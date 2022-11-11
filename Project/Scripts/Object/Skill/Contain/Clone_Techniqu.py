# 분신술
from Scripts.Object.Player.Player import *

class Clone_Techniqu(Skill):

    def __init__(self):
        super(Clone_Techniqu, self).__init__()
        # 객체 초기화
        self.skill_Type = 'Active'
        self.coolTime = 1

        self.image = load_image('image/UI/Skill/Clone_Techniqu.png')
        self.image_type = [0, 0, 64, 64]

        # Transform
        self.transform.Scale *= 0.5

        # Text 초기화
        self.skillName = '[분신술]'
        self.explain.text = 'Level 만큼의 숫자의 분신을 소환합니다\n분신들은 Player 주변을 맴돕니다.'
        # 능력 초기화
        pass

    def __del__(self):
        pass

    def OnSkill(self):
        super(Clone_Techniqu, self).OnSkill()

        newClone = Player()
        Object.events = get_events()
        Object.updateList.remove(newClone)
        Object.updateList.insert(1, newClone)
        newClone.name = 'Player Clone'
        newClone.speed += 100
        newClone.transform.Position += Player.this.transform.Position

        newClone.maxLife = Player.this.maxLife
        newClone.life = newClone.maxLife

        lifeCount = len(newClone.lifeObject)
        if lifeCount < newClone.life:
            newClone.lifeObject += [Life([100 * (i + lifeCount) + 50, Instance.windowSize[1] - 50]) for i in newClone.life - lifeCount]
        pass

    def Handle_Event(self, event):
        if super(Clone_Techniqu, self).Handle_Event(event) is False:
            return

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            self.OnSkill()
        pass

    pass