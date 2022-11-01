from Scripts.EndlessTile import *
from Scripts.Object.Player.Player import *
from Scripts.Object.Monster.MonsterPool import *
from Scripts.Object.Player.Skill.SkillContain import *
import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.Lobby_State as lobby
import  Scripts.State.LevelUp_State as LevelUp

# Timer
start = None
end = None

# Render
#   Object
TileRender = None
PlayerRender = None
MonsterRender = None

#   UI
LifeUIRender = None
SkillUIRender = None

# Objcet
player = None
endlessTile = None

# pool
monsterPools = None

# Update List
ObjectUpdateList = None
UIUpdateList = None

# Render List
RenderUpdateList = None
UIRenderUpdateList = None

def enter():
    global start, end
    global TileRender, PlayerRender, MonsterRender, LifeUIRender, SkillUIRender
    global player, endlessTile
    global monsterPools
    global ObjectUpdateList, UIUpdateList
    global RenderUpdateList, UIRenderUpdateList
    start = time.time()
    end = None

    # Init
    Collide.AllCollider = []
    monsterPools = []
    ObjectUpdateList = []
    UIUpdateList = []

    # 객채 생성
    TileRender = Render()
    PlayerRender = Render()
    MonsterRender = Render()
    LifeUIRender = Render()
    SkillUIRender = Render()

    SkillContain()
    player = Player()
    Player.this = player

    endlessTile = EndlessTile(player)

    # Monster Pool 객체 생성
    monsterPools.append(MonsterPool(Limbo(player), 20, 1))
    monsterPools.append(MonsterPool(RedBat(player), 20, 1))

    # Player 초기화
    player.transform.Position = numpy.array([Instance.windowSize[0] // 2, Instance.windowSize[1] // 2], dtype=float)


    # Camera 초기화
    Camera.MainCamera = Camera(player.transform)
    Collide.MainCamera = Camera.MainCamera

    # Monster Pool 초기화
    for pool in monsterPools:
        pool.Spawn(5)

    # UpdateList 초기화
    ObjectUpdateList += [player]
    for mobPool in monsterPools:
        ObjectUpdateList += mobPool.pool

    for mobAttackObj in monsterPools:
        for pool in mobAttackObj.pool:
            ObjectUpdateList += pool.attackObject

    UIUpdateList += player.lifeObject
    UIUpdateList += [player.skillBox, player.skill]

    # Render 초기화
    #   Object
    endlessTile.render = TileRender
    PlayerRender.AddRenderObject(player)

    for mobPool in monsterPools:
        MonsterRender.RendererObjectList += mobPool.pool

    for mobAttackObj in monsterPools:
        for pool in mobAttackObj.pool:
            MonsterRender.RendererObjectList += pool.attackObject

    RenderUpdateList = [TileRender, PlayerRender, MonsterRender]

    #   UI
    LifeUIRender.RendererObjectList += player.lifeObject
    SkillUIRender.RendererObjectList += [player.skillBox, player.skill]

    UIRenderUpdateList = [LifeUIRender, SkillUIRender]
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
            if event.key == SDLK_F1: # 디버그용 key
                game_framework.push_state(LevelUp)
        pass

    pass


def update():
    global ObjectUpdateList
    global start, end, poolStartTime
    global endlessTile, monsterPools

    endlessTile.UpdateVisibleTerrain()

    for monsterPool in monsterPools:
        flowTime = time.time() - monsterPool.startTime
        if flowTime > monsterPool.coolTime:
            monsterPool.startTime = time.time()
            monsterPool.Spawn(5)
        pass

    # Function Flow
    # 모든 Object의 Update 호출
    for obj in ObjectUpdateList:
        obj.Update()
    for ui in UIUpdateList:
        ui.Update()
    # 모든 Object의 OnCollider을 호출
    Collide.SortAllCollide()
    for obj in ObjectUpdateList:
        obj.OnCollide()
    # 모든 Object의 OnTrigger을 호출
    for obj in ObjectUpdateList:
        obj.collider.OnTrigger()
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
    difTime = time.time() - start
    for obj in ObjectUpdateList:
        obj.time.start = time.time()
        if obj.collider.tag == 'Monster':
            obj.lifeStart += difTime
        if obj.name == "Player":
            obj.InitHandle()
    for ui in UIUpdateList:
        ui.time.start = time.time()

    pass


def ChagneSkillBox():
    global UIUpdateList
    global SkillUIRender

    UIUpdateList[-1] = Player.this.skill
    SkillUIRender.RendererObjectList[-1] = Player.this.skill
    pass

