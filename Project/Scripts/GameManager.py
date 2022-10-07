from Scripts.EndlessTile import *
from Scripts.Object.Player import *

w, h = windowSize[0], windowSize[1]
open_canvas(windowSize[0],windowSize[1])
clear_canvas()
TileRender = Renderer()
PlayerRender = Renderer()

player = Player()
player.name = "player"
player.transform.Position = numpy.array([w//2,h//2])
player.transform.Scale += 2
PlayerRender.AddRenderObject(player)

Camera.MainCamera.transform = player.transform

endlessTile = EndlessTile(player)
endlessTile.render = TileRender


while GameRunning:
    clear_canvas()
    endlessTile.UpdateVisibleTerrain()

    player.Handle_Event()

    TileRender.Update()
    PlayerRender.Update()

    update_canvas()
    delay(1/60)
    pass

close_canvas()