from Scripts.Object.Player.Skill.SkillContain import *
from Scripts.Object.Player.Skill.Skill import *
from Scripts.Object.Player.Player import Player

class LevelUP_PopUp(Object):

    def __init__(self):
        super(LevelUP_PopUp, self).__init__()
        # 객체 초기화
        self.count = 2

        SkillContain.array[0].skillName.transform.Position += [800, 450]
        self.skillIndex = 0

        # Box UI 컬러
        self.yellowBox = Animation()
        self.yellowBox.image = load_image('image/UI/PopUp/Yellow.png')
        self.yellowBox.image_type = [0, 0, 24, 24]

        self.redBox = Animation()
        self.redBox.image = load_image('image/UI/PopUp/Red.png')
        self.redBox.image_type = [0, 0, 24, 24]

        self.blueBox = Animation()
        self.blueBox.image = load_image('image/UI/PopUp/Blue.png')
        self.blueBox.image_type = [0, 0, 24, 24]

        self.mainBox = self.yellowBox

        # Box UI 초기화
        self.textBoxObject = [Object() for i in range(3)]
        for i, boxObj in enumerate(self.textBoxObject):
            boxObj.image = self.mainBox.image
            boxObj.image_type = self.mainBox.image_type
            boxObj.transform.Position += [Instance.windowSize[0]//2 + 70, 150 * i + 300]
            boxObj.transform.Scale += [25, 5]
            pass

        self.imageBoxObject = [Object() for i in range(3)]
        for i, boxObj in enumerate(self.imageBoxObject):
            boxObj.image = self.mainBox.image
            boxObj.image_type = self.mainBox.image_type
            boxObj.transform.Position += [Instance.windowSize[0]//4 + 70, 150 * i + 300]
            boxObj.transform.Scale += [5, 5]
            pass

        self.ChangeBoxColor('Red')
        # Box 에 들어갈 스킬 image와 text
        self.boxText = [[], []]
        self.skillIndex = [-1,-1,-1]
        count = 0
        while True:
            if count >= 3:
                break
            index = SkillContain.RandomIndex()
            if self.skillIndex == index:
                continue
            self.skillIndex[count] = index
            count += 1
            pass

        for i in range(3):
            self.boxText[0].append(SkillContain.array[self.skillIndex[i]].skillName.Copy())
            self.boxText[0][i].transform.Position = self.textBoxObject[i].transform.Position + [-280, 50]
            self.boxText[0][i].color = (1, 1, 1)
            pass
        for i in range(3):
            self.boxText[1].append(SkillContain.array[self.skillIndex[i]].explain.Copy())
            self.boxText[1][i].transform.Position = self.textBoxObject[i].transform.Position + [-260, 0]
            self.boxText[1][i].color = (1, 1, 1)
            pass

        self.boxImage = [Object() for i in range(3)]
        for i, imageObj in enumerate(self.boxImage):
            # TODO 이 아래부터는 다 임시
            imageObj.image = SkillContain.array[self.skillIndex[i]].image
            imageObj.image_type = SkillContain.array[self.skillIndex[i]].image_type
            imageObj.transform.Position += self.imageBoxObject[i].transform.Position
            imageObj.transform.Scale = SkillContain.array[self.skillIndex[i]].transform.Scale
            pass
        pass

    def __del__(self):
        del self.textBoxObject, self.imageBoxObject
        del self.boxImage, self.boxText
        del self.yellowBox, self.redBox, self.blueBox
        pass

    def OnSkill(self):
        if SkillContain.array[self.skillIndex[self.count]].skill_Type == 'Passive':
            SkillContain.array[self.skillIndex[self.count]].OnSkill()
        else:
            Player.this.skill = SkillContain.array[self.skillIndex[self.count]]
            Player.this.skill.transform.Position = Player.this.skillBox.transform.Position
            Player.this.skill.transform.Info()
        pass

    def ChangeBoxColor(self, color):
        if color == 'Yellow':
            self.mainBox = self.yellowBox
        elif color == 'Red':
            self.mainBox = self.redBox
        elif color == 'Blue':
            self.mainBox = self.blueBox

        for i in range(3):
            self.textBoxObject[i].image = self.yellowBox.image
            self.imageBoxObject[i].image = self.yellowBox.image

        self.textBoxObject[self.count].image = self.mainBox.image
        self.imageBoxObject[self.count].image = self.mainBox.image
        pass
    pass