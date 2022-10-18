from Scripts.Object.Monster.Monster import *
from Scripts.Object.Monster.Limbo import *

class MonsterPool():

    def __init__(self, monsterType, maxCount, coolTime=5):
        self.type = monsterType
        self.maxCount = maxCount #Pool이 가지고 있는 최대 오브젝트 개수
        self.pool = []
        self.coolTime = coolTime

        for i in range(maxCount):
            self.pool.append(self.type.Copy())
            pass
        pass

    def __del__(self):
        pass

    def Spawn(self, count):
        for monster in self.pool:
            if count == 0:
                break
            if monster.isActive is True:
                continue

            monster.isActive = True
            monster.transform.Position -= 400
            count -= 1
            pass
        pass

    pass