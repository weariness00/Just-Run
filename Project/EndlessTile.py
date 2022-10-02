from Afx import *


class TileType(Enum):
    glass_Default = Tile(load_image("image\Tile\snow-expansion.png"), (0, 208, 16, 16))
    pass


class EndlessTile:

    def __init__(self, Player=Object()):
        self.Player = Player

        self.maxViewDistance = 1000
        self.terrainSize = 100
        self.terrainVisibleInViewDistance = self.maxViewDistance // self.terrainSize

        self.terrainDictionary = {}
        self.LastUpdateTerrain = []
        self.VisibleTerrainList = None
        pass

    def UpdateVisibleTerrain(self):
        #현재 Active중인 타일 전부 False
        for obj in self.LastUpdateTerrain:
            obj.isActive = False
            pass
        self.LastUpdateTerrain = []

        currentTerrain_Pos = self.Player.transform.Position // self.terrainSize

        obj = None
        #Player의 위치를 반경으로 Tile 활성화
        for yOffset in range(-self.terrainVisibleInViewDistance, self.terrainVisibleInViewDistance):
            for xOffset in range(-self.terrainVisibleInViewDistance, self.terrainVisibleInViewDistance):
                viewedTerrainPos = currentTerrain_Pos + numpy.array([xOffset, yOffset])

                if self.terrainDictionary.get(viewedTerrainPos) is not None:
                    obj = self.terrainDictionary.get(viewedTerrainPos)
                    pass
                else:
                    self.terrainDictionary[viewedTerrainPos] = TileType.glass_Default
                    obj = self.terrainDictionary.get(viewedTerrainPos)
                    obj.transfrom.Position = viewedTerrainPos
                    pass
                obj.isActive = True
                self.LastUpdateTerrain.append(obj)
                pass
            pass
        pass

    pass
