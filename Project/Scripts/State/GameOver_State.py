from Scripts.Afx import *
from Scripts.FrameWork.Object import Object
from Scripts.FrameWork.Animation import Animation
from Scripts.FrameWork.Render import Render
from Scripts.FrameWork.FrameTime import FrameTime
from Scripts.FrameWork.UI import UI
from Scripts.UI.Text import Text
from Scripts.UI.Button import Button

import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.GamePlay_State as Game_State
import Scripts.State.Lobby_State as Lobby_State

p = None
back_Button = None

objectRender = None
uiRender = None
textRender = None



def enter():
    global p, back_Button
    global objectRender, uiRender, textRender
    Game_State.gameManager.bgm.stop()

    Object.updateList = []

    objectRender = Render()
    objectRender.name += " : Object - GameOver"
    uiRender = Render()
    uiRender.name += " : UI - GameOver"
    textRender = Render()
    textRender.name += " : Text - GameOver"

    Object.renderList = objectRender
    UI.renderList = uiRender
    Text.renderList = textRender

    p = Object()
    p.transform.Position += Instance.windowSize//2
    p.transform.Scale *= 2
    p.ani = Animation()
    p.ani.image = load_image('image/GameOver/Player_GameOver.png')
    p.ani.image_type = [0,0,40,60]
    p.ani.frame = 12
    p.ani.countSpeed = 5
    p.image = p.ani.image
    p.image_type = p.ani.image_type

    gameover = Text(200)
    gameover.font = gameover.fontList['Stone_Head']
    gameover.text = 'GAME OVER'
    gameover.color = [255,0,0]
    gameover.transform.Position += Instance.windowSize//2 + [-420, 100]

    back_Button = Button(1)
    back_Button.transform.Scale *= 2
    back_Button.transform.Position += Instance.windowSize//2 + [0, -150]
    back_Button.text = Text(40)
    back_Button.text.text = '로비'
    back_Button.text.transform.Position += back_Button.transform.Position + [-40, 0]

    backGround_UI = UI()
    backGround_UI.image = load_image('image/UI/PopUp/BackGround.png')
    backGround_UI.image_type = [0,0,1600,900]
    backGround_UI.transform.Position = Instance.windowSize//2
    uiRender.AddObject(backGround_UI)

    uiRender.AddObject(p)
    pass

# finalization code
def exit():
    Object.updateList.clear()
    objectRender.__del__()
    uiRender.__del__()
    textRender.__del__()

    Game_State.exit()
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
                game_framework.quit()
            if event.key == SDLK_SPACE:
                game_framework.change_state(Lobby_State)
        pass
    pass


def update():
    if back_Button.isClick is True:
        game_framework.change_state(Lobby_State)
    if p.ani.count < p.ani.frame:
        p.ani.OnAnimation(FrameTime.fTime)
    for obj in Object.updateList:
        obj.Update()
    pass

def event_update():
    for obj in Object.updateList:
        obj.EventCall()
    pass

def draw():
    Game_State.draw()

    objectRender.Draw()
    uiRender.UIDraw()
    textRender.TextDraw()

    pass

def pause():
    pass

def resume():
    pass

