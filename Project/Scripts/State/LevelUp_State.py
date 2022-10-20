from Scripts.FrameWork.Render import *
from Scripts.Object.PopUp.LevelUP_PopUp import *
import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.GamePlay_State as Game_State

# Render
levelUP_Render = None
UI_Render = None

# UI
levelUp_UI = None
backGround_UI = None

# Update List
UIUpdateList = None

# Render List
UIRenderUpdateList = None

def enter():
    global levelUP_Render, UI_Render
    global levelUp_UI, backGround_UI
    global UIUpdateList
    global UIRenderUpdateList

    # Init
    UIUpdateList = []
    UIRenderUpdateList = []

    # 객체 생성
    levelUP_Render = Render()
    UI_Render = Render()

    levelUp_UI = LevelUP_PopUp()

    # BackGround 초기화
    backGround_UI = Object()
    backGround_UI.image = load_image('image/UI/PopUp/BackGround.png')
    backGround_UI.image_type = [0,0,1600,900]
    backGround_UI.transform.Position = Instance.windowSize//2

    #Render 초기화
    levelUP_Render.RendererObjectList += levelUp_UI.boxObject
    UI_Render.RendererObjectList += [backGround_UI]


    # Update List 초기화
    UIUpdateList += [levelUp_UI]

    # Render List 초기화
    UIRenderUpdateList += [UI_Render, levelUP_Render]

    pass

# finalization code
def exit():
    global levelUP_Render
    global levelUp_UI
    del levelUp_UI
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()

        pass
    pass


def update():
    global levelUP_Render
    global levelUp_UI
    global UIUpdateList
    global UIRenderUpdateList

    for obj in UIUpdateList:
        obj.Update()

    pass

def draw():
    global levelUP_Render
    global levelUp_UI
    global UIUpdateList
    global UIRenderUpdateList

    Game_State.draw()

    for render in UIRenderUpdateList:
        render.UIDraw()
    pass

def pause():
    pass

def resume():
    pass