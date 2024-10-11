from Scripts.Afx import *
from Scripts.FrameWork.Object import Object
from Scripts.FrameWork.UI import UI
from Scripts.UI.Text import Text
from Scripts.UI.Button import Button
from Scripts.FrameWork.Effect import Effect
from Scripts.FrameWork.Animation import Animation
from Scripts.FrameWork.Render import Render
from Scripts.FrameWork.FrameTime import FrameTime
from Scripts.UI.InputFiled import InputFiled


import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.Lobby_State as Lobby_State

from Data.PlayData import PlayData

# 객체
background = None
back_Button = None
nameInputFiled = None
# Render
objectRender = None
uiRender = None
textRender = None

#list
updateList = None

def enter():
    global background, back_Button, nameInputFiled
    global objectRender, uiRender, textRender
    global updateList


    # Render
    objectRender = Render()
    uiRender = Render()
    textRender = Render()

    Object.renderList = objectRender
    UI.renderList = uiRender
    Text.renderList = textRender

    # List
    updateList = []
    Object.updateList = updateList

    background = UI()
    background.image = load_image('image/GameWin/background.png')
    background.image_type = [0, 0, 1920, 1100]
    background.transform.Scale *= Instance.windowSize / [1920, 1100]
    background.transform.Position += Instance.windowSize//2

    window = UI()
    window.image = load_image('image/GameWin/Window.png')
    window.image_type = [0, 0, 235, 150]
    window.transform.Position += Instance.windowSize//2
    window.transform.Scale *= Instance.windowSize / [235, 150] / 1.3

    gameover = Text(50)
    gameover.font = gameover.fontList['Fire']
    gameover.text = 'GAME WiN'
    gameover.color = [0, 0, 0]
    gameover.transform.Position += Instance.windowSize//2 + [-140, 200]

    back_Button = Button(2)
    back_Button.transform.Scale *= 2
    back_Button.transform.Position += Instance.windowSize//2 + [0, -150]
    back_Button.text = Text(40)
    back_Button.text.text = '로비'
    back_Button.text.transform.Position += back_Button.transform.Position + [-40, 0]

    Score().OnScore()

    nameInputFiled = InputFiled(3)
    nameInputFiled.transform.Scale *= [3,2]
    nameInputFiled.transform.Position[0] = Instance.windowSize[0] // 2
    nameInputFiled.transform.Position[1] = nameInputFiled.image_type[3] + 30
    nameInputFiled.explainText.text = "이름을 입력해주세요."

    nameInputFiled.OnValueChangeCall.append(ValueChange)

    uiRender.AddObject(background)
    uiRender.AddObject(window, 1)
    pass

# finalization code
def exit():
    global objectRender, uiRender, textRender

    Object.updateList.clear()
    Object.AllObject.clear()

    objectRender.__del__()
    uiRender.__del__()
    textRender.__del__()

    pass

def handle_events():
    if back_Button.isClick is True:
        game_framework.change_state(Lobby_State)

    events = get_events()
    Object.events = events

    for obj in updateList:
        obj.Handle_Event()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            pass
    pass


def update():
    global updateList

    for obj in updateList:
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

class Score:
    def __init__(self):
        self.inputFiled = InputFiled()

        self.playTimeText = Text()
        self.killCountText = Text()
        self.earnItemCountText = Text()
        self.scoreText = Text(35)

        self.playTimeText.color = [0,0,0]
        self.killCountText.color = [0,0,0]
        self.earnItemCountText.color = [0,0,0]
        self.scoreText.color = [0,0,0]

        self.playTimeText.transform.Position += Instance.windowSize//2 + [-200, 100]
        self.killCountText.transform.Position += Instance.windowSize//2 + [-50, 100]
        self.earnItemCountText.transform.Position += Instance.windowSize//2 + [100, 100]
        self.scoreText.transform.Position += Instance.windowSize//2 + [-50, 0]
        pass

    def OnScore(self):
        pd = PlayData()
        pd.GetPlayData(self)
        pass
    pass

def ValueChange():
    global nameInputFiled
    pd = PlayData()
    nextIndex = pd.sheet["A1"].value - 1
    pd.sheet.cell(row=nextIndex + 2, column=2).value = nameInputFiled.Text.text
    pd.file.save('Data/PlayData.xlsx')
    pass

