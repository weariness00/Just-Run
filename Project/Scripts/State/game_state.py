from Scripts.EndlessTile import *
from Scripts.Object.Player import *
from Scripts.Object.Monster.MonsterPool import *
import Scripts.FrameWork.game_framework as game_framework

start = None
end = None

TileRender = None
PlayerRender = None
MonsterRender = None
player = None

endlessTile = None

monster = None

ObjectUpdateList = None
RenderUpdateList = None

def enter():
    global start, end
    global TileRender, PlayerRender, MonsterRender
    global player, monster
    global endlessTile
    global ObjectUpdateList, RenderUpdateList
    start = time.time()
    end = None


    TileRender = Renderer()
    PlayerRender = Renderer()
    MonsterRender = Renderer()

    player = Player()
    player.name = "player"
    player.transform.Position = numpy.array([Instance.windowSize[0] // 2, Instance.windowSize[1] // 2], dtype=float)
    PlayerRender.AddRenderObject(player)

    Camera.MainCamera.transform = player.transform
    Collide.MainCamera = Camera.MainCamera

    endlessTile = EndlessTile(player)
    endlessTile.render = TileRender

    monster = Monster(player)
    MonsterRender.AddRenderObject(monster)

    ObjectUpdateList = [player, monster]
    RenderUpdateList = [TileRender, PlayerRender, MonsterRender]
    pass

# finalization code
def exit():
    global start, end
    global TileRender, PlayerRender, MonsterRender
    global player, monster
    global endlessTile
    global ObjectUpdateList, RenderUpdateList
    del TileRender, PlayerRender, MonsterRender
    del ObjectUpdateList, RenderUpdateList
    del endlessTile
    del player, monster
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
    global start, end

    endlessTile.UpdateVisibleTerrain()

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


# Instance.SetStartTime()
# while Instance.GameRunning:
#     clear_canvas()
#     endlessTile.UpdateVisibleTerrain()
#
#     for obj in ObjectUpdateList:
#         obj.Update()
#         obj.OnCollide()
#         pass
#
#     for render in RenderUpdateList:
#         render.Update()
#
#     # Collide.AllBoxDraw()
#
#     update_canvas()
#     Instance.SetStartTime()
#     # end = time.time()
#     # if 1/144 - float(end - start) > 0:
#     #     delay(1/144 - float(end - start))
#     # start = time.time()
#     pass
#
# close_canvas()