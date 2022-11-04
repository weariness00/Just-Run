from Scripts.Afx import *
from Scripts.FrameWork.Object import Object
from Scripts.FrameWork.Animation import Animation
from Scripts.FrameWork.Render import Render

import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.GamePlay_State as Game_State
import Scripts.State.Lobby_State as Lobby_State

player = None
updateList = None
renderList = None

def enter():
    global player
    global updateList, renderList

    player = Object()
    player.transform.Position += [Instance.windowSize[0]//2, Instance.windowSize[1]//2]
    player.transform.Scale *= 2
    player.ani = Animation()
    player.ani.image = load_image('image/GameOver/Player_GameOver.png')
    player.ani.image_type = [0,0,40,60]
    player.ani.frame = 12
    player.ani.countSpeed = 10
    player.image = player.ani.image
    player.image_type = player.ani.image_type

    render = Render()
    render.AddRenderObject(player)

    updateList = []
    renderList = []

    updateList.append(player)
    renderList += [render]
    pass

# finalization code
def exit():
    global player
    del player
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

    player.ani.OnAnimation(player.time.OneFrameTime())
    player.time.start = time.time()
    for obj in updateList:
        obj.Update()
    pass

def draw():
    global renderList

    for obj in renderList:
        obj.UIDraw()
    pass

def pause():
    pass

def resume():
    pass

