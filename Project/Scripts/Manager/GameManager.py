from Scripts.FrameWork.Object import *
from Scripts.Object.Item.ItemContain import *
from Scripts.Object.GamePlay.PlayTimer import PlayTimer
from Scripts.UI.Number import Number


class GameManager(Object):
    uiRenderList = None

    def __init__(self):
        super(GameManager, self).__init__()
        self.playTimer = PlayTimer()    # 게임 진행 시간

        self.item = Object()
        self.item.image = FireJewelry.image
        self.item.image_type = [0, 0, 32, 32]
        self.item.transform.Scale *= 2
        self.item.transform.Position += Instance.windowSize + [-200, -70]
        self.itemNumber = Number()
        self.itemNumber.transform.Scale *= 0.5
        self.itemNumber.transform.Position += Instance.windowSize + [-100, -70]
        self.itemNumber.ChangeNumber(12)
        GameManager.uiRenderList.AddObject(self.item)

        pass

    def __del__(self):
        super(GameManager, self).__del__()
        pass

    def Update(self):

        pass