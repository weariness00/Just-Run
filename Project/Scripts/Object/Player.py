from Scripts.FrameWork.Object import *

class keyType(Enum):
    Left = 0
    Right = 1
    UP = 2
    Down = 3
    pass

class Player(Object):
    def __init__(self):
        super(Player, self).__init__()


        self.__speed = 450
        self.idle = dict()

        for key in keyType:
            self.idle[key] = False

        #Transform 초긱화
        self.transform.Scale *= 2

        #Collde 초기화
        self.collider = Collide()
        self.collider.object = self
        self.collider.InitTransform(self.transform)
        self.collider.Pivot = numpy.array([0,-23])
        self.collider.SetCollideBox(numpy.array([[20,10], [0,0]]))
        self.collider.tag = "Player"
        self.collider.isTrigger = True

        #Animation 초기화
        self.__defaultName = 'image/player/Player_'
        self.__sprite_Name = "Idle"
        self.__ani_Name = Instance.SetPngName(self.__defaultName, self.__sprite_Name)
        self.image = load_image(self.__ani_Name)
        self.image_type = [0,0,43,60]
        self.__ani_Frame = 7
        self.__ani_Count = 0;

        pass

    def __del__(self):
        pass

    def Update(self):
        self.Handle_Event()
        self.Movement()
        self.Animaiton()
        self.OnCollide()
        pass
    def Handle_Event(self):
        events = get_events()
        for event in events:

            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    self.idle[keyType.Left] = True
                    self.dir = 'None'
                    self.__sprite_Name = "Working"
                if event.key == SDLK_RIGHT:
                    self.idle[keyType.Right] = True
                    self.dir = 'h'
                    self.__sprite_Name = "Working"
                if event.key == SDLK_UP:
                    self.idle[keyType.UP] = True
                    self.__sprite_Name = "Working"
                if event.key == SDLK_DOWN:
                    self.idle[keyType.Down] = True
                    self.__sprite_Name = "Working"
                self.ChangeSprite()
                pass

            if event.type == SDL_KEYUP:
                if event.key == SDLK_LEFT:
                    self.idle[keyType.Left] = False
                    self.__sprite_Name = 'idle'
                if event.key == SDLK_RIGHT:
                    self.idle[keyType.Right] = False
                    self.__sprite_Name = 'idle'
                if event.key == SDLK_UP:
                    self.idle[keyType.UP] = False
                    self.__sprite_Name = 'idle'
                if event.key == SDLK_DOWN:
                    self.idle[keyType.Down] = False
                    self.__sprite_Name = 'idle'
                self.ChangeSprite()
                pass


            pass

        pass

    def Movement(self):
        movePos = numpy.array([0,0], dtype= float)

        if self.idle[keyType.Left]:
            movePos[0] -= self.__speed * Instance.FrameTime()
        if self.idle[keyType.Right]:
            movePos[0] += self.__speed * Instance.FrameTime()
        if self.idle[keyType.UP]:
            movePos[1] += self.__speed * Instance.FrameTime()
        if self.idle[keyType.Down]:
            movePos[1] -= self.__speed * Instance.FrameTime()

        self.transform.movePosition = movePos
        self.transform.Position += movePos
        pass

    def OnCollide(self):
        collides = self.collider.OnCollider()

        for collider in collides:
            if collider.tag == "Tile":
                print("충돌 TIle")

            pass
        pass

    def Animaiton(self):
        self.image_type[0] = (int(self.__ani_Count) % self.__ani_Frame) * self.image_type[2]
        self.__ani_Count += Instance.FrameTime() * 10

    def ChangeSprite(self):
        if self.__sprite_Name == "Working":
            self.image_type = [0, 0, 43, 60]
            self.__ani_Frame = 7
        elif self.__sprite_Name == "Idle":
            self.image_type = [0, 0, 40, 60]
            self.__ani_Frame = 6
        pass

        self.__ani_Name = Instance.SetPngName(self.__defaultName, self.__sprite_Name)
        self.image = load_image(self.__ani_Name)
        pass

    pass