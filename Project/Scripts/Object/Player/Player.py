from Scripts.Object.Player.Life import *
from Scripts.Object.Skill.SkillBox import *
from Scripts.Object.Skill.Skill import Skill
from Scripts.Object.Player.Animation.PlayerAnimationController import *
from Scripts.Object.Player.Animation.Player_Static_State import key_event_table
from Scripts.FrameWork.LayCast import CircleLay

# Data
from Data.PlayerData import PlayerData

event_Name = ['null',
              'Right Key Down', 'Left Key Down', 'Up Key Down', 'Down Key Down',
              'Right Key Up', 'Left Key Up', 'Up Key Up', 'Down Key Up']

class Player(Object):
    this = None
    renderList = None
    def __init__(self, name='FlameSpirit'):
        super(Player, self).__init__()
        # 객체 초기화
        self.name = name
        self.maxLife = 0
        self.life = 0
        self.speed = 0
        data = PlayerData()
        data.SetDate(self, name)

        self.addSpeed = 0
        self.idle = dict()

        self.isGot = False
        self.gotTime = 0
        self.gotDurationTime = 0
        self.itemCount = 0

        for key in range(4):
            self.idle[key] = False

        # Life 초기화
        self.lifeObject = [Life([100 * i + 50, Instance.windowSize[1] - 50]) for i in range(self.maxLife)]
        for i in range(1, self.maxLife - self.life + 1):
            self.lifeObject[-i].mainAnimation = self.lifeObject[-i].blueFireAni

        # SKill
        self.skillBox = SkillBox()
        self.skill = Skill()

        #Transform 초긱화
        self.transform.Scale *= 2

        # Lay 초기화
        self.circleLay = CircleLay(self.transform, 100)

        #Collde 초기화
        self.collider = Collide()
        self.collider.tag = "Player"
        self.collider.object = self
        self.collider.InitTransform(self.transform)
        self.collider.Pivot += [0, -13]
        self.collider.SetCollideBox(numpy.array([[0,0],[15,32]]))
        self.collider.isTrigger = True

        # Animation 초기화
        self.idleAni = Animation()
        self.idleAni.image = load_image('image/player/Player_Idle.png')
        self.idleAni.image_type = [0, 0, 40, 60]
        self.idleAni.frame = 6
        self.idleAni.countSpeed = 5

        self.workingAni = Animation()
        self.workingAni.image = load_image('image/player/Player_Working.png')
        self.workingAni.image_type = [0, 0, 43, 60]
        self.workingAni.frame = 7
        self.workingAni.countSpeed = 10

        self.dashAni = Animation()
        self.dashAni.image = load_image('image/player/Player_Dash.png')
        self.dashAni.image_type = [0, 0, 22, 20]
        self.dashAni.frame = 5
        self.dashAni.countSpeed = 20

        self.mainAnimation = self.idleAni

        self.q = []
        self.cur_state = Player_Idle
        self.cur_state.enter(self, None)

        Object.renderList.AddObject(self, 3)
        pass

    def __del__(self):
        del self.idle
        del self.q
        self.idleAni.__del__()
        self.workingAni.__del__()
        pass

    def Resume(self):
        self.InitHandle()
        self.gotTime += FrameTime.diffTime
        pass

    def Update(self):
        self.Handle_Event()

        self.cur_state.do(self)
        if self.q:  # 리스트에 무언가 들어있으면
            event = self.q.pop()    # 이벤트 확인
            self.cur_state.exit(self)   # 현재 이벤트 탈출
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'Error: Boy_state {self.cur_state.__name__}, Event: {event_Name[event]}')
            self.cur_state.enter(self, event)  # 다음 이벤트 호출
            pass

        self.GodMode()
        self.OnAnimation()
        pass
    def Handle_Event(self):
        for event in Object.events.copy():
            self.skill.Handle_Event(event)

            if (event.type, event.key) in key_event_table:
                key_event = key_event_table[(event.type, event.key)]
                self.q.insert(0, key_event)

            pass
        pass

    def GodMode(self):  # 무적 상태 Update 구문
        if self.isGot is False:
            return

        gtime = time.time() - self.gotTime

        if self.gotDurationTime <= gtime:
            self.isGot = False
        pass

    def OnGotMode(self, duration = 1):
        self.isGot = True
        self.gotTime = time.time()
        self.gotDurationTime = duration
        pass

    def OnCollide(self):
        if self.collider.isCollide is False:
            return

        self.collider.isTrigger = True
        onColliderList = self.collider.OnCollider()
        for collider in onColliderList:
            if collider.tag == "Monster" or collider.tag == "Monster Attack":
                if self.isGot is True:
                    continue

                if self.life >= 0:
                    self.life -= 1
                # 맞았을때 스프라이트 해주기
                self.lifeObject[self.life].blueFireAni.count = self.lifeObject[self.life].redFireAni.count
                self.lifeObject[self.life].mainAnimation = self.lifeObject[self.life].blueFireAni

                self.OnGotMode()
                # if self.name == "Player Clone" and self.life <= 0:
                #     Object.updateList.remove(self)
                #     Object.renderList.RemoveObject(self)

                pass
            elif collider.tag == "Player":
                self.collider.isTrigger = False
            pass
        del onColliderList

        # Lay 충돌 처리
        if self.circleLay.isActive is False:
            return

        layColliderList = self.circleLay.OnLayCast()
        for collider in layColliderList:
            if collider.tag == 'Item':
                collider.object.isMoveMent = True
                collider.isCollide = False
        pass

    def OnAnimation(self):
        self.mainAnimation.OnAnimation(FrameTime.fTime)

        self.image = self.mainAnimation.image
        self.image_type = self.mainAnimation.image_type
        pass

    def InitHandle(self):
        for key in range(4):
            self.idle[key] = False
        pass

    pass