import numpy.lib.format

from Afx import *

open_canvas(800,600)
clear_canvas()

player = Object()
player.transform.Position = numpy.array([400,300])

endlessTile = EndlessTile(player)
endlessTile.UpdateVisibleTerrain()

update_canvas()

delay(1)
close_canvas()