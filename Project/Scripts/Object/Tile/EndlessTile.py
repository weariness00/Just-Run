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
        pass


    def Update(self):
        self.UpdateVisibleTerrain()
        pass
    def UpdateVisibleTerrain(self):
        #현재 Active중인 타일 전부 False
        for obj in self.LastUpdateTerrain:
            obj.SetActive(False)
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
                    # obj = Tile(load_image("image\Tile\snow-expansion.png"), (16 * 1, 208, 16, 16))
                    obj = TileType(random.randint(TileTypeMin, TileTypeMax))
                    obj.transform.Position = pos * self.terrainSize
                    obj.tileSize = 16
                    obj.transform.Scale *= 10
                    obj.name = 'tile'

                    self.terrainDictionary[viewedTerrainPos] = obj
                    EndlessTile.renderList.AddObject(obj)
                    pass

                obj.SetActive(True)
                self.LastUpdateTerrain.append(obj)
                pass
            pass
        pass

    pass