from Scripts.Object.Monster.Monster import *
from Scripts.FrameWork.Camera import Camera

from Scripts.Object.Monster.Contain.AttackBall import AttackBall
from Scripts.Object.Monster.Contain.Limbo import Limbo
from Scripts.Object.Monster.Contain.RedBat import RedBat
from Scripts.Object.Monster.Contain.Worm import Worm

class MonsterPool(Object):

    def __init__(self, monsterType, maxCount = 0, spawnCount=0, coolTime=0):
        super(MonsterPool, self).__init__()
        self.name = "Pool : " + monsterType
        self.type = None
        self.maxCount = maxCount #Pool이 가지고 있는 최대 오브젝트 개수
        self.pool = []
        self.coolTime = coolTime
        self.spawnCount = spawnCount

        self.startTime = time.time()

        self.__Type(monsterType)

        pass

    def __del__(self):
        pass

    def Update(self):
        flowTime = time.time() - self.startTime
        if flowTime > self.coolTime:
            self.startTime = time.time()
            self.Spawn(self.spawnCount)

    def Spawn(self, count): # count 만큼 pool에서 비활성화 된 Monster을 활성화
        for monster in self.pool:
            if count == 0:
                break
            if monster.isActive is True:
                continue

            monster.SetActive(True)
            monster.transform.Position = self.RandomSpawnPosition()
            count -= 1
            pass
        pass

    def RandomSpawnPosition(self):  # Player 위치 기반으로 dis 거리만큼 랜덤한 Position에 스폰
        dis = 1000  # Player와 떨어질 거리
        setha = math.radians(random.randint(0, 360 + 1))
        position = [dis * math.cos(setha), dis * math.sin(setha)] + Camera.MainCamera.transform.Position
        return position
        pass

    def __Type(self, type):
        if type == "Limbo": self.type = Limbo()
        elif type == "RedBat": self.type = RedBat()
        elif type == "Worm":self.type = Worm()
        else: return

        for i in range(self.maxCount):
            self.pool.append(self.type.Copy())
        pass

    pass