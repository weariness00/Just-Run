# 분신술

from Scripts.Object.Player.Skill.Skill import *

class Clone_Techniqu(Skill):

    def __init__(self):
        super(Clone_Techniqu, self).__init__()
        # 객체 초기화
        self.image = load_image('image/UI/Skill/Clone_Techniqu.png')
        self.image_type = [0, 0, 64, 64]
        self.skill_Type = 'Active'

        # Transform
        self.transform.Scale *= 0.5

        # Text 초기화
        self.skillName.text = '[분신술]'
        self.explain.text = 'Level 만큼의 숫자의 분신을 소환합니다\n분신들은 Player 주변을 맴돕니다.'
        # 능력 초기화
        pass

    def __del__(self):
        pass

    def OnSkill(self):

        pass

    def Handle_Event(self, event):
        if (event.type, event.key) == (SDLK_DOWN, SDLK_q):
            self.OnSkill()
        pass

    pass