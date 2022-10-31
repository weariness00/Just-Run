from Scripts.Object.Player.Skill.Skill import *
from Scripts.Object.Player.Skill.Contain.StrongStrength import StrongStrength
from Scripts.Object.Player.Skill.Contain.Clone_Techniqu import Clone_Techniqu
from Scripts.Object.Player.Skill.Contain.Dash import Dash

class SkillContain:
    array = []
    maxIndex = None
    def __init__(self):
        self.array.append(StrongStrength())
        self.array.append(Clone_Techniqu())
        self.array.append(Dash())
        SkillContain.maxIndex = len(self.array)
        print(self.maxIndex)
        pass

    @staticmethod
    def RandomIndex():
        return random.randint(0, SkillContain.maxIndex - 1)
    pass