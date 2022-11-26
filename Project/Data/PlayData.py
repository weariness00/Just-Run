from openpyxl import load_workbook
from Scripts.Object.Monster.Monster import Monster
from Scripts.Object.Item.Item import Item

class PlayData:
    def __init__(self):
        self.file = load_workbook('Data/PlayData.xlsx')
        self.sheet = self.file["Sheet1"]
        for i in range(2, 7):
            self.sheet.cell(row = 2, column=i).value = 0
        self.file.save('Data/PlayData.xlsx')
        pass

    def __del__(self):
        pass

    def SetData(self, game):
        pass

    def GetData(self, game):
        self.sheet['B2'] = game.playTimer.nowTime
        self.sheet['C2'] = Monster.deathCount
        self.sheet['D2'] = Item.earnCount

        self.file.save('Data/PlayData.xlsx')
        pass

