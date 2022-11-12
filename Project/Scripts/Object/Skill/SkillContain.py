from Scripts.Afx import *
from Scripts.Object.Skill.Contain.StrongStrength import StrongStrength
from Scripts.Object.Skill.Contain.Clone_Techniqu import Clone_Techniqu
from Scripts.Object.Skill.Contain.Dash import Dash

class SkillContain:
    array = []
    maxIndex = None
    def __init__(self):
        self.array.append(StrongStrength())
        self.array.append(Clone_Techniqu())
        self.array.append(Dash())
        SkillContain.maxIndex = len(self.array)

        for skill in SkillContain.array:
            skill.SetActive(False)
            skill.LevelUp()
        pass

    def __del__(self):
        pass

    @staticmethod
    def RandomIndex():
        return random.randint(0, SkillContain.maxIndex - 1)
    pass