from Scripts.Afx import *
from Scripts.FrameWork.Object import Object
from Scripts.FrameWork.Animation import Animation
from Scripts.FrameWork.Render import Render
from Scripts.FrameWork.FrameTime import FrameTime

import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.GamePlay_State as Game_State
import Scripts.State.Lobby_State as Lobby_State

p = None
updateList = None
renderList = None

def enter():
    global p
    global render
    global updateList, renderList

    p = Object()
    p.transform.Position += [Instance.windowSize[0]//2, Instance.windowSize[1]//2]
    p.transform.Scale *= 2
    p.ani = Animation()
    p.ani.image = load_image('image/GameOver/Player_GameOver.png')
    p.ani.image_type = [0,0,40,60]
    p.ani.frame = 12
    p.ani.countSpeed = 5
    p.image = p.ani.image
    p.image_type = p.ani.image_type

    render = Render()
    render.AddObject(p)

    updateList = []
    renderList = []

    updateList.append(p)
    renderList += [render]
    pass

# finalization code
def exit():
    global render
    del render
    Game_State.exit()
    pass

def handle_events():
    events = get_events()
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
    global updateList

    if p.ani.count < p.ani.frame:
        p.ani.OnAnimation(FrameTime.fTime)
    for obj in updateList:
        obj.Update()
    pass

def draw():
    global renderList
    Game_State.draw()

    for obj in renderList:
        obj.UIDraw()
    pass

def pause():
    pass

def resume():
    pass

