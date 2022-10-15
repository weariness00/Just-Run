from Afx import *
import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.game_state as game_state

# 플레이어의 애니메이션을 좀 더 자연스럽게 만들어야함
# 콜라이더의 충돌 Trigger 부분을 자연스럽게 만들어야함

Instance.Init()
Instance.SetStartTime()
open_canvas(Instance.windowSize[0], Instance.windowSize[1])
game_framework.run(game_state)
close_canvas()