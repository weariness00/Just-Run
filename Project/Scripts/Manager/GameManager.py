from Scripts.Object.Item.ItemContain import *
from Scripts.Object.Monster.MonsterPool import *
from Scripts.Object.Skill.SkillContain import *
from Scripts.FrameWork.LayCast import Lay

from Scripts.FrameWork.Render import Render
from Scripts.Object.GamePlay.PlayTimer import PlayTimer
from Scripts.Object.Player.Player import Player
from Scripts.Object.Skill.Skill import Skill
from Scripts.Object.Tile.EndlessTile import EndlessTile
from Scripts.Object.Player.Life import Life
from Scripts.FrameWork.Effect import Effect
from Scripts.FrameWork.UI import UI
from Scripts.UI.Number import Number
from Scripts.UI.Text import Text
from Scripts.UI.Button import Button

import Scripts.FrameWork.game_framework as game_framework
import Scripts.State.GameOver_State as GameOver
import Scripts.State.GameWInner_State as GameWinner

from Data.PlayData import PlayData
from Data.LevelingData import LevelingData

class GameManager(Object):
    def __init__(self, level = 'Easy'):
        super(GameManager, self).__init__()
        self.bgm = load_music('Music/Background/GamePlayBGM_0' + random.randint(1,2).__str__() + '.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

        self.playTimer = PlayTimer()    # 게임 진행 시간

        # Item 관련 임시 변수들
        self.item = Object()
        self.item.image = FireJewelry.image
        self.item.image_type = [0, 0, 32, 32]
        self.item.transform.Scale *= 2
        self.item.transform.Position += Instance.windowSize + [-200, -70]
        self.itemNumber = Number()
        self.itemNumber.transform.Scale *= 0.35
        self.itemNumber.transform.Position += Instance.windowSize + [-150, -70]
        self.itemNumber.ChangeNumber(0)
        UI.renderList.AddObject(self.item)

        # Player
        self.player = Player('FlameSpirit_' + level)
        self.player.transform.Position = numpy.array([Instance.windowSize[0] // 2, Instance.windowSize[1] // 2], dtype=float)
        Player.this = self.player
        Monster.target = self.player

        self.skillContain = SkillContain()

        self.endlessTile = EndlessTile(self.player)

        # Monster Pool 객체 생성
        self.pools = []

        # Data 셋팅
        Monster.deathCount = 0
        Item.earnCount = 0
        self.playData = PlayData()
        self.levelData = LevelingData(level)
        self.levelData.SetDefaultPoolData(self.pools)
        self.levelData.SetTimeData(self.playTimer)
        self.levelData.SetTileData(self.endlessTile)

        # Camera 초기화
        Camera.MainCamera = Camera(self.player.transform)
        Collide.MainCamera = Camera.MainCamera

        UI.renderList.AddObject(self.player.skillBox, 0)

        pass

    def __del__(self):
        # self.bgm.stop()
        pass

    def Update(self):
        if self.playTimer.isLevelUp:
            self.playTimer.isLevelUp = False
            self.levelData.SetPoolData(self.pools, self.playTimer.levelUpCount)

        if Player.this.life <= 0:
            self.playData.GetData(self)
            self.player.isActive = False
            game_framework.push_state(GameOver)
        elif self.playTimer.isWin is True:
            self.playData.GetData(self)
            game_framework.change_state(GameWinner)

        self.itemNumber.ChangeNumber(Player.this.itemCount)

        pass

    def Handle_Event(self):
        for event in Object.events:
            if event.type == SDL_KEYDOWN:
                self.KeyDown(event.key)
            pass

    def KeyDown(self, key):
        if key == SDLK_EQUALS:
            self.playTimer.startTime -= 10
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