from Scripts.Object.Monster.Monster import *

class MonsterPool():

    def __init__(self, monsterType, maxCount):
        self.type = monsterType
        self.maxCount = maxCount #Pool이 가지고 있는 최대 오브젝트 개수
        self.pool = []

        for i in range(maxCount):
            self.pool.append(self.type)
            pass

        print(self.pool)

        pass

    def __del__(self):
        pass

    pass