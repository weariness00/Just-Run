from Scripts.FrameWork.Object import *


class Item(Object):
    renderList = None
    def __init__(self):
        super(Item, self).__init__()

        self.name = 'Item'

        Item.renderList.AddObject(self)
        pass

    def __del__(self):
        super(Item, self).__del__()
        pass

    def OnItem(self, position):
        self.isActive = True
        self.transform.Position = numpy.copy(position)

    pass