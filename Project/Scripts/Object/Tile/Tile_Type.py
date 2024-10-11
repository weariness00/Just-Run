from Scripts.Object.Tile.Tile import *
from Scripts.Object.Monster.Monster import *

TileTypeMin = 0
TileTypeMax = 3


def TileType(typeNumber, imageIndex = 0):
    if imageIndex == 0:
        return PastureTile(typeNumber)
    elif imageIndex == 1:
        return SnowTile(typeNumber)
    pass

def PastureTile(typeNumber):
    image_type = [0, 208, 16, 16]

    if typeNumber == 0:
        return Tile(image_type)

    image_type[0] += 16 * typeNumber
    tile = Tile(image_type, Collide())
    tile.typeIndex = 0
    tile.collider.object = tile
    tile.collider.tag = "Tile"

    if typeNumber == 1:
        tile.collider.Pivot += [6, -5]
        tile.collider.SetCollideBox(numpy.array([[4, 6], [0, 0]]))
        pass
    elif typeNumber == 2:
        tile.collider.Pivot += [-6, -5]
        tile.collider.SetCollideBox(numpy.array([[4, 6], [0, 0]]))
        pass
    elif typeNumber == 3:
        tile.collider.Pivot += [6, 7]
        tile.collider.SetCollideBox(numpy.array([[2, 2], [0, 0]]))
        pass
    return tile
    pass

def SnowTile(typeNumber):
    image_type = [128, 208, 16, 16]

    if typeNumber == 0:
        return Tile(image_type)

    image_type[0] += 16 * typeNumber
    tile = Tile(image_type, Collide())
    tile.typeIndex = 1
    tile.collider.object = tile
    tile.collider.tag = "Tile"
    if typeNumber == 1:
        tile.collider.Pivot += [7, -6]
        tile.collider.SetCollideBox(numpy.array([[2, 6], [0, 0]]))
        pass
    elif typeNumber == 2:
        tile.collider.Pivot += [-6, -5]
        tile.collider.SetCollideBox(numpy.array([[4, 6], [0, 0]]))
        pass
    elif typeNumber == 3:
        tile.collider.Pivot += [7, 7]
        tile.collider.SetCollideBox(numpy.array([[2, 2], [0, 0]]))
        pass
    return tile
    pass