from Scripts.Afx import *

Instance.Init()
open_canvas(*Instance.windowSize)

import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.Lobby_State as lobby_state
import Scripts.State.LevelUp_State as test_State

load_image('image/FirePunch.png').draw_now(*Instance.windowSize // 2, *Instance.windowSize)
delay(1)

game_framework.run(lobby_state)
close_canvas()

#TODO 모든 Object가 자기가 다루는 시간을 관리 할 수 있게 Time 관련 클래스 생성
# 이유는 다른 씬에 넘어 갔다 올떄 객체가 가지고 있는 시간 관련 변수들을 업데이트 해줘야되서