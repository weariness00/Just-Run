from Scripts.Object.Monster.RedBat import *
from Scripts.Object.Monster.Limbo import *
from Scripts.FrameWork.Camera import *

class MonsterPool():

    def __init__(self, monsterType, maxCount, coolTime=5):
        self.type = monsterType
        self.maxCount = maxCount #Pool이 가지고 있는 최대 오브젝트 개수
        self.pool = []
        self.coolTime = coolTime

        self.startTime = time.time()

        for i in range(maxCount):
            self.pool.append(self.type.Copy())

        pass

    def __del__(self):
        pass

    def Spawn(self, count): # count 만큼 pool에서 비활성화 된 Monster을 활성화
        for monster in self.pool:
            if count == 0:
                break
            if monster.isActive is True:
                continue

            monster.isActive = True
            monster.transform.Position = self.RandomSpawnPosition()
            monster.lifeTime = random.randint(5, 10 + 1)
            monster.lifeStart = time.time()
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