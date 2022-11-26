from openpyxl import Workbook
from openpyxl import load_workbook

class PlayerData:
    def __init__(self):
        self.file = load_workbook("Data/Player.xlsx", data_only = True)
        self.sheet = self.file['Sheet1']

        pass

    def __del__(self):
        pass

    def SetDate(self, player, name="None"):
        if name == "None":
            name = self.sheet["B2"]
        for i in range(self.sheet["A2"].value):
            if self.sheet["B" + str(i + 10)].value == name:
                player.speed = self.sheet["E" + str(i + 10)].value
                player.maxLife = self.sheet["F" + str(i+10)].value
                player.life = self.sheet["G" + str(i+10)].value
                break
        pass
    pass