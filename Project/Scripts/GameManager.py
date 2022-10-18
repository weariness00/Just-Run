from Scripts.Afx import *
import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.Lobby_State as lobby
import Scripts.State.GamePlay_State as game_state

# TODO 프레임 드랍을 해결해야됨
# TODO 쓸데 없는 계산 비용을 낭비하는 코드를 찾아보기 <- 프레임 드랍 해결 부분

Instance.Init()
open_canvas(Instance.windowSize[0], Instance.windowSize[1])
game_framework.run(game_state)
close_canvas()