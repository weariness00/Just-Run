from Scripts.Object.Player.Animation.Player_Static_State import *
from Scripts.Object.Player.Animation.Player_Working import Player_Working


class Player_Dash:
    Dash_Skill = None
    @staticmethod
    def enter(self, event):
        if Player_Dash.Dash_Skill is None:
            Player_Dash.Dash_Skill = self.skill

        Static_State.enter(self, event)
        self.mainAnimation = self.dashAni
        self.speed += Player_Dash.Dash_Skill.speed
        pass

    @staticmethod
    def exit(self):
        self.speed -= Player_Dash.Dash_Skill.speed
        pass

    @staticmethod
    def do(self):
        dTime = time.time() - Player_Dash.Dash_Skill.dashTime
        if dTime > 0.5:
            self.skill.isSkillOn = False
            self.collider.isCollide = True

            self.cur_state.exit(self)  # 현재 이벤트 탈출
            self.cur_state = Player_Working  # 다음 이벤트 저장
            self.cur_state.enter(self, null)  # 다음 이벤트 호출
            pass
        Static_State.do(self)
        pass

    @staticmethod
    def draw(self):
        pass

    pass