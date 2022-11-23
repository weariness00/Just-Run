# 불의 방패
from Scripts.Object.Skill.Skill import *
from Scripts.Object.Player.Player import Player
from Scripts.FrameWork.Effect import Effect

class Barrier(Effect):
    image = load_image('Effect/Fire/FireRing.png')
    def __init__(self):
        super(Barrier, self).__init__(2)
        self.isLifeCycle = True
        self.frame_X = 8
        self.frame_Y = 5
        self.countSpeed = 30
        self.name += " : Fire Ring"

        self.image = Barrier.image
        self.image_type = [0, 0, 1024//8, 630//5]
        pass

    def __del__(self):
        super(Barrier, self).__del__()
        pass

    pass

class FireBarrier(Skill):
    def __init__(self):
        super(FireBarrier, self).__init__()
        self.image = load_image('image/UI/Skill/FireBarrier.png')
        self.image_type = [0,0,512,512]
        self.skill_Type = 'Active'
        self.transform.Scale *= 30/512

        # Text 초기화
        self.skillName = '[불의 방패]'
        self.explain[0].text = '따뜻한 불길이 모여 나를 지켜준다.'
        self.explain.append(Text())
        self.explain[1].font = self.explain[1].fontList['Explain']
        self.explain[1].text = 'level * 2만큼의 시간만큼 무적이 된다.'
        self.explain.append(Text())
        self.explain[2].font = self.explain[1].fontList['Explain']
        self.explain[2].text = '최대 Level 5, CoolTime 3, Space Bar을 누르면 발동'

        # Barrier
        self.barrier = Barrier()
        self.barrier.SetActive(False)
        self.startTime = 0

        pass

    def __del__(self):
        super(FireBarrier, self).__del__()
        pass

    def Update(self):
        super(FireBarrier, self).Update()
        self.barrier.transform.Position = Player.this.transform.Position - [0, 50]
        pass
    def OnSkill(self):
        super(FireBarrier, self).OnSkill()
        Player.this.OnGotMode(self.level * 2)
        self.onSkillTime += self.level * 2
        self.barrier.lifeTime = self.level * 2
        self.barrier.SetActive(True)
        self.startTime = time.time()
        pass

    def Handle_Event(self, event):
        if not super(FireBarrier, self).Handle_Event(event):
            return

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            self.OnSkill()
        pass

    def LevelUp(self):
        super(FireBarrier, self).LevelUp()
        if self.level >= 5:
            self.isMaxLevel = True
        pass
    pass