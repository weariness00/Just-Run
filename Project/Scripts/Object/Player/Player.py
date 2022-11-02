from Scripts.Object.Player.Life import *
from Scripts.Object.Skill.SkillBox import *
from Scripts.Object.Skill.Skill import Skill

class keyType(Enum):
    Left = 0
    Right = 1
    UP = 2
    Down = 3
    pass


class Player(Object):
    this = None
    def __init__(self):
        super(Player, self).__init__()

        # 객체 초기화
        self.name = 'Player'
        self.maxLife = 3
        self.life = self.maxLife
        self.speed = 150
        self.idle = dict()
        self.events = []

        for key in keyType:
            self.idle[key] = False

        # Life 초기화
        self.lifeObject = [Life([100 * i + 50, Instance.windowSize[1] - 50]) for i in range(self.maxLife + 1)]

        # SKill
        self.skillBox = SkillBox()
        self.skill = Skill()

        #Transform 초긱화
        self.transform.Scale *= 2

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

        self.mainAnimation = self.idleAni
        pass

    def __del__(self):
        pass

    def Update(self):
        if self.isActive is False:
            return

        self.Handle_Event()
        self.Movement()
        self.OnAnimation()
        self.time.start = time.time()
        pass
    def Handle_Event(self):
        for event in self.events:
            self.skill.Handle_Event(event)

            if event.type == SDL_KEYUP:
                if event.key == SDLK_LEFT:
                    self.idle[keyType.Left] = False
                if event.key == SDLK_RIGHT:
                    self.idle[keyType.Right] = False
                if event.key == SDLK_UP:
                    self.idle[keyType.UP] = False
                if event.key == SDLK_DOWN:
                    self.idle[keyType.Down] = False

                if any(self.idle.values()) == False:
                    self.mainAnimation = self.idleAni
                else:
                    pass
                pass

            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    self.idle[keyType.Left] = True
                    self.image_dir = 'None'
                    self.mainAnimation = self.workingAni
                if event.key == SDLK_RIGHT:
                    self.idle[keyType.Right] = True
                    self.image_dir = 'h'
                    self.mainAnimation = self.workingAni
                if event.key == SDLK_UP:
                    self.idle[keyType.UP] = True
                    self.mainAnimation = self.workingAni
                if event.key == SDLK_DOWN:
                    self.idle[keyType.Down] = True
                    self.mainAnimation = self.workingAni
                pass

            pass
        pass

    def Movement(self):
        moveDir = numpy.array([0, 0], dtype= float)

        if self.idle[keyType.Left]:
            moveDir[0] -= self.speed * self.time.OneFrameTime()
        if self.idle[keyType.Right]:
            moveDir[0] += self.speed * self.time.OneFrameTime()
        if self.idle[keyType.UP]:
            moveDir[1] += self.speed * self.time.OneFrameTime()
        if self.idle[keyType.Down]:
            moveDir[1] -= self.speed * self.time.OneFrameTime()

        self.transform.direction = moveDir
        self.transform.Position += moveDir
        pass

    def OnCollide(self):
        if self.collider.isCollide is False:
            return

        onColliderList = self.collider.OnCollider()
        for collider in onColliderList:
            if collider.tag == "Tile":
                pass
            if collider.tag == "Monster":
                # 맞았을때 스프라이트 해주기
                self.lifeObject[self.life].mainAnimation = self.lifeObject[self.life].blueFireAni
                if self.life > 0:
                    self.life -= 1

                print("몬스터와 충돌 _ Player 클래스에")
                pass


            pass
        pass

    def OnAnimation(self):
        self.mainAnimation.OnAnimation(self.time.OneFrameTime())

        self.image = self.mainAnimation.image
        self.image_type = self.mainAnimation.image_type
        pass

    def InitHandle(self):
        for key in keyType:
            self.idle[key] = False
        pass

    pass