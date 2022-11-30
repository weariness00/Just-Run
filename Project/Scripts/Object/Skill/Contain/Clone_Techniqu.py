# 분신술
from Scripts.Object.Skill.Skill import *
from Scripts.UI.Text import Text
from Scripts.Object.Player.Player import Player
from Scripts.Object.Player.Life import Life
class Clone_Techniqu(Skill):

    def __init__(self):
        super(Clone_Techniqu, self).__init__()
        # 객체 초기화
        self.clones = []
        self.cloneCount = 0
        self.cloneNumber = Number(3)
        self.cloneNumber.SetActive(False)
        self.cloneNumber.transform.Scale *= 0.2
        self.cloneNumber.transform.Position = [Instance.windowSize[0]//2 + 50, 150]

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
        self.explain[2].text = '(Q)를 누르면 발동합니다. 최대 Level 2'

        # 능력 초기화
        pass

    def __del__(self):
        super(Clone_Techniqu, self).__del__()
        pass

    def Enable(self):
        super(Clone_Techniqu, self).Enable()
        self.cloneNumber.ChangeNumber(self.level - self.cloneCount)
        self.cloneNumber.SetActive(True)
        pass

    def Disable(self):
        super(Clone_Techniqu, self).Disable()
        self.cloneNumber.SetActive(False)
        pass

    def Update(self):
        for clone in self.clones:
            if clone.life <= 0:
                self.clones.remove(clone)
                Object.updateList.remove(clone)
                Object.renderList.RemoveObject(clone)
            pass

        self.cloneNumber.ChangeNumber(self.level - self.cloneCount)
        super(Clone_Techniqu, self).Update()
        skillTime = time.time() - self.onSkillTime
        if skillTime >= self.coolTime:
            if self.cloneCount > 0:
                super(Clone_Techniqu, self).OnSkill()
                self.cloneCount -= 1
        pass

    def OnSkill(self):
        if self.cloneCount >= self.level:
            return
        if len(self.clones) >= self.level:
            return
        if not self.isSkillOn:
            super(Clone_Techniqu, self).OnSkill()

        self.cloneCount += 1
        newClone = Player(Player.this.name)
        newClone.name = "Player Clone"
        newClone.speed += 100
        newClone.transform.Position += Player.this.transform.Position
        newClone.circleLay.SetActive(False)

        newClone.maxLife = Player.this.maxLife
        newClone.life = newClone.maxLife

        lifeCount = len(newClone.lifeObject)
        if lifeCount < newClone.life:
            newClone.lifeObject += [Life([100 * (i + lifeCount) + 50, Instance.windowSize[1] - 50]) for i in range(newClone.life - lifeCount)]

        for life in newClone.lifeObject:
            life.SetActive(False)

        self.clones.append(newClone)
        Object.updateList.remove(newClone)
        Object.updateList.insert(1, newClone)
        pass

    def Handle_Event(self, event):
        if self.level <= self.cloneCount:
            return

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            self.OnSkill()
        pass

    def LevelUp(self):
        super(Clone_Techniqu, self).LevelUp()
        if self.level >= 2:
            self.isMaxLevel = True
            self.level = 2
        pass

    pass