from Scripts.Object.Player.Animation.Player_Static_State import *

class Player_Idle:

    @staticmethod
    def enter(self, event):
        Static_State.enter(self,event)
        self.mainAnimation = self.idleAni
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