from Scripts.FrameWork.Object import *
from Scripts.UI.Text import Text
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

        # Text
        self.name = Text(30)
        self.explain = [Text()]

        self.name.text = "None"
        self.explain[0].text = "None"

        Object.renderList.AddObject(self, 2)
        pass

    def __del__(self):
        self.collider.__del__()
        super(Item, self).__del__()
        pass

    def Enable(self):
        self.collider.isCollide = True
        self.isMoveMent = False
        pass

    def Disable(self):
        Object.renderList.RemoveObject(self)
        Player.this.itemCount += 1
        pass

    def Update(self):
        self.MoveMent()
        pass

    def MoveMent(self):
        if not self.isMoveMent:
            return

        self.transform.LooAtTarget(Player.this.transform.Position, 500 * FrameTime.fTime)

        dis = Instance.Distance(Player.this.transform.Position, self.transform.Position)
        if dis <= 10:
            self.SetActive(False)
        pass

    def OnItem(self, position):
        self.SetActive(True)
        self.transform.Position = numpy.copy(position)
    pass