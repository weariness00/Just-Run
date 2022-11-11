from Scripts.Afx import *
from Scripts.FrameWork.Object import Object
from Scripts.UI.Button import Button
from Scripts.FrameWork.Render import Render
from Scripts.FrameWork.Text import Text
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

# Update List / Render List
objectUpdateList = None

uiRenderList = None
textRenderList = None

def enter():
    global background
    global start_Button, exit_Button
    global ui_Render, text_Render
    global objectUpdateList, uiRenderList, textRenderList

    # Init
    uiRenderList = []
    textRenderList = []
    objectUpdateList = []

    Object.updateList = objectUpdateList

    # 객체 초기화
    ButtonInit()

    background = Object()
    background.image = load_image('image/FirePunch.png')
    background.image_type = [0, 0, 32, 32]
    background.transform.Position += [Instance.windowSize[0]/2, Instance.windowSize[1]/2]
    background.transform.Scale += [Instance.windowSize[0]//32, Instance.windowSize[1]//32]

    # Render 초기화
    ui_Render = Render()
    ui_Render.RendererObjectList += [background, start_Button, exit_Button]

    text_Render = Render()
    text_Render.RendererObjectList += [start_Button.text, exit_Button.text]

    uiRenderList += [ui_Render]
    textRenderList += [text_Render]

    # List 초기화
    # objectUpdateList += [background, start_Button, exit_Button]

    pass

# finalization code
def exit():
    global background
    global start_Button, exit_Button
    global ui_Render
    global uiRenderList, objectUpdateList
    del background
    del ui_Render
    del uiRenderList, objectUpdateList
    pass

def handle_events():
    ButtonLogic()

    events = get_events()
    Object.events = events
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_SPACE:
                game_framework.change_state(game_state)
        pass
    pass


def update():
    for obj in objectUpdateList:
        obj.Update()
    pass

def draw():
    for ui in uiRenderList:
        ui.UIDraw()

    for text in textRenderList:
        text.TextDraw()

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
    start_Button = Button()
    start_Button.transform.Scale *= 2
    start_Button.transform.Position += [Instance.windowSize[0]//2- 300, 200]
    start_Button.text = Text(40)
    start_Button.text.text = '시작'
    start_Button.text.transform.Position += [Instance.windowSize[0]//2 - 340, 200]

    # Exit
    exit_Button = Button()
    exit_Button.transform.Scale *= 2
    exit_Button.transform.Position += [Instance.windowSize[0]//2 + 300, 200]
    exit_Button.text = Text(40)
    exit_Button.text.text = '종료'
    exit_Button.text.transform.Position += [Instance.windowSize[0]//2 + 260, 200]

    pass