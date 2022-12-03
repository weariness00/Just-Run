from Scripts.FrameWork.Render import *
from Scripts.FrameWork.UI import UI
from Scripts.PopUp.LevelUP_PopUp import *
import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.GamePlay_State as Game_State


# UI
ObjectRender = None
UIRender = None
TextRender = None

levelUp = None
backGround_UI = None
Skills_UI = None

def enter():
    global ObjectRender, UIRender, TextRender
    global levelUp, backGround_UI

    # Init
    Object.updateList = []

    # 객체 생성
    ObjectRender = Render()
    UIRender = Render()
    TextRender = Render()

    Object.objectRender = ObjectRender
    UI.renderList = UIRender
    Text.renderList = TextRender

    levelUp = LevelUP_PopUp()

    # BackGround 초기화
    backGround_UI = Object()
    backGround_UI.image = load_image('image/UI/PopUp/BackGround.png')
    backGround_UI.image_type = [0,0,1600,900]
    backGround_UI.transform.Position = Instance.windowSize//2
    UIRender.AddObject(backGround_UI)
    pass

# finalization code
def exit():
    global levelUp
    del levelUp
    pass

def handle_events():
    global levelUp

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif event.key == SDLK_DOWN:
                levelUp.count = (levelUp.count - 1) % 3
                levelUp.ChangeBoxColor('Red')
            elif event.key == SDLK_UP:
                levelUp.count = (levelUp.count + 1) % 3
                levelUp.ChangeBoxColor('Red')
            elif event.key == SDLK_RETURN:   # 현재 Enter의 값하고 달라서 디버그 돌려서 나온 key value를 임의로 넣어줌
                levelUp.ChangeSkill()
                game_framework.pop_state()
            pass
        pass
    pass


def update():
    for obj in Object.updateList:
        obj.Update()

    pass

def draw():
    global UIRender, ObjectRender, TextRender

    Game_State.draw()

    ObjectRender.Draw()

    UIRender.UIDraw()

    TextRender.TextDraw()

    pass

def pause():
    pass

def resume():
    pass