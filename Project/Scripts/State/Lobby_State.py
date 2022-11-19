from Scripts.Afx import *
from Scripts.FrameWork.UI import UI
from Scripts.FrameWork.Object import Object
from Scripts.FrameWork.Render import Render
from Scripts.UI.Button import Button
from Scripts.UI.Text import Text
import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.GamePlay_State as game_state

# Object
background = None

# Button
start_Button = None
exit_Button = None

# Render
ui_Render = None
text_Render = None

updateList = None

def enter():
    global background
    global start_Button, exit_Button
    global ui_Render, text_Render
    global updateList

    updateList = []
    Object.updateList = updateList

    ui_Render = Render()
    ui_Render.name += " : UI - Lobby"
    UI.renderList = ui_Render

    text_Render = Render()
    text_Render.name += " : Text - Lobby"
    Text.renderList = text_Render

    # 객체 초기화
    ButtonInit()

    frame = Object()
    frame.image = load_image('image/UI/Frame_White.png')
    frame.image_type = [0, 0, 600, 600]
    frame.transform.Position += Instance.windowSize/2
    frame.transform.Scale *= 1.2

    background = Object()
    background.image = load_image('image/Background/Forest.png')
    background.image_type = [0, 450, 1024, 450]
    background.transform.Position += Instance.windowSize/2
    background.transform.Scale *= Instance.windowSize / [background.image_type[2],background.image_type[3]]

    banner = Text(120)
    banner.text = '그냥 튀어!'
    banner.color = [62,62,62]
    banner.font = banner.fontList['Explain']
    banner.transform.Position = Instance.windowSize//2 + [-230, 200]
    subBanner = Text(40)
    subBanner.text = 'Just Run!'
    subBanner.color = [62,62,62]
    subBanner.transform.Position = banner.transform.Position + [130, -100]

    # Render 초기화

    ui_Render.AddObject(background, 0)
    ui_Render.AddObject(frame, 0)


    pass

# finalization code
def exit():
    global ui_Render, text_Render
    Object.AllObject.clear()
    Object.updateList.clear()

    ui_Render.__del__()
    text_Render.__del__()
    pass

def handle_events():
    ButtonLogic()

    events = get_events()
    Object.events = events
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        pass
    pass


def update():
    for obj in Object.updateList:
        obj.Update()

    pass

def draw():

    ui_Render.UIDraw()

    text_Render.TextDraw()

    pass

def pause():
    pass

def resume():
    pass

def ButtonLogic():
    if start_Button.isClick is True:
       game_framework.change_state(game_state)
    elif exit_Button.isClick is True:
        game_framework.quit()

    pass

def ButtonInit():
    global start_Button, exit_Button

    # Start
    start_Button = Button(1)
    start_Button.transform.Scale *= 2
    start_Button.transform.Position += [Instance.windowSize[0]//2, 300]
    start_Button.text = Text(40)
    start_Button.text.text = '시작'
    start_Button.text.transform.Position += start_Button.transform.Position + [-40, 0]

    # Exit
    exit_Button = Button(1)
    exit_Button.transform.Scale *= 2
    exit_Button.transform.Position += [Instance.windowSize[0]//2, 200]
    exit_Button.text = Text(40)
    exit_Button.text.text = '종료'
    exit_Button.text.transform.Position += exit_Button.transform.Position + [-40, 0]

    pass