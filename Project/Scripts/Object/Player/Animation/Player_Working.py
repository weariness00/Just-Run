from Scripts.Object.Player.Animation.Player_Static_State import *
from Scripts.Object.Player.Animation.Player_Idle import Player_Idle

class Player_Working:

    @staticmethod
    def enter(self, event):
        Static_State.enter(self, event)

        self.mainAnimation = self.workingAni

        if any(self.idle.values()) == False:
            self.cur_state.exit(self)  # 현재 이벤트 탈출
            self.cur_state = Player_Idle  # 다음 이벤트 저장
            self.cur_state.enter(self, null)  # 다음 이벤트 호출
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        Static_State.do(self)
        pass

    @staticmethod
    def draw(self):
        pass

    pass
