from Afx import *

w, h = windowSize[0], windowSize[1]
open_canvas(windowSize[0],windowSize[1])
clear_canvas()

Camera.MainCamera = Camera()
# MainCamera = Camera()
player = Player()
Camera.MainCamera.transform = player.transform
player.transform.Position = numpy.array([10,10])

player.name = "player"
player.transform.Position = numpy.array([w//2,h//2])

endlessTile = EndlessTile(player)
endlessTile.UpdateVisibleTerrain()

player.Draw()

update_canvas()

delay(1)
close_canvas()