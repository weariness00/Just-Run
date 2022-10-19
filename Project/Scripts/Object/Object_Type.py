from Scripts.Object.Tile import *
from Scripts.Object.Monster.Monster import *

TileTypeMin = 0
TileTypeMax = 3
def TileType(typeNumber):
    image = load_image("image\Tile\snow-expansion.png")
    image_type = [0, 208, 16, 16]
    if typeNumber == 0:
        return Tile(image, image_type)
    elif typeNumber == 1:
        image_type[0] = 16 * typeNumber
        tile = Tile(image, image_type, Collide())
        tile.collider.object = tile
        tile.collider.Pivot = numpy.array([6, -5])
        tile.collider.SetCollideBox(numpy.array([[4, 6], [0, 0]]))
        tile.collider.tag = "Tile"
        return tile
    elif typeNumber == 2:
        image_type[0] = 16 * typeNumber
        tile = Tile(image, image_type, Collide())
        tile.collider.object = tile
        tile.collider.Pivot = numpy.array([-6, -5])
        tile.collider.SetCollideBox(numpy.array([[4, 6], [0, 0]]))
        tile.collider.tag = "Tile"
        return tile
    elif typeNumber == 3:
        image_type[0] = 16 * typeNumber
        tile = Tile(image, image_type, Collide())
        tile.collider.object = tile
        tile.collider.Pivot = numpy.array([6, 7])
        tile.collider.SetCollideBox(numpy.array([[2, 2], [0, 0]]))
        tile.collider.tag = "Tile"
        return tile
    pass