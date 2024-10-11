from Scripts.Manager.GameManager import *

import Scripts.State.PlayStop as Stop
import Scripts.State.GameWInner_State as GameWin
import Scripts.State.LevelUp_State as LevelUp

state = None

# Timer
start = None
end = None
isDrawColliderBox = None

# Render
ObjectRender = None
uiRender = None
textRender = None

# Objcet
gameManager = None
level = None

# list
UpdateList = None


def enter():
    global start, end, isDrawColliderBox
    global ObjectRender, uiRender, textRender
    global gameManager
    global UpdateList
    start = time.time()
    end = None

    # 객채 생성
    UpdateList = []
    Object.updateList = UpdateList

    ObjectRender = Render()
    ObjectRender.name += " : Object - GamePlay"
    uiRender = Render()
    uiRender.name += " : ui - GamePlay"
    textRender = Render()
    textRender.name += " : Text - GamePlay"

    Object.renderList = ObjectRender
    UI.renderList = uiRender
    Text.renderList = textRender

    Life.renderList = uiRender
    Life.updateList = UpdateList

    gameManager = GameManager(level)

    pass

# finalization code
def exit():
    global gameManager,UpdateList
    global ObjectRender, uiRender, textRender
    Object.AllObject.clear()
    UpdateList.clear()
    Monster.AllMonster.clear()
    Collide.AllCollider.clear()
    Collide.AllColliderX.clear()
    Collide.AllColliderY.clear()
    SkillContain.array.clear()

    gameManager.bgm.stop()
    gameManager.__del__()
    ObjectRender.__del__()
    uiRender.__del__()
    textRender.__del__()
    Lay.RemoveAll()
    pass

def handle_events():
    global gameManager, isDrawColliderBox
    events = get_events()
    Object.events = events
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.push_state(Stop)
            if event.key == SDLK_F1:
                game_framework.push_state(LevelUp)
            elif event.key == SDLK_F10:
                Player.this.SetActive(False)
                gameManager.playData.GetData(gameManager)
                game_framework.push_state(GameOver)
            elif event.key == SDLK_F11:
                gameManager.playData.GetData(gameManager)
                game_framework.change_state(GameWin)
            elif event.key == SDLK_DELETE:
                isDrawColliderBox = not isDrawColliderBox
        pass

    gameManager.Handle_Event()
    pass


def update():
    global state
    # Function Flow
    # 모든 Object의 Update 호출
    for obj in UpdateList.copy():
        if obj.isActive is False:
            continue
        if state is "Pause":
            state = "None"
            return
        obj.Update()
    # 모든 Object의 OnCollider을 호출
    Collide.SortAllCollide()
    for obj in UpdateList:
        obj.OnCollide()
    # 모든 Object의 OnTrigger을 호출
    for collider in Collide.AllCollider:
        if collider.isTrigger is False:
            continue
        collider.OnTrigger()
    pass

def event_update():
    for obj in Object.updateList:
        obj.EventCall()
    pass

def draw():
    ObjectRender.Draw()

    uiRender.UIDraw()

    if isDrawColliderBox:
        Collide.AllBoxDraw()
        Lay.DrawLayCast()

    pass

def pause():
    global start, state
    start = time.time()
    state = "Pause"
    pass

def resume():
    Object.updateList = UpdateList

    Object.renderList = ObjectRender
    UI.renderList = uiRender
    Text.renderList = textRender

    FrameTime.diffTime = time.time() - start
    for obj in UpdateList:
        obj.Resume()

    # gameManager.playTimer.startTime += difTime
    # Player.this.skill.onSkillTime += difTime
    # for collider in Collide.AllCollider:
    #     if collider.tag == 'Monster':
    #         collider.object.lifeStart += difTime
    #     if collider.tag == "Player":
    #         collider.object.InitHandle()

    pass

