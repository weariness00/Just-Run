from Scripts.Object.Item.ItemContain import *
from Scripts.Object.Monster.MonsterPool import *
from Scripts.Object.Skill.SkillContain import *

from Scripts.FrameWork.Render import Render
from Scripts.Object.GamePlay.PlayTimer import PlayTimer
from Scripts.Object.Player.Player import Player
from Scripts.Object.Skill.Skill import Skill
from Scripts.Object.Tile.EndlessTile import EndlessTile
from Scripts.Object.Player.Life import Life
from Scripts.FrameWork.Effect import Effect
from Scripts.UI.Number import Number

import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.GameOver_State as GameOver
import Scripts.State.GameWInner_State as GameWin


class GameManager(Object):
    uiRenderList = None

    def __init__(self):
        super(GameManager, self).__init__()
        self.bgm = load_music('Music/Background/GamePlayBGM_0' + random.randint(1,2).__str__() + '.mp3')
        self.bgm.set_volume(100)
        self.bgm.repeat_play()

        self.playTimer = PlayTimer()    # 게임 진행 시간

        self.item = Object()
        self.item.image = FireJewelry.image
        self.item.image_type = [0, 0, 32, 32]
        self.item.transform.Scale *= 2
        self.item.transform.Position += Instance.windowSize + [-200, -70]
        self.itemNumber = Number()
        self.itemNumber.transform.Scale *= 0.35
        self.itemNumber.transform.Position += Instance.windowSize + [-150, -70]
        self.itemNumber.ChangeNumber(12)
        GameManager.uiRenderList.AddObject(self.item)

        SkillContain()

        self.player = Player()
        Player.this = self.player
        Monster.target = self.player

        endlessTile = EndlessTile(self.player)

        # Monster Pool 객체 생성
        self.LimboPool = MonsterPool(Limbo(), 50, 5, 1)
        self.RedBatPool = MonsterPool(RedBat(), 10, 2, 3)
        self.WormPool = MonsterPool(Worm(), 5, 1, 5)

        # Player 초기화
        self.player.transform.Position = numpy.array([Instance.windowSize[0] // 2, Instance.windowSize[1] // 2], dtype=float)

        # Camera 초기화
        Camera.MainCamera = Camera(self.player.transform)
        Collide.MainCamera = Camera.MainCamera

        Skill.renderList.RendererObjectList.insert(0, self.player.skillBox)

        pass

    def __del__(self):
        super(GameManager, self).__del__()
        pass

    def Update(self):
        if Player.this.life <= 0:
            self.player.isActive = False
            game_framework.push_state(GameOver)


        pass

    def Handle_Event(self):
        for event in Object.events:
            if event.type == SDL_KEYDOWN:
                self.KeyDown(event.key)
            pass

    def KeyDown(self, key):
        if key == SDLK_EQUALS:
            self.playTimer.startTime -= 1
        elif key == SDLK_F2:
            if Player.this.life <= 0:
                return
            Player.this.life -= 1
            Player.this.lifeObject[Player.this.life].blueFireAni.count = Player.this.lifeObject[
                Player.this.life].redFireAni.count
            Player.this.lifeObject[Player.this.life].mainAnimation = Player.this.lifeObject[
                Player.this.life].blueFireAni
        elif key == SDLK_F3:
            if Player.this.life >= Player.this.maxLife:
                return

            Player.this.lifeObject[Player.this.life].redFireAni.count = Player.this.lifeObject[
                Player.this.life].blueFireAni.count
            Player.this.lifeObject[Player.this.life].mainAnimation = Player.this.lifeObject[Player.this.life].redFireAni
            Player.this.life += 1