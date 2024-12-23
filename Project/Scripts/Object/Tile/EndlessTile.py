from Scripts.Object.Tile.Tile_Type import *
from Scripts.FrameWork.Render import *

#타입에 따른 타일 만들기
#Player 포지션에 따른 맵 생성 제대로 되게 하기

class EndlessTile(Object):
    renderList = None
    def __init__(self, Player):
        super(EndlessTile, self).__init__()
        self.Player = Player

        self.maxViewDistance = 160 * 4
        self.terrainSize = 160

        self.terrainDictionary = dict()
        self.LastUpdateTerrain = []
        self.VisibleTerrainList = None

        # Tile이 여러개 있는데 현재 index로 관리중이라 쓰는 임시 변수
        self.minType = 0
        self.maxType = 0
        # Tile의 지형 이름 index
        self.tileNameIndex = 0
        pass

    def __del__(self):
        super(EndlessTile, self).__del__()

        pass

    def Update(self):
        self.UpdateVisibleTerrain()
        pass
    def UpdateVisibleTerrain(self):
        #현재 Active중인 타일 전부 False
        for obj in self.LastUpdateTerrain:
            obj.SetActive(False)
            obj.changeTypeIndex(self.tileNameIndex)
            pass
        self.LastUpdateTerrain = []

        currentTerrain_Pos = self.Player.transform.Position // self.terrainSize
        terrainVisibleInViewDistance = self.maxViewDistance // self.terrainSize

        #Player의 위치를 반경으로 Tile 활성화
        for yOffset in range(-terrainVisibleInViewDistance, terrainVisibleInViewDistance + 1):
            for xOffset in range(-terrainVisibleInViewDistance - 1, terrainVisibleInViewDistance + 3):
                pos = currentTerrain_Pos + numpy.array([xOffset, yOffset])
                viewedTerrainPos = (pos[0],pos[1])

                obj = self.terrainDictionary.get(viewedTerrainPos)
                if obj is not None:
                    pass
                else:
                    obj = TileType(random.randint(self.minType, self.maxType), self.tileNameIndex)
                    obj.transform.Position = pos * self.terrainSize
                    obj.tileSize = 16
                    obj.transform.Scale *= self.terrainSize // obj.tileSize
                    obj.name = 'tile'

                    self.terrainDictionary[viewedTerrainPos] = obj
                    Object.renderList.AddObject(obj)
                    pass

                obj.SetActive(True)
                self.LastUpdateTerrain.append(obj)
                pass
            pass
        pass

    pass