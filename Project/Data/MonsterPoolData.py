from openpyxl import load_workbook
from Scripts.Object.Monster.MonsterPool import MonsterPool

class MonsterPoolData:
    def __init__(self):
        self.file = load_workbook("Data/MonsterPoolData.xlsx",data_only = True)
        self.sheet = self.file["Sheet1"]
        pass

    def __del__(self):
        pass

    def SetData(self, pools):
        maxPool = self.sheet["A2"].value
        for i in range(maxPool):
            num = str(i + 11)
            type = self.sheet["F" + num].value
            maxCount = self.sheet["G" + num].value
            sapwnCount = self.sheet["H" + num].value
            coolTime = self.sheet["I" + num].value
            pools.append(MonsterPool(type, maxCount, sapwnCount, coolTime))
            pass
        pass