import numpy
from Scripts.Object.Player.Life import *
from Scripts.FrameWork.Animation import *

class keyType(Enum):
    Left = 0
    Right = 1
    UP = 2
    Down = 3
    pass

class Player(Object):
    def __init__(self):
        super(Player, self).__init__()

        # 객체 초기화
        self.name = 'Player'
        self.maxLife = 3
        self.life = self.maxLife
        self.__speed = 150
        self.idle = dict()
        self.events = []

        for key in keyType:
            self.idle[key] = False

        # Life 초기화
        self.lifeObject = [Life([100 * i + 50, Instance.windowSize[1] - 50]) for i in range(self.maxLife + 1)]

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
            moveDir[0] -= self.__speed * self.time.OneFrameTime()
        if self.idle[keyType.Right]:
            moveDir[0] += self.__speed * self.time.OneFrameTime()
        if self.idle[keyType.UP]:
            moveDir[1] += self.__speed * self.time.OneFrameTime()
        if self.idle[keyType.Down]:
            moveDir[1] -= self.__speed * self.time.OneFrameTime()

        self.transform.direction = moveDir
        self.transform.Position += moveDir
        pass

    def OnCollide(self):
        if self.collider.isCollide is False:
            return

        self.collider.OnCollider()

        for collider in self.collider.onColliderList:
            if collider.tag == "Tile":
                pass
            if collider.tag == "Monster":
                # 맞았을때 스프라이트 해주기
                self.lifeObject[self.life].mainAnimation = self.lifeObject[self.life].blueFireAni
                if self.life > 0:
                    self.life -= 1
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