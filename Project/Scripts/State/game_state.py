from Scripts.EndlessTile import *
from Scripts.Object.Player import *
from Scripts.Object.Monster.MonsterPool import *
import Scripts.FrameWork.game_framework as game_framework

start = None
end = None
poolStartTime = None

TileRender = None
PlayerRender = None
MonsterRender = None
player = None

endlessTile = None

monsterPools = []

ObjectUpdateList = None
RenderUpdateList = None

def enter():
    global start, end, poolStartTime
    global TileRender, PlayerRender, MonsterRender
    global player, monsterPools
    global endlessTile
    global ObjectUpdateList, RenderUpdateList
    start = time.time()
    end = None
    poolStartTime = time.time()

    # 객채 생성
    TileRender = Renderer()
    PlayerRender = Renderer()
    MonsterRender = Renderer()
    player = Player()
    endlessTile = EndlessTile(player)

    # Player 초기화
    player.name = "player"
    player.transform.Position = numpy.array([Instance.windowSize[0] // 2, Instance.windowSize[1] // 2], dtype=float)
    PlayerRender.AddRenderObject(player)

    # Camera 초기화
    Camera.MainCamera.transform = player.transform
    Collide.MainCamera = Camera.MainCamera

    # Render 초기화
    endlessTile.render = TileRender
    monsterPools.append(MonsterPool(Limbo(player), 20, 5))
    for mobPool in monsterPools:
        MonsterRender.RendererObjectList += mobPool.pool
    RenderUpdateList = [TileRender, PlayerRender, MonsterRender]

    # UpdateList 초기화
    ObjectUpdateList = [player]
    for mobPool in monsterPools:
        ObjectUpdateList += mobPool.pool
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
    pass

def handle_events():
    # events = get_events()
    # for event in events:
    #     if event.type == SDL_QUIT:
    #         game_framework.quit()
    #     pass
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

    for obj in ObjectUpdateList:
        obj.Update()
        pass

    # end = time.time()
    # if 1/144 - float(end - start) > 0:
    #     delay(1/144 - float(end - start))
    # start = time.time()

    pass

def draw():
    clear_canvas()
    global RenderUpdateList
    for render in RenderUpdateList:
        render.Update()

    Collide.AllBoxDraw()

    update_canvas()
    Instance.SetStartTime()
    pass

def pause():
    pass

def resume():
    pass

