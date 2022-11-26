from openpyxl import load_workbook

class LevelingData:
    def __init__(self, level):
        self.file = load_workbook('Data/LevelingData.xlsx', data_only = True)
        self.level = self.file[level]

        pass

    def __del__(self):
        pass

    def SetData(self, pools, level):
        maxLevel = self.level["F2"].value
        if maxLevel > level:
            level = maxLevel

        r = 22
        c = level * 3
        for pool in pools:
            pool.spawnCount += self.level.cell(row=r, column=c).value
            pool.coolTime += self.level.cell(row=r, column=c).value
            r += 1
            pass
        pass