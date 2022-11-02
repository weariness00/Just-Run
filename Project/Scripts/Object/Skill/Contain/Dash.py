# 돌진

from Scripts.Object.Skill.Skill import *
from Scripts.Object.Player.Player import Player
from Scripts.Object.Player.Animation.PlayerAnimationController import *

class Dash(Skill):
    def __init__(self):
        super(Dash, self).__init__()
        # 객체 초기화
        self.dashTime = 0

        self.image = load_image('image/UI/Skill/Dash.png')
        self.image_type = [0, 0, 32, 32]
        self.skill_Type = 'Active'

        # Text 초기화
        self.skillName.text = '[돌진]'
        self.explain.text = 'Level * 100 만큼 돌진 합니다.\n돌진시에는 무적이 됩니다.'
        # 능력 초기화
        pass

    def __del__(self):
        pass

    def OnSkill(self):
        self.isSkillOn = True
        self.dashTime = time.time()
        Player.this.isGot = True
        Player.this.collider.isCollide = False
        Player.this.gotTime = time.time()
        Player.this.gotDurationTime = 0.5
        pass

    def Handle_Event(self, event):
        if self.isSkillOn is True:
            return

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LSHIFT) or \
                (event.type, event.key) == (SDL_KEYDOWN, SDLK_RSHIFT):
            self.OnSkill()
            Player.this.cur_state.exit(Player.this)  # 현재 이벤트 탈출
            Player.this.cur_state = next_state[Player_Dash][null]  # 다음 이벤트 저장
            Player.this.cur_state.enter(Player.this, event)  # 다음 이벤트 호출
        pass

    pass