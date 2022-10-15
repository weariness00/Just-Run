from Afx import *
import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.game_state as game_state

Instance.Init()
Instance.SetStartTime()
open_canvas(Instance.windowSize[0], Instance.windowSize[1])
game_framework.run(game_state)
close_canvas()