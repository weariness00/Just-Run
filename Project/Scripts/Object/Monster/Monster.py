from Scripts.FrameWork.Object import *
from Scripts.FrameWork.Animation import *

class Monster(Object):
    HitSound = load_wav('Music/Monster/Hit/Default.wav')

    target = None
    renderList = None
    def __init__(self):
        super(Monster, self).__init__()
        self._speed = 0
        self.hitSound = Monster.HitSound
        self.hitSound.set_volume(30)

        self.isActive = False
        self.isMoveMent = True
        self.isDeath = False    # 현재 죽은 상태인지


        # Attack 관련 멤버
        self.attackSpeed = 5
        self.attackTimer = None
        self.attackRange = -1

        # 생명주기
        self.lifeTime = 10
        self.lifeStart = 0

        # Collider
        self.collider = Collide()
        self.collider.InitTransform(self.transform)
        self.collider.tag = "Monster"
        self.collider.object = self

        # Animaiton
        self.mainAnimation = None
        self.workingAni = Animation()
        self.attackAni = Animation()
        self.deathAni = Animation()

        # Attack Object
        self.attackObject = []

        # Timer
        self.deathStart = time.time()

        Monster.renderList.AddObject(self)
        pass

    def __del__(self):
        super(Monster, self).__del__()
        pass

    def Enable(self):

        pass

    def Disable(self):
        self.isDeath = False
        self.collider.isCollide = True
        self.isMoveMent = True
        # self.attackAni.count = 0
        # self.mainAnimation = self.workingAni
        pass

    def MoveMent(self):
        if self.isMoveMent is False:
            return

        distance = Instance.Distance(Monster.target.transform.Position, self.transform.Position)

        if self.attackRange >= 0:
            attackTime = time.time() - self.attackTimer
            if distance < self.attackRange:
                if attackTime < self.attackSpeed:
                    return
                self.mainAnimation = self.attackAni
                self.isMoveMent = False
                self.attackTimer = time.time()
                return

        realspeed = self._speed * FrameTime.fTime
        self.transform.LooAtTarget(Monster.target.transform, realspeed)
        pass

    def OnAnimation(self):
        self.mainAnimation.OnAnimation(FrameTime.fTime)

        self.image = self.mainAnimation.image
        self.image_type = self.mainAnimation.image_type

        if self.transform.direction[0] > 0:
            self.image_dir = 'None'
        elif self.transform.direction[0] < 0:
            self.image_dir = 'h'

        if self.isDeath is True and time.time() - self.deathStart > 1:
            self.SetActive(False)
        pass

    def CheckLifeTime(self):  # 생명주기 체크
        if self.collider.isCollide is False:
            return

        lTime = time.time() - self.lifeStart
        if lTime > self.lifeTime:
            self.collider.isCollide = False
            self.isMoveMent = False
            self.isDeath = True
            self.mainAnimation = self.deathAni
            self.deathStart = time.time()
            pass
        pass

    def OnCollide(self, collider):

        if collider.tag == "Player":
            self.collider.isCollide = False
            self.isMoveMent = False
            self.isDeath = True
            self.hitSound.play(1)
            self.mainAnimation = self.deathAni
            self.deathStart = time.time()
        elif collider.tag == 'Monster Attack':
            self.collider.isTrigger = False
        pass
    pass
