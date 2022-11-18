from Scripts.Afx import *
from Scripts.Object.Skill.Contain.StrongStrength import StrongStrength
from Scripts.Object.Skill.Contain.Clone_Techniqu import Clone_Techniqu
from Scripts.Object.Skill.Contain.Dash import Dash
from Scripts.Object.Skill.Contain.IntenseFlame import IntenseFlame
from Scripts.Object.Skill.Contain.BottledFire import BottledFire
from Scripts.Object.Skill.Contain.Volcano import Volcano
from Scripts.Object.Skill.Contain.MischievousFlame import MischievousFlame

class SkillContain:
    array = []
    maxIndex = 0
    def __init__(self):
        SkillContain.array.append(StrongStrength())
        SkillContain.array.append(Clone_Techniqu())
        SkillContain.array.append(Dash())
        SkillContain.array.append(IntenseFlame())
        SkillContain.array.append(BottledFire())
        SkillContain.array.append(Volcano())
        SkillContain.array.append(MischievousFlame())
        SkillContain.maxIndex = len(SkillContain.array)

        for skill in SkillContain.array:
            skill.SetActive(False)
            skill.LevelUp()
        pass

    def __del__(self):
        for skill in SkillContain.array:
            SkillContain.array.remove(skill)
        pass

    @staticmethod
    def RandomIndex():
        return random.randint(0, SkillContain.maxIndex - 1)
    pass