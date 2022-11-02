from Scripts.Afx import *

Instance.Init()
open_canvas(Instance.windowSize[0], Instance.windowSize[1])

import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.Lobby_State as lobby_state
import Scripts.State.LevelUp_State as test_State

game_framework.run(lobby_state)
close_canvas()