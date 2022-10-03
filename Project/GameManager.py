import numpy.lib.format

from Afx import *

open_canvas()
clear_canvas()

endlessTile = EndlessTile()
endlessTile.UpdateVisibleTerrain()
update_canvas()

delay(1)
close_canvas()