from Scripts.Manager.GameManager import *


import Scripts.State.Lobby_State as lobby
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


def enter():
    global start, end
    global ObjectRender, uiRender, textRender
    global gameManager
    start = time.time()
    end = None

    # 객채 생성
    ObjectRender = Render()
    ObjectRender.name += " : Object - GamePlay"
    uiRender = Render()
    uiRender.name += " : ui - GamePlay"
    textRender = Render()
    textRender.name += " : Text - GamePlay"

    GameManager.uiRenderList = uiRender

    Player.renderList = ObjectRender
    EndlessTile.renderList = ObjectRender
    Effect.renderList = ObjectRender
    Monster.renderList = ObjectRender
    Item.renderList = ObjectRender

    Life.renderList = uiRender
    Skill.renderList = uiRender
    Number.renderList = uiRender
    Button.renderList = uiRender

    Text.renderList = textRender

    gameManager = GameManager()

    pass

# finalization code
def exit():
    global gameManager
    global ObjectRender, uiRender, textRender
    Object.AllObject.clear()
    Monster.AllMonster.clear()
    Collide.AllCollider.clear()
    Collide.AllColliderX.clear()
    Collide.AllColliderY.clear()

    gameManager.__del__()
    ObjectRender.__del__()
    uiRender.__del__()
    textRender.__del__()
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
                game_framework.quit()
            if event.key == SDLK_SPACE:
                game_framework.change_state(lobby)
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
    for obj in Object.AllObject:
        if obj.isActive is False:
            continue
        obj.Update()
    # 모든 Object의 OnCollider을 호출
    Collide.SortAllCollide()
    for obj in Object.AllObject:
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
    Player.renderList = ObjectRender
    EndlessTile.renderList = ObjectRender
    Effect.renderList = ObjectRender
    Monster.renderList = ObjectRender
    Item.renderList = ObjectRender

    Life.renderList = uiRender
    Skill.renderList = uiRender
    Number.renderList = uiRender

    difTime = time.time() - start
    for collider in Collide.AllCollider:
        if collider.tag == 'Monster':
            collider.object.lifeStart += difTime
        if collider.tag == "Player":
            collider.object.InitHandle()

    pass

