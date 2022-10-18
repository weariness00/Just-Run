from Scripts.EndlessTile import *
from Scripts.Object.Player.Player import *
from Scripts.Object.Monster.MonsterPool import *
import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.Lobby_State as lobby

start = None
end = None
poolStartTime = None

TileRender = None
PlayerRender = None
MonsterRender = None
LifeUIRender = None

player = None
endlessTile = None

monsterPools = None

ObjectUpdateList = None
UIUpdateList = None

RenderUpdateList = None
UIRenderUpdateList = None

def enter():
    global start, end, poolStartTime
    global TileRender, PlayerRender, MonsterRender, LifeUIRender
    global player, monsterPools
    global endlessTile
    global ObjectUpdateList, UIUpdateList
    global RenderUpdateList, UIRenderUpdateList
    start = time.time()
    end = None

    # Init
    poolStartTime = time.time()
    Collide.AllCollider = []
    monsterPools = []
    ObjectUpdateList = []
    UIUpdateList = []

    # 객채 생성
    TileRender = Renderer()
    PlayerRender = Renderer()
    MonsterRender = Renderer()
    LifeUIRender = Renderer()
    player = Player()
    endlessTile = EndlessTile(player)
    monsterPools.append(MonsterPool(Limbo(player), 50, 0.1))

    # Player 초기화
    player.name = "player"
    player.transform.Position = numpy.array([Instance.windowSize[0] // 2, Instance.windowSize[1] // 2], dtype=float)

    # Camera 초기화
    Camera.MainCamera = Camera(player.transform)
    Collide.MainCamera = Camera.MainCamera

    # UpdateList 초기화
    ObjectUpdateList += [player]
    for mobPool in monsterPools:
        ObjectUpdateList += mobPool.pool

    UIUpdateList += player.lifeObject

    # Render 초기화
    endlessTile.render = TileRender
    PlayerRender.AddRenderObject(player)
    for mobPool in monsterPools:
        MonsterRender.RendererObjectList += mobPool.pool
    LifeUIRender.RendererObjectList += player.lifeObject
    RenderUpdateList = [TileRender, PlayerRender, MonsterRender]

    UIRenderUpdateList = [LifeUIRender]
    pass

# finalization code
def exit():
    global start, end
    global TileRender, PlayerRender, MonsterRender
    global player, monsterPools
    global endlessTile
    global ObjectUpdateList, RenderUpdateList
    del TileRender, PlayerRender, MonsterRender
    del ObjectUpdateList, RenderUpdateList
    del endlessTile
    del player, monsterPools
    del Collide.AllCollider
    pass

def handle_events():
    global player
    events = get_events()
    player.events = events
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_SPACE:
                game_framework.change_state(lobby)
        pass

    pass


def update():
    global ObjectUpdateList
    global start, end, poolStartTime
    global endlessTile, monsterPools

    endlessTile.UpdateVisibleTerrain()

    for monsterPool in monsterPools:
        flowTime = time.time() - poolStartTime
        if flowTime > monsterPool.coolTime:
            poolStartTime = time.time()
            monsterPool.Spawn(1)
        pass

    # Function Flow
    # 모든 Object의 Update 호출
    for obj in ObjectUpdateList:
        obj.Update()
    for ui in UIUpdateList:
        ui.Update()
    # 모든 Object의 OnCollider을 호출
    for obj in ObjectUpdateList:
        obj.OnCollide()
    # 모든 Object의 OnTrigger을 호출
    for obj in ObjectUpdateList:
        obj.collider.OnTrigger()

    # end = time.time()
    # if 1/144 - float(end - start) > 0:
    #     delay(1/144 - float(end - start))
    # start = time.time()

    pass

def draw():
    clear_canvas()
    global RenderUpdateList, UIRenderUpdateList
    for render in RenderUpdateList:
        render.Draw()

    for UIRender in UIRenderUpdateList:
        UIRender.UIDraw()

    Collide.AllBoxDraw()

    update_canvas()

    pass

def pause():
    pass

def resume():
    pass
