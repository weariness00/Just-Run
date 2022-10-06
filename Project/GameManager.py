import Player
from EndlessTile import *
from Player import *



w, h = windowSize[0], windowSize[1]
open_canvas(windowSize[0],windowSize[1])
clear_canvas()

player = Player()
player.name = "player"
player.transform.Position = numpy.array([w//2,h//2])
player.transform.Scale += 2
Renderer.MainRender.P = player

Camera.MainCamera.transform = player.transform

endlessTile = EndlessTile(player)


while GameRunning:
    clear_canvas()
    endlessTile.UpdateVisibleTerrain()

    player.Handle_Event()
    # player.Draw()
    Renderer.MainRender.Update()

    update_canvas()
    delay(1/60)
    pass

close_canvas()