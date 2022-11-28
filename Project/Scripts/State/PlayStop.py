from Scripts.Afx import *
from Scripts.FrameWork.Object import Object
from Scripts.FrameWork.Render import Render
from Scripts.FrameWork.UI import UI
from Scripts.UI.Text import Text
from Scripts.UI.Button import Button
import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.GamePlay_State as game_state
import Scripts.State.Lobby_State as Lobby

# Object
background = None

# Button
play_Button = None
exit_Button = None

# Render
ui_Render = None
text_Render = None

UpdateList = None

def enter():
    global background
    global play_Button, exit_Button
    global ui_Render, text_Render
    global UpdateList

    UpdateList = []
    Object.updateList = UpdateList

    ui_Render = Render()
    ui_Render.name += " : UI - Lobby"
    Button.renderList = ui_Render

    text_Render = Render()
    text_Render.name += " : Text - Lobby"
    Text.renderList = text_Render

    UI.renderList = ui_Render
    Text.renderList = text_Render

    backGround_UI = Object()
    backGround_UI.image = load_image('image/UI/PopUp/BackGround.png')
    backGround_UI.image_type = [0,0,1600,900]
    backGround_UI.transform.Position = Instance.windowSize//2
    ui_Render.AddObject(backGround_UI)

    ButtonInit()

    # 객체 초기화

# finalization code
def exit():
    global ui_Render, text_Render
    ui_Render.__del__()
    text_Render.__del__()
    pass

def handle_events():


    events = get_events()
    Object.events = events
    for obj in UpdateList:
        obj.Handle_Event()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.pop_state()
            game_state.exit()

        pass
    pass

def update():
    ButtonLogic()
    for obj in UpdateList:
        obj.Update()

    pass

def draw():

    game_state.draw()

    ui_Render.UIDraw()

    text_Render.TextDraw()

    pass

def pause():
    pass

def resume():
    pass

def ButtonLogic():
    if play_Button.isClick is True:
       game_framework.pop_state()
    elif exit_Button.isClick is True:
        game_state.exit()
        game_framework.change_state(Lobby)

    pass

def ButtonInit():
    global play_Button, exit_Button

    # Start
    play_Button = Button(1)
    play_Button.transform.Scale *= 2
    play_Button.transform.Position += [Instance.windowSize[0]//2, 400]
    play_Button.text = Text(40)
    play_Button.text.text = '계속'
    play_Button.text.transform.Position += play_Button.transform.Position + [-40, 0]

    # Exit
    exit_Button = Button(1)
    exit_Button.transform.Scale *= 2
    exit_Button.transform.Position += [Instance.windowSize[0]//2, 300]
    exit_Button.text = Text(40)
    exit_Button.text.text = '로비'
    exit_Button.text.transform.Position += exit_Button.transform.Position + [-40, 0]

    pass
