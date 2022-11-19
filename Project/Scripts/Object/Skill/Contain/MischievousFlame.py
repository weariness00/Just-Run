# 장난꾸러기 불꽃
from Scripts.UI.Text import Text
from Scripts.Object.Player.Player import *
from Scripts.FrameWork.LayCast import CircleLay

class FlameFlower(Object):
    idleImage = load_image('image/FlameFlower/Idle.png')
    workImage = load_image('image/FlameFlower/Work.png')
    def __init__(self):
        super(FlameFlower, self).__init__()
        self.isActive = False
        self.isMoveMent = True

        self.lifeTime = 5
        self.startTime = 0
        self.endTime = 0

        self.randomPosition = 0
        self.moveTime = 0
        self.speed = 0

        self.transform.Scale *= 0.25

        # LayCast
        self.circleLay = CircleLay(self.transform, 100)
        self.circleLay.name = "FlameFlower CircleLay"
        self.circleLay.SetActive(False)
        self.circleLay.cameraType = 'UI'

        # Animation
        self.idleAni = Animation()
        self.idleAni.image = FlameFlower.idleImage
        self.idleAni.image_type = [0,0,244,525]
        self.idleAni.frame = 4
        self.idleAni.countSpeed = 5

        self.workAni = Animation()
        self.workAni.image = FlameFlower.workImage
        self.workAni.image_type = [0,0,350,525]
        self.workAni.frame = 3
        self.workAni.countSpeed = 10

        self.image = self.workAni.image

        Object.renderList.AddObject(self, 1)
        pass

    def __del__(self):
        super(FlameFlower, self).__del__()
        pass

    def Enable(self):
        self.circleLay.SetActive(True)
        self.isMoveMent = True

        halfWindowSize = Instance.windowSize//2
        self.transform.Position = numpy.copy(Player.this.transform.Position)
        self.transform.Position[0] += random.randint(-halfWindowSize[0], halfWindowSize[0])
        self.transform.Position[1] += random.randint(-halfWindowSize[1], halfWindowSize[1])
        self._SetRandomPosition()
        self.startTime = time.time()
        pass

    def Update(self):
        if time.time() - self.endTime > 5:
            self.isMoveMent = True
            self.isDraw = True
            self.startTime = time.time()

        self.MoveMent()
        pass

    def MoveMent(self):
        if not self.isMoveMent:
            return

        if time.time() - self.startTime > self.lifeTime:
            self.isMoveMent = False
            self.isDraw = False
            self.endTime = time.time()
            return

        self.workAni.OnAnimation(FrameTime.fTime)
        self.image_type = self.workAni.image_type

        if abs(Player.this.transform.Position[0] - self.transform.Position[0]) > Instance.windowSize[0]//2:
            self._SetRandomPosition()
            self.speed = Player.this.speed + 300
        elif abs(Player.this.transform.Position[1] - self.transform.Position[1]) > Instance.windowSize[1]//2:
            self._SetRandomPosition()
            self.speed = Player.this.speed + 300

        self.transform.LooAtTarget(self.randomPosition, self.speed * FrameTime.fTime)

        if self.transform.direction[0] > 0:
            self.image_dir = 'h'
        elif self.transform.direction[0] < 0:
            self.image_dir = 'None'

        if time.time() - self.moveTime > 1:
            self._SetRandomPosition()
        pass

    def _SetRandomPosition(self):
        halfWindowSize = Instance.windowSize // 2
        self.randomPosition = numpy.copy(Player.this.transform.Position)+\
                              [random.randint(-halfWindowSize[0], halfWindowSize[0]),
                               random.randint(-halfWindowSize[1], halfWindowSize[1])]
        self.speed = random.randint(100, 500)
        self.moveTime = time.time()
        pass

    def OnCollide(self):
        if not self.circleLay.isActive:
            return

        # TODO Lay 충돌 미구현
        # UI 상태인 Lay의 충돌을 미구현
        colliderList = self.circleLay.OnLayCast()
        for collider in colliderList:
            if collider.tag == "Monster":
                collider.object.addSpeed = -collider.object.speed//2
        pass

    pass

class MischievousFlame(Skill):
    def __init__(self):
        super(MischievousFlame, self).__init__()
        # 객체 초기화
        self.skill_Type = 'Passive'
        self.coolTime = 10

        self.image = load_image('image/UI/Skill/MischievousFlame.png')
        self.image_type = [0, 0, 244, 525]

        # Transform
        self.transform.Scale *= 0.1

        # Text 초기화
        self.skillName = '[장난꾸러기 불꽃]'
        self.explain[0].text = 'level 만큼의 시간동안 제멋대로 움직이다가 사라지는 불꽃을 소환합니다.'
        self.explain.append(Text())
        self.explain[1].font = self.explain[1].fontList['Explain']
        self.explain[1].text = '불꽃에 닿는 몬스터는 이동속도가 50%만큼 느려집니다.'
        self.explain.append(Text())
        self.explain[2].font = self.explain[2].fontList['Explain']
        self.explain[2].text = '사라진 후 5초뒤 나타납니다. 최대 Level 5'

        # 능력 초기화
        self.flame = FlameFlower()
        pass

    def __del__(self):
        super(MischievousFlame, self).__del__()
        pass

    def OnSkill(self):
        super(MischievousFlame, self).OnSkill()
        self.flame.lifeTime = self.level * 5
        self.flame.SetActive(True)
        pass

    def LevelUp(self):
        super(MischievousFlame, self).LevelUp()
        if self.level >= 5:
            self.isMaxLevel = True
        pass

    pass