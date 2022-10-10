import numpy

from Scripts.EndlessTile import *
from Scripts.Object.Player import *
from Scripts.Object.Monster import *

Instance.Init()

open_canvas(Instance.windowSize[0],Instance.windowSize[1])
clear_canvas()

TileRender = Renderer()
PlayerRender = Renderer()
MonsterRender = Renderer()

player = Player()
player.name = "player"
player.transform.Position = numpy.array([Instance.windowSize[0]//2,Instance.windowSize[1]//2])
player.transform.Scale += 2
PlayerRender.AddRenderObject(player)

Camera.MainCamera.transform = player.transform

endlessTile = EndlessTile(player)
endlessTile.render = TileRender

monster = Monster(player)
MonsterRender.AddRenderObject(monster)

ObjectUpdateList = [player, monster]
RenderUpdateList = [TileRender, PlayerRender, MonsterRender]

while Instance.GameRunning:
    clear_canvas()
    endlessTile.UpdateVisibleTerrain()

    for obj in ObjectUpdateList:
        obj.Update()

    for render in RenderUpdateList:
        render.Update()

    update_canvas()
    delay(1/60)
    pass

close_canvas()