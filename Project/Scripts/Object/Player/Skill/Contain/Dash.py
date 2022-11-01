# 돌진

from Scripts.Object.Player.Skill.Skill import *

class Dash(Skill):
    def __init__(self):
        super(Dash, self).__init__()
        # 객체 초기화
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
        pass

    def Handle_Event(self, event):
        if (event.type, event.key) == (SDLK_DOWN, SDLK_LSHIFT) or \
                (event.type, event.key) == (SDLK_DOWN, SDLK_RSHIFT):
            self.OnSkill()
        pass

    pass