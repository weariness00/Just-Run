from Scripts.Object.Skill.SkillContain import *
from Scripts.Object.Skill.Skill import *
from Scripts.Object.Player.Player import Player

class LevelUP_PopUp(Object):
    objectRender = None
    uiRender = None
    textRender = None
    def __init__(self):
        super(LevelUP_PopUp, self).__init__()
        # 객체 초기화
        self.count = 2

        # SkillContain.array[0].nameText.transform.Position += [800, 450]
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
        maxLevelSkillCount = 0
        for skill in SkillContain.array:
            if skill.isMaxLevel is True:
                 maxLevelSkillCount += 1

        setIndex = set()
        while True:
            if len(setIndex) >= 3:
                break

            index = SkillContain.RandomIndex()
            # maxLevel인 스킬 제외
            if SkillContain.array[index].isMaxLevel is True:
                continue

            setIndex.add(index)
            pass
        self.skillIndex = list(setIndex)

        for i in range(3):
            self.boxText[0].append(SkillContain.array[self.skillIndex[i]].nameText.Copy())
            self.boxText[0][i].transform.Position = self.textBoxObject[i].transform.Position + [-280, 50]
            self.boxText[0][i].color = [84, 0, 33]
            pass
        for i in range(3):
            self.boxText[1].append([])
            for index, explain in enumerate(SkillContain.array[self.skillIndex[i]].explain):
                self.boxText[1][i].append(explain.Copy())
                self.boxText[1][i][index].transform.Position = self.textBoxObject[i].transform.Position + [-260, 15 -30 * index]
                self.boxText[1][i][index].color = (35, 35, 35)
            pass

        self.boxImage = [Object() for i in range(3)]
        for i, imageObj in enumerate(self.boxImage):
            # TODO 이 아래부터는 다 임시
            imageObj.image = SkillContain.array[self.skillIndex[i]].image
            imageObj.image_type = SkillContain.array[self.skillIndex[i]].image_type
            imageObj.transform.Position += self.imageBoxObject[i].transform.Position
            imageObj.transform.Scale = SkillContain.array[self.skillIndex[i]].transform.Scale
            pass

        LevelUP_PopUp.uiRender.AddObject(self.textBoxObject, 1)
        LevelUP_PopUp.uiRender.AddObject(self.imageBoxObject, 1)
        LevelUP_PopUp.uiRender.AddObject(self.boxImage, 2)

        pass

    def __del__(self):
        del self.textBoxObject, self.imageBoxObject
        del self.boxImage, self.boxText
        del self.yellowBox, self.redBox, self.blueBox
        pass

    def ChangeSkill(self):
        if SkillContain.array[self.skillIndex[self.count]].skill_Type == 'Passive':
            SkillContain.array[self.skillIndex[self.count]].OnSkill()
            SkillContain.array[self.skillIndex[self.count]].LevelUp()
        else:
            Player.this.skill.SetActive(False)
            Player.this.skill = SkillContain.array[self.skillIndex[self.count]]
            Player.this.skill.LevelUp()
            Player.this.skill.transform.Position = Player.this.skillBox.transform.Position
            Player.this.skill.SetActive(True)
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