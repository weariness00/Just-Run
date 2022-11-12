from Scripts.FrameWork.Render import *
from Scripts.PopUp.LevelUP_PopUp import *
import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.GamePlay_State as Game_State

# Render
levelUP_Render = None
UI_Render = None
Text_Render = None

# UI
levelUp_UI = None
backGround_UI = None
Skills_UI = None

# Update List
UIUpdateList = None

# Render List
UIRenderUpdateList = None
TextRenderUpdateList = None

# Init Memeber

def enter():
    global levelUP_Render, UI_Render, Text_Render
    global levelUp_UI, backGround_UI, Skills_UI
    global UIUpdateList
    global UIRenderUpdateList, TextRenderUpdateList

    # Init Member

    # Init
    UIUpdateList = []
    UIRenderUpdateList = []
    TextRenderUpdateList = []

    # 객체 생성
    levelUP_Render = Render()
    UI_Render = Render()
    Text_Render = Render()
    Text.renderList = Text_Render

    levelUp_UI = LevelUP_PopUp()

    # BackGround 초기화
    backGround_UI = Object()
    backGround_UI.image = load_image('image/UI/PopUp/BackGround.png')
    backGround_UI.image_type = [0,0,1600,900]
    backGround_UI.transform.Position = Instance.windowSize//2

    #Render 초기화
    levelUP_Render.RendererObjectList += levelUp_UI.textBoxObject
    levelUP_Render.RendererObjectList += levelUp_UI.imageBoxObject
    levelUP_Render.RendererObjectList += levelUp_UI.boxImage
    UI_Render.RendererObjectList += [backGround_UI]

    # Text_Render.RendererObjectList += levelUp_UI.boxText[0]
    # Text_Render.RendererObjectList += levelUp_UI.boxText[1]

    # Update List 초기화
    UIUpdateList += [levelUp_UI]

    # Render List 초기화
    UIRenderUpdateList += [UI_Render, levelUP_Render]
    TextRenderUpdateList += [Text_Render]

    pass

# finalization code
def exit():
    global levelUP_Render
    global levelUp_UI
    del levelUp_UI
    pass

def handle_events():
    global count
    global levelUp_UI

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif event.key == SDLK_DOWN:
                levelUp_UI.count = (levelUp_UI.count - 1) % 3
                levelUp_UI.ChangeBoxColor('Red')
            elif event.key == SDLK_UP:
                levelUp_UI.count = (levelUp_UI.count + 1) % 3
                levelUp_UI.ChangeBoxColor('Red')
            elif event.key == SDLK_RETURN:   # 현재 Enter의 값하고 달라서 디버그 돌려서 나온 key value를 임의로 넣어줌
                levelUp_UI.ChangeSkill()
                game_framework.pop_state()
            pass
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
    global UIRenderUpdateList, TextRenderUpdateList

    Game_State.draw()

    for render in UIRenderUpdateList:
        render.UIDraw()

    for text in TextRenderUpdateList:
        text.TextDraw()
    pass

def pause():
    pass

def resume():
    pass