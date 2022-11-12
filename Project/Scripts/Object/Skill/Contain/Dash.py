# 돌진

from Scripts.Object.Skill.Skill import *
from Scripts.Object.Player.Player import Player
from Scripts.Object.Player.Animation.PlayerAnimationController import *

class Dash(Skill):
    def __init__(self):
        super(Dash, self).__init__()
        # 객체 초기화
        self.dashTime = 0
        self.speed = -100

        self.image = load_image('image/UI/Skill/Dash.png')
        self.image_type = [0, 0, 32, 32]
        self.skill_Type = 'Active'
        self.coolTime = 1

        # Text 초기화
        self.skillName = '[돌진]'
        self.explain[0].text = 'Level * 100 만큼 돌진 합니다.'
        self.explain.append(Text())
        self.explain[1].font = self.explain[1].fontList['Explain']
        self.explain[1].text = '돌진시에는 무적이 됩니다.'

        # 능력 초기화
        pass

    def __del__(self):
        pass

    def OnSkill(self):
        super(Dash, self).OnSkill()

        self.dashTime = time.time()
        Player.this.collider.isCollide = False
        pass

    def Handle_Event(self, event):
        if super(Dash, self).Handle_Event(event) is False:
            return

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LSHIFT) or \
                (event.type, event.key) == (SDL_KEYDOWN, SDLK_RSHIFT):
            self.OnSkill()
            Player.this.cur_state.exit(Player.this)  # 현재 이벤트 탈출
            Player.this.cur_state = next_state[Player_Dash][null]  # 다음 이벤트 저장
            Player.this.cur_state.enter(Player.this, event)  # 다음 이벤트 호출
        pass

    def LevelUp(self):
        super(Dash, self).LevelUp()

        if self.isSkillOn is True:
            Player.this.speed -= self.speed
            self.speed += 100
            Player.this.speed += self.speed
        else:
            self.speed += 100

        pass
    pass