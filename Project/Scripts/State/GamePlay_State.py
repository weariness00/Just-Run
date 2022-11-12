from Scripts.Manager.GameManager import *


import Scripts.State.Lobby_State as lobby
import Scripts.State.LevelUp_State as LevelUp


# Timer
start = None
end = None

# Render
#   Object
TileRender = None
PlayerRender = None
MonsterRender = None
EffectRender = None
ItemRender = None

#   UI
uiRender = None
numberRender = None
LifeUIRender = None
SkillUIRender = None

# Objcet
gameManager = None

# Update List
ObjectUpdateList = None
UIUpdateList = None

# Render List
RenderUpdateList = None
UIRenderUpdateList = None

def enter():
    global start, end
    global TileRender, PlayerRender, MonsterRender, EffectRender, ItemRender
    global uiRender, LifeUIRender, SkillUIRender, numberRender
    global gameManager, player, endlessTile
    global monsterPools
    global ObjectUpdateList, UIUpdateList
    global RenderUpdateList, UIRenderUpdateList
    start = time.time()
    end = None

    # Init
    Collide.AllCollider = []
    ObjectUpdateList = []
    UIUpdateList = []

    Object.updateList = ObjectUpdateList

    # 객채 생성
    TileRender = Render()
    PlayerRender = Render()
    MonsterRender = Render()
    EffectRender = Render()
    ItemRender = Render()

    uiRender = Render()
    numberRender = Render()
    LifeUIRender = Render()
    SkillUIRender = Render()

    GameManager.uiRenderList = uiRender
    Player.renderList = PlayerRender
    Life.renderList = LifeUIRender
    Skill.renderList = SkillUIRender
    Number.renderList = numberRender

    EndlessTile.renderList = TileRender
    Effect.renderList = EffectRender
    Monster.renderList = MonsterRender
    Item.renderList = ItemRender

    gameManager = GameManager()


    # Render 초기화
    #   Object
    RenderUpdateList = [TileRender, PlayerRender, ItemRender, MonsterRender, EffectRender]

    UIRenderUpdateList = [uiRender, numberRender, LifeUIRender, SkillUIRender]
    pass

# finalization code
def exit():
    global gameManager
    global TileRender, PlayerRender, MonsterRender, EffectRender, ItemRender
    global uiRender, LifeUIRender, SkillUIRender, numberRender
    del gameManager.bgm
    del TileRender, PlayerRender, MonsterRender, EffectRender, ItemRender
    del uiRender, LifeUIRender, SkillUIRender, numberRender
    pass

def handle_events():
    global player, gameManager
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
    global ObjectUpdateList
    global endlessTile, monsterPools

    # Function Flow
    # 모든 Object의 Update 호출
    for obj in ObjectUpdateList:
        obj.Update()
    # 모든 Object의 OnCollider을 호출
    Collide.SortAllCollide()
    for obj in ObjectUpdateList:
        obj.OnCollide()
    # 모든 Object의 OnTrigger을 호출
    for collider in Collide.AllCollider:
        collider.OnTrigger()
    pass

def draw():
    global RenderUpdateList, UIRenderUpdateList
    for render in RenderUpdateList:
        render.Draw()

    for UIRender in UIRenderUpdateList:
        UIRender.UIDraw()

    Collide.AllBoxDraw()

    pass

def pause():
    global start
    start = time.time()
    pass

def resume():
    GameManager.uiRenderList = uiRender
    Player.renderList = PlayerRender
    Life.renderList = LifeUIRender
    Skill.renderList = SkillUIRender
    Number.renderList = numberRender

    EndlessTile.renderList = TileRender
    Effect.renderList = EffectRender
    Monster.renderList = MonsterRender
    Item.renderList = ItemRender

    difTime = time.time() - start
    for collider in Collide.AllCollider:
        if collider.tag == 'Monster':
            collider.object.lifeStart += difTime
        if collider.tag == "Player":
            collider.object.InitHandle()

    pass

