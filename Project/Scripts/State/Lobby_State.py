from Scripts.Afx import *
import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.GamePlay_State as game_state

lobby_image = None

def enter():
    global lobby_image
    lobby_image = load_image('image/FirePunch.png')

    pass

# finalization code
def exit():
    global lobby_image
    del lobby_image
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
                game_framework.change_state(game_state)
        pass
    pass


def update():

    pass

def draw():
    global lobby_image
    lobby_image.draw_now(Instance.windowSize[0]/2, Instance.windowSize[1]/2, Instance.windowSize[0], Instance.windowSize[1])

    pass

def pause():
    pass

def resume():
    pass

