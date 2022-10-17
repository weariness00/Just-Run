from Scripts.Afx import *
import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.GamePlay_State as Game_State
import Scripts.State.Lobby_State as Lobby_State


def enter():

    pass

# finalization code
def exit():

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

    pass

def draw():
    clear_canvas()

    update_canvas()
    pass

def pause():
    pass

def resume():
    pass

