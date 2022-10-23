from Scripts.Afx import *
import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.Lobby_State as lobby_state
import Scripts.State.LevelUp_State as test_State

# TODO
#   Collide를 수정해 프레임 드랍을 획기적으로 줄였으나
#   충돌체크의 부자연스러움이 나타남

Instance.Init()
open_canvas(Instance.windowSize[0], Instance.windowSize[1])
game_framework.run(lobby_state)
close_canvas()