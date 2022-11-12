# 분신술
from Scripts.FrameWork.Text import Text
from Scripts.Object.Player.Player import *

class Clone_Techniqu(Skill):

    def __init__(self):
        super(Clone_Techniqu, self).__init__()
        # 객체 초기화
        self.cloneCount = -1

        self.skill_Type = 'Active'
        self.coolTime = 10

        self.image = load_image('image/UI/Skill/Clone_Techniqu.png')
        self.image_type = [0, 0, 64, 64]

        # Transform
        self.transform.Scale *= 0.5

        # Text 초기화
        self.skillName = '[분신술]'
        self.explain[0].text = 'Level 만큼의 숫자의 분신을 소환할 수 있습니다'
        self.explain.append(Text())
        self.explain[1].font = self.explain[1].fontList['Explain']
        self.explain[1].text = '분신들은 Player의 행동에 영향을 받습니다.'
        self.explain.append(Text())
        self.explain[2].font = self.explain[2].fontList['Explain']
        self.explain[2].text = '(Q)를 누르면 발동합니다.'

        # 능력 초기화
        pass

    def __del__(self):
        super(Clone_Techniqu, self).__del__()
        pass

    def Update(self):
        if time.time() - self.onSkillTime >= self.coolTime:
            self.onSkillTime = time.time()
            if self.cloneCount > 0:
                self.cloneCount -= 1
        pass

    def OnSkill(self):
        if self.cloneCount == 0:
            self.onSkillTime = time.time()

        self.cloneCount += 1

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
            newClone.lifeObject += [Life([100 * (i + lifeCount) + 50, Instance.windowSize[1] - 50]) for i in range(newClone.life - lifeCount)]

        for life in newClone.lifeObject:
            life.SetActive(False)
        pass

    def Handle_Event(self, event):
        if self.level <= self.cloneCount + 1:
            return

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            self.OnSkill()
        pass

    def LevelUp(self):
        super(Clone_Techniqu, self).LevelUp()
        pass

    pass