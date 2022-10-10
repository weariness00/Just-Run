
from Scripts.Object.Object_Type import *
from Scripts.FrameWork.Renderer import *

#타입에 따른 타일 만들기
#Player 포지션에 따른 맵 생성 제대로 되게 하기

class EndlessTile:
    def __init__(self, Player=Object()):
        self.Player = Player

        self.maxViewDistance = 160 * 3
        self.terrainSize = 160

        self.terrainDictionary = dict()
        self.LastUpdateTerrain = []
        self.VisibleTerrainList = None
        self.render = None
        pass

    def UpdateVisibleTerrain(self):
        #현재 Active중인 타일 전부 False
        for obj in self.LastUpdateTerrain:
            obj.isActive = False
            pass
        self.LastUpdateTerrain = []

        currentTerrain_Pos = self.Player.transform.Position // self.terrainSize
        terrainVisibleInViewDistance = self.maxViewDistance // self.terrainSize

        #Player의 위치를 반경으로 Tile 활성화
        for yOffset in range(-terrainVisibleInViewDistance, terrainVisibleInViewDistance + 1):
            for xOffset in range(-terrainVisibleInViewDistance - 1, terrainVisibleInViewDistance + 2):
                pos = currentTerrain_Pos + numpy.array([xOffset, yOffset])
                viewedTerrainPos = (pos[0],pos[1])

                obj = self.terrainDictionary.get(viewedTerrainPos)
                if obj is not None:
                    pass
                else:
                    obj = Tile(load_image("image\Tile\snow-expansion.png"), (16 * 1, 208, 16, 16))
                    obj.transform.Position = pos * self.terrainSize
                    obj.tileSize = 16
                    obj.transform.Scale *= 10
                    obj.name = 'tile'

                    self.terrainDictionary[viewedTerrainPos] = obj
                    self.render.AddRenderObject(obj)

                    pass

                obj.isActive = True
                self.LastUpdateTerrain.append(obj)

                pass
            pass
        pass

    pass