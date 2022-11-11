from Scripts.Object.Tile.EndlessTile import *
from Scripts.Object.Monster.MonsterPool import *
from Scripts.Object.Skill.SkillContain import *
from Scripts.Object.Player.Player import *
from Scripts.UI.Number import Number
from Scripts.Object.Item.ItemContain import *

from Scripts.Manager.GameManager import GameManager

import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.Lobby_State as lobby
import Scripts.State.LevelUp_State as LevelUp
import Scripts.State.GameOver_State as GameOver

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

player = None
endlessTile = None

# pool & contain
monsterPools = None

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
    monsterPools = []
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

    SkillContain()

    gameManager = GameManager()
    player = Player()
    Player.this = player
    Monster.target = player

    endlessTile = EndlessTile(player)

    # Monster Pool 객체 생성
    monsterPools.append(MonsterPool(Limbo(), 50, 1))
    monsterPools.append(MonsterPool(RedBat(), 10, 1))

    # Player 초기화
    player.transform.Position = numpy.array([Instance.windowSize[0] // 2, Instance.windowSize[1] // 2], dtype=float)

    # Camera 초기화
    Camera.MainCamera = Camera(player.transform)
    Collide.MainCamera = Camera.MainCamera

    # Monster Pool 초기화
    for pool in monsterPools:
        pool.Spawn(5)

    # Render 초기화
    #   Object
    RenderUpdateList = [TileRender, PlayerRender, ItemRender, MonsterRender, EffectRender]

    #   UI
    LifeUIRender.RendererObjectList += player.lifeObject
    SkillUIRender.RendererObjectList.insert(0, player.skillBox)

    UIRenderUpdateList = [uiRender, numberRender, LifeUIRender, SkillUIRender]
    pass

# finalization code
def exit():
    global start, end
    global TileRender, PlayerRender, MonsterRender, EffectRender, ItemRender
    global uiRender, LifeUIRender, SkillUIRender, numberRender
    global ObjectUpdateList, UIUpdateList
    global RenderUpdateList, UIRenderUpdateList
    del TileRender, PlayerRender, MonsterRender, EffectRender, ItemRender
    del uiRender, LifeUIRender, SkillUIRender, numberRender
    del ObjectUpdateList, RenderUpdateList, UIUpdateList, UIRenderUpdateList
    pass

def handle_events():
    global player, gameManager
    events = get_events()
    Object.events = events
    gameManager.Handle_Event(events.copy())
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
            elif event.key == SDLK_F2:
                if Player.this.life <= 0:
                    continue
                Player.this.life -= 1
                Player.this.lifeObject[Player.this.life].blueFireAni.count = Player.this.lifeObject[Player.this.life].redFireAni.count
                Player.this.lifeObject[Player.this.life].mainAnimation = Player.this.lifeObject[Player.this.life].blueFireAni
            elif event.key == SDLK_F3:
                if Player.this.life >= Player.this.maxLife:
                    continue

                Player.this.lifeObject[Player.this.life].redFireAni.count = Player.this.lifeObject[Player.this.life].blueFireAni.count
                Player.this.lifeObject[Player.this.life].mainAnimation = Player.this.lifeObject[Player.this.life].redFireAni
                Player.this.life += 1
            elif event.key == SDLK_F10:
                player.isActive = False
                game_framework.push_state(GameOver)
        pass

    pass


def update():
    global ObjectUpdateList
    global start, end, poolStartTime
    global endlessTile, monsterPools

    if Player.this.life <= 0:
        player.isActive = False
        game_framework.push_state(GameOver)

    endlessTile.UpdateVisibleTerrain()

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
    difTime = time.time() - start
    for collider in Collide.AllCollider:
        if collider.tag == 'Monster':
            collider.object.lifeStart += difTime
        if collider.tag == "Player":
            collider.object.InitHandle()

    pass

