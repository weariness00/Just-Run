from Scripts.FrameWork.Object import *
from Scripts.Object.Player.Player import Player

class Item(Object):
    renderList = None
    def __init__(self):
        super(Item, self).__init__()
        self.isMoveMent = False

        self.name = 'Item'
        self.isActive = False

        # Collide
        self.collider = Collide()
        self.collider.tag = "Item"
        self.collider.object = self
        self.collider.InitTransform(self.transform)
        self.collider.SetCollideBox(numpy.array([[0, 0], [32, 32]]))

        Item.renderList.AddObject(self)
        pass

    def __del__(self):
        super(Item, self).__del__()
        pass

    def Enable(self):
        self.collider.isCollide = True
        self.isMoveMent = False
        pass

    def Update(self):
        self.MoveMent()
        pass

    def MoveMent(self):
        if self.isMoveMent is False:
            return

        self.transform.LooAtTarget(Player.this.transform, 500 * FrameTime.fTime)

        dis = Instance.Distance(Player.this.transform.Position, self.transform.Position)
        if  dis <= 10:
            self.SetActive(False)
        pass

    def OnItem(self, position):
        self.SetActive(True)
        self.transform.Position = numpy.copy(position)
    pass