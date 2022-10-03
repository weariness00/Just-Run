from Afx import *


class TileType(Enum):
    glass_Default = auto()
    pass


class EndlessTile:
    def __init__(self, Player=Object()):
        self.Player = Player

        self.maxViewDistance = 16 * 25
        self.terrainSize = 16

        self.terrainVisibleInViewDistance = self.maxViewDistance // self.terrainSize

        self.terrainDictionary = dict()
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
        print(currentTerrain_Pos)

        obj = None
        #Player의 위치를 반경으로 Tile 활성화
        for yOffset in range(-self.terrainVisibleInViewDistance, self.terrainVisibleInViewDistance):
            for xOffset in range(-self.terrainVisibleInViewDistance, self.terrainVisibleInViewDistance):
                pos = currentTerrain_Pos + numpy.array([xOffset, yOffset])
                viewedTerrainPos = (pos[0],pos[1])

                obj = self.terrainDictionary.get(viewedTerrainPos)
                if obj is not None:
                    pass
                else:
                    tile = Tile(load_image("image\Tile\snow-expansion.png"), (0, 208, 16, 16))
                    self.terrainDictionary[viewedTerrainPos] = tile
                    obj = self.terrainDictionary[viewedTerrainPos]
                    obj.transform.Position = pos
                    pass
                obj.isActive = True
                obj.tileSize = self.terrainSize
                self.LastUpdateTerrain.append(obj)
                obj.Draw()
                pass
            pass
        pass

    pass
