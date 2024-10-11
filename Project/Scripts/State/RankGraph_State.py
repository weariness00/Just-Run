from Scripts.Afx import *
from Scripts.FrameWork.Object import Object
from Scripts.FrameWork.Animation import Animation
from Scripts.FrameWork.Render import Render
from Scripts.FrameWork.FrameTime import FrameTime
from Scripts.FrameWork.UI import UI
from Scripts.UI.Text import Text
from Scripts.UI.Button import Button

import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.Lobby_State as Lobby_State

from Data.PlayData import PlayData

back_Button = None

objectRender = None
uiRender = None
textRender = None

def enter():
    global back_Button
    global objectRender, uiRender, textRender
    Object.updateList = []

    objectRender = Render()
    objectRender.name += " : Object - RankGraph"
    uiRender = Render()
    uiRender.name += " : UI - RankGraph"
    textRender = Render()
    textRender.name += " : Text - RankGraph"

    Object.renderList = objectRender
    UI.renderList = uiRender
    Text.renderList = textRender

    back_Button = Button(1)
    back_Button.transform.Scale *= 2
    back_Button.transform.Position += [back_Button.image_type[2], back_Button.image_type[3]]
    back_Button.text = Text(40)
    back_Button.text.text = '로비'
    back_Button.text.type = "Middle"
    back_Button.text.transform.Position += back_Button.transform.Position

    backGround_UI = UI()
    backGround_UI.image = load_image('image/Background/Forest.png')
    backGround_UI.image_type = [0, 450, 1024, 450]
    backGround_UI.transform.Position += Instance.windowSize / 2
    backGround_UI.transform.Scale *= Instance.windowSize / [backGround_UI.image_type[2], backGround_UI.image_type[3]]

    explain_UI = ShowDataUI()
    explain_UI.transform.Position += [330 + 100, Instance.windowSize[1] - 70]
    explain_UI.playerNameText.text = "Name"
    explain_UI.playTimeText.text = "Time"
    explain_UI.monsterDeathCountText.text = "Kill"
    explain_UI.earnItemCountText.text = "Item"
    explain_UI.levelText.text = "Difficulty"
    explain_UI.speedText.text = "Speed"
    explain_UI.maxLifeText.text = "Max Life"
    explain_UI.lifeText.text = "Life"
    explain_UI.scoreText.text = "Score"
    nextDis = 0; explain_UI.playerNameText.transform.Position = explain_UI.transform.Position + [0, 0]
    nextDis += 220; explain_UI.playTimeText.transform.Position = explain_UI.transform.Position + [nextDis, 0]
    nextDis += 80; explain_UI.monsterDeathCountText.transform.Position = explain_UI.transform.Position + [nextDis, 0]
    nextDis += 60; explain_UI.earnItemCountText.transform.Position = explain_UI.transform.Position + [nextDis, 0]
    nextDis += 70; explain_UI.levelText.transform.Position = explain_UI.transform.Position + [nextDis, 0]
    nextDis += 250; explain_UI.speedText.transform.Position = explain_UI.transform.Position + [nextDis, 0]
    nextDis += 100; explain_UI.maxLifeText.transform.Position = explain_UI.transform.Position + [nextDis, 0]
    nextDis += 120; explain_UI.lifeText.transform.Position = explain_UI.transform.Position + [nextDis, 0]
    nextDis += 60; explain_UI.scoreText.transform.Position = explain_UI.transform.Position + [nextDis, 0]


    uiRender.AddObject(backGround_UI)
    RankPagePopup()
    pass

# finalization code
def exit():
    Object.updateList.clear()
    objectRender.__del__()
    uiRender.__del__()
    textRender.__del__()
    pass

def handle_events():

    events = get_events()
    Object.events = events
    for obj in Object.updateList:
        obj.Handle_Event()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
        pass
    pass


def update():
    if back_Button.isClick is True:
        game_framework.pop_state()
    for obj in Object.updateList:
        obj.Update()
    pass

def event_update():
    for obj in Object.updateList:
        obj.EventCall()
    pass

def draw():
    objectRender.Draw()
    uiRender.UIDraw()
    textRender.TextDraw()

    pass

def pause():
    pass

def resume():
    pass

class ShowDataUI(UI):
    def __init__(self):
        super(ShowDataUI, self).__init__()

        self.playerNameText = Text()
        self.playTimeText = Text()
        self.monsterDeathCountText = Text()
        self.earnItemCountText = Text()
        self.levelText = Text()
        self.speedText = Text()
        self.maxLifeText = Text()
        self.lifeText = Text()
        self.scoreText = Text()

        pass

    def TextInit(self):
        self.playerNameText.text = " "
        self.playTimeText.text = " "
        self.monsterDeathCountText.text = " "
        self.earnItemCountText.text = " "
        self.levelText.text = " "
        self.speedText.text = " "
        self.maxLifeText.text = " "
        self.lifeText.text = " "
        self.scoreText.text = " "
        pass

    def PositionUpdate(self):
        nextDis = 0; self.playerNameText.transform.Position = self.transform.Position + [0, 0]
        nextDis += 220; self.playTimeText.transform.Position = self.transform.Position + [nextDis, 0]
        nextDis += 80; self.monsterDeathCountText.transform.Position = self.transform.Position + [nextDis, 0]
        nextDis += 60; self.earnItemCountText.transform.Position = self.transform.Position + [nextDis, 0]
        nextDis += 70; self.levelText.transform.Position = self.transform.Position + [nextDis, 0]
        nextDis += 250; self.speedText.transform.Position = self.transform.Position + [nextDis, 0]
        nextDis += 100; self.maxLifeText.transform.Position = self.transform.Position + [nextDis, 0]
        nextDis += 120; self.lifeText.transform.Position = self.transform.Position + [nextDis, 0]
        nextDis += 60; self.scoreText.transform.Position = self.transform.Position + [nextDis,0]
        pass
    pass

class RankPagePopup(Object):
    def __init__(self):
        super(RankPagePopup, self).__init__()

        # Player Data 불러오기
        self.pd = PlayData()
        self.showMaxDataLenth = 10
        self.pageIndex = 0
        playerCount = self.pd.sheet["A1"].value
        self.maxPageIndex = playerCount // self.showMaxDataLenth
        self.lastPagePlayerCount = playerCount - self.showMaxDataLenth * self.maxPageIndex

        # Data를 보여줄 Text 셋팅
        self.dataUIList = [ShowDataUI() for _ in range(self.showMaxDataLenth)]
        nextIndex = 0
        for ui in self.dataUIList:
            ui.transform.Position += [330 + 100, Instance.windowSize[1] - (nextIndex + 2) * 70]
            ui.PositionUpdate()
            nextIndex += 1
            pass

        # 기본 UI 셋팅
        ButtonScale = 2

        self.popup_UI = UI()
        self.popup_UI.image = load_image("image/UI/Frame.png")
        self.popup_UI.image_type = [0, 0, 600, 600]
        self.popup_UI.transform.Position += Instance.windowSize // 2 + [160, 0]
        self.popup_UI.transform.Scale *= [2.1, 1.5]

        self.leftButton = Button(1)
        self.leftButton.image = load_image("image/UI/RankGraph/Left_Button.png")
        self.leftButton.image_type = [0,0,32,32]
        self.leftButton.frameCount = 0
        self.leftButton.transform.Scale *= ButtonScale
        self.leftButton.transform.Position += [Instance.windowSize[0] // 2 + 100 - (100 + self.leftButton.image_type[2]), self.leftButton.image_type[3] * ButtonScale]

        self.rightButton = Button(1)
        self.rightButton.image = load_image("image/UI/RankGraph/Right_Button.png")
        self.rightButton.image_type = [0,0,32,32]
        self.rightButton.frameCount = 0
        self.rightButton.transform.Scale *= ButtonScale
        self.rightButton.transform.Position += [Instance.windowSize[0] // 2 + 100 + (100 + self.rightButton.image_type[2]), self.rightButton.image_type[3] * ButtonScale]

        # Page를 표시해주는 Text
        self.pageText = Text(50)
        self.pageText.type = "Middle"
        self.pageText.text = str(self.pageIndex + 1) + " / " + str(self.maxPageIndex + 1)
        self.pageText.transform.Position += [Instance.windowSize[0] // 2 + 180, self.leftButton.image_type[3] * ButtonScale]

        # 함수 초기화
        self.ChangePage(0)

        UI.renderList.AddObject(self.popup_UI)
        pass

    def Handle_Event(self):
        if self.leftButton.isClick is True:
            self.leftButton.frameCount = 0
            self.ChangePage(self.pageIndex - 1)
            self.leftButton.isClick = False
        elif self.rightButton.isClick is True:
            self.rightButton.frameCount = 0
            self.ChangePage(self.pageIndex + 1)
            self.rightButton.isClick = False
        pass

    def ChangePage(self, index):
        if index < 0 or index > self.maxPageIndex: return

        self.pageIndex = index
        self.pageText.text = str(self.pageIndex + 1) + " / " + str(self.maxPageIndex + 1)

        nextIndex = index * self.showMaxDataLenth

        for ui in self.dataUIList:
            if index == self.maxPageIndex and self.lastPagePlayerCount <= nextIndex % 10:
                ui.TextInit()
                continue

            ui.playerNameText.text = self.pd.sheet.cell(row=nextIndex + 2, column=2).value
            ui.playTimeText.text = str(self.pd.sheet.cell(row=nextIndex + 2, column=3).value)
            ui.monsterDeathCountText.text = str(self.pd.sheet.cell(row=nextIndex + 2, column=4).value)
            ui.earnItemCountText.text = str(self.pd.sheet.cell(row=nextIndex + 2, column=5).value)

            ui.levelText.text = self.pd.sheet.cell(row=nextIndex + 2, column=8).value
            ui.speedText.text = str(self.pd.sheet.cell(row=nextIndex + 2, column=9).value)
            ui.maxLifeText.text = str(self.pd.sheet.cell(row=nextIndex + 2, column=10).value)
            ui.lifeText.text = str(self.pd.sheet.cell(row=nextIndex + 2, column=11).value)
            ui.scoreText.text = str(self.pd.sheet.cell(row=nextIndex + 2, column=12).value)
            nextIndex += 1

        pass

    pass