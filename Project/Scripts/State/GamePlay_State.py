from Scripts.Manager.GameManager import *

import Scripts.State.PlayStop as Stop
import Scripts.State.Lobby_State as Lobby
import Scripts.State.LevelUp_State as LevelUp


# Timer
start = None
end = None

# Render
ObjectRender = None
uiRender = None
textRender = None

# Objcet
gameManager = None

# list
UpdateList = None


def enter():
    global start, end
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

    gameManager = GameManager()

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

    gameManager.__del__()
    ObjectRender.__del__()
    uiRender.__del__()
    textRender.__del__()
    Lay.RemoveAll()
    pass

def handle_events():
    global gameManager
    events = get_events()
    Object.events = events
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.push_state(Stop)
            if event.key == SDLK_SPACE:
                game_framework.change_state(Lobby)
            if event.key == SDLK_F1:
                game_framework.push_state(LevelUp)
            elif event.key == SDLK_F10:
                Player.this.SetActive(False)
                game_framework.push_state(GameOver)
            elif event.key == SDLK_F11:
                game_framework.change_state(GameWin)
        pass

    gameManager.Handle_Event()
    pass


def update():
    # Function Flow
    # 모든 Object의 Update 호출
    for obj in UpdateList:
        if obj.isActive is False:
            continue
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

def draw():
    ObjectRender.Draw()

    uiRender.UIDraw()

    Collide.AllBoxDraw()
    Lay.DrawLayCast()

    pass

def pause():
    global start
    start = time.time()
    pass

def resume():
    Object.updateList = UpdateList

    Object.renderList = ObjectRender
    UI.renderList = uiRender
    Text.renderList = textRender

    difTime = time.time() - start
    for collider in Collide.AllCollider:
        if collider.tag == 'Monster':
            collider.object.lifeStart += difTime
        if collider.tag == "Player":
            collider.object.InitHandle()

    pass

