from Scripts.Object.Monster.Monster import *
from Scripts.Object.Monster.RedBat import RedBat
from Scripts.Object.Monster.Limbo import Limbo
from Scripts.Object.Monster.Worm import Worm
from Scripts.FrameWork.Camera import Camera

class MonsterPool(Object):

    def __init__(self, monsterType, maxCount, spawnCount=5, coolTime=5):
        super(MonsterPool, self).__init__()
        self.type = monsterType
        self.maxCount = maxCount #Pool이 가지고 있는 최대 오브젝트 개수
        self.pool = []
        self.coolTime = coolTime
        self.spawnCount = spawnCount

        self.startTime = time.time()

        self.name = 'Monster Pool'

        for i in range(maxCount):
            self.pool.append(self.type.Copy())

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

    pass