from Scripts.Afx import *
from Scripts.FrameWork.Object import Object
from Scripts.FrameWork.Animation import Animation
from Scripts.FrameWork.Render import Render
from Scripts.FrameWork.FrameTime import FrameTime

import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.Lobby_State as Lobby_State


# 객체
background = None

# Render
objectRender = None
uiRender = None

#list
updateList = None
objectRenderList = None
uiRenderList = None


def enter():
    global background
    global objectRender, uiRender
    global updateList, objectRenderList, uiRenderList

    # Render
    objectRender = Render()
    uiRender = Render()

    # List
    updateList = []
    objectRenderList = []
    uiRenderList = []

    objectRenderList += [objectRender]
    uiRenderList += [uiRender]

    Object.updateList = updateList

    background = Object()
    background.image = load_image('background.png')
    background.image_type = [0, 0, 1920, 1100]
    background.transform.Scale *= Instance.windowSize / [1920, 1100]
    background.transform.Position += Instance.windowSize//2

    uiRender.AddObject(background)

    pass

# finalization code
def exit():

    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                game_framework.change_state(Lobby_State)
    pass


def update():
    global updateList

    for obj in updateList:
        obj.Update()
    pass

def draw():
    global objectRenderList, uiRenderList

    for obj in objectRenderList:
        obj.Draw()
    for obj in uiRenderList:
        obj.UIDraw()
    pass

def pause():
    pass

def resume():
    pass

