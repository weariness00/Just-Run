import numpy

from Scripts.Object.Player.Life import *

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
        self.maxLife = 3
        self.life = self.maxLife
        self.__speed = 150
        self.idle = dict()
        self.events = []

        for key in keyType:
            self.idle[key] = False

        # Life 초기화
        self.lifeObject = [Life(numpy.array([100 * i + 50, Instance.windowSize[1] - 50], dtype=float)) for i in range(self.maxLife + 1)]

        #Transform 초긱화
        self.transform.Scale *= 2

        #Collde 초기화
        self.collider = Collide()
        self.collider.tag = "Player"
        self.collider.object = self
        self.collider.InitTransform(self.transform)
        self.collider.Pivot = numpy.array([0,-13], dtype= float)
        self.collider.SetCollideBox(numpy.array([[0,0],[15,32]]))
        self.collider.isTrigger = True

        #Animation 초기화
        self._defaultName = 'image/player/Player_'
        self.ChangeSprite('Idle')
        self._ani_Frame = 6
        self._ani_Count = 0

        pass

    def __del__(self):
        pass

    def Update(self):
        self.Handle_Event()
        self.Movement()
        self.Animaiton()
        self.OnCollide()
        self.time.start = time.time()
        pass
    def Handle_Event(self):
        state = None

        # events = get_events()
        for event in self.events:
            if event.type == SDL_KEYUP:
                if event.key == SDLK_LEFT:
                    self.idle[keyType.Left] = False
                    # state = 'Idle'
                if event.key == SDLK_RIGHT:
                    self.idle[keyType.Right] = False
                    # state = 'Idle'
                if event.key == SDLK_UP:
                    self.idle[keyType.UP] = False
                    # state = 'Idle'
                if event.key == SDLK_DOWN:
                    self.idle[keyType.Down] = False
                    # state = 'Idle'

                if any(self.idle.values()) == False:
                    self.ChangeSprite('Idle')
                else:
                    self.ChangeSprite(state)
                pass

            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    self.idle[keyType.Left] = True
                    self.dir = 'None'
                    state = "Working"
                if event.key == SDLK_RIGHT:
                    self.idle[keyType.Right] = True
                    self.dir = 'h'
                    state = "Working"
                if event.key == SDLK_UP:
                    self.idle[keyType.UP] = True
                    state = "Working"
                if event.key == SDLK_DOWN:
                    self.idle[keyType.Down] = True
                    state = "Working"
                self.ChangeSprite(state)
                pass

            pass
        pass

    def Movement(self):
        movePos = numpy.array([0,0], dtype= float)

        if self.idle[keyType.Left]:
            movePos[0] -= self.__speed * self.time.OneFrameTime()
        if self.idle[keyType.Right]:
            movePos[0] += self.__speed * self.time.OneFrameTime()
        if self.idle[keyType.UP]:
            movePos[1] += self.__speed * self.time.OneFrameTime()
        if self.idle[keyType.Down]:
            movePos[1] -= self.__speed * self.time.OneFrameTime()

        self.transform.movePos = movePos
        self.transform.Position += movePos
        pass

    def OnCollide(self):
        if self.isActive is False:
            return

        collides = self.collider.OnCollider()

        for collider in collides:
            if collider.tag == "Tile":
                collider.object.Info() # 체크용
            if collider.tag == "Monster":
                # 맞았을때 스프라이트 해주기
                pass


            pass
        pass

    def Animaiton(self):
        self.image_type[0] = (int(self._ani_Count) % self._ani_Frame) * self.image_type[2]
        self._ani_Count += self.time.OneFrameTime() * 10

    def ChangeSprite(self, state):
        if state == "Working":
            self._sprite_Name = 'Working'
            self.image_type = [0, 0, 43, 60]
            self._ani_Frame = 7
        elif state == "Idle":
            self._sprite_Name = 'Idle'
            self.image_type = [0, 0, 40, 60]
            self._ani_Frame = 6
        pass

        ani_Name = Instance.SetPngName(self._defaultName, self._sprite_Name)
        self.image = load_image(ani_Name)
        pass

    pass