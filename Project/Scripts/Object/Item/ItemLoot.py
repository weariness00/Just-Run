from Scripts.FrameWork.Object import *
from Scripts.Object.Item.ItemContain import *


class DropItem:

    def __init__(self):
        self.item = None
        self.probability = 0
        self.dropCount = [0,1] # 최소, 최대
        pass

    def __del__(self):
        pass

    def Drop(self, position):
        if random.randint(0, 100) > self.probability:
            return

        for i in range(random.randint(*self.dropCount)):
            item = self.item.Copy()
            item.transform.Position = numpy.copy(position)
            item.SetActive(True)

        pass
    pass


class LootTable:

    def __init__(self, transform):
        self.dropList = []
        self.transform = transform
        pass

    def __del__(self):
        pass

    def AddItem_Table(self, item, probability=0, dropCount=[0, 1]):
        item.isActive = False
        di = DropItem()
        di.item = item
        di.probability = probability
        di.dropCount = dropCount
        self.dropList.append(di)

    def Drop(self):

        for item in self.dropList:
            item.Drop(self.transform.Position)
            pass

        pass