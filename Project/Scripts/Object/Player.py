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
        self.image = load_image('image/player/Player.png')
        self.image_type = [0,0,46,70]

        self.__speed = 5
        self.idle = dict()

        for key in keyType:
            self.idle[key] = False

        #Transform 초긱화
        self.transform.Scale *= 2

        #Collde 초기화
        self.collider = Collide()
        self.collider.object = self
        self.collider.InitTransform(self.transform)
        self.collider.Pivot = numpy.array([0,-10])
        self.collider.SetCollideBox(numpy.array([[20,10], [0,0]]))
        self.collider.tag = "Player"

        pass

    def __del__(self):
        pass

    def Update(self):
        self.Handle_Event()
        self.Movement()
        pass
    def Handle_Event(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                Instance.SetRunning(False)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                Instance.SetRunning(False)

            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    self.idle[keyType.Left] = True
                if event.key == SDLK_RIGHT:
                    self.idle[keyType.Right] = True
                if event.key == SDLK_UP:
                    self.idle[keyType.UP] = True
                if event.key == SDLK_DOWN:
                    self.idle[keyType.Down] = True
                pass


            if event.type == SDL_KEYUP:
                if event.key == SDLK_LEFT:
                    self.idle[keyType.Left] = False
                if event.key == SDLK_RIGHT:
                    self.idle[keyType.Right] = False
                if event.key == SDLK_UP:
                    self.idle[keyType.UP] = False
                if event.key == SDLK_DOWN:
                    self.idle[keyType.Down] = False
                pass

            pass


        pass

    def Movement(self):

        movePos = numpy.array([0,0])

        if self.idle[keyType.Left]:
            movePos[0] -= 5
        if self.idle[keyType.Right]:
            movePos[0] += 5
        if self.idle[keyType.UP]:
            movePos[1] += 5
        if self.idle[keyType.Down]:
            movePos[1] -= 5

        self.transform.Position += movePos

        pass

    def OnCollide(self):
        collides = self.collider.OnCollider()

        for collider in collides:
            if collider.tag == "Tile":
                print("충돌 TIle")
                movePos = numpy.array([0, 0])
                if self.idle[keyType.Left]:
                    movePos[0] -= 5
                if self.idle[keyType.Right]:
                    movePos[0] += 5
                if self.idle[keyType.UP]:
                    movePos[1] += 5
                if self.idle[keyType.Down]:
                    movePos[1] -= 5

                print(collider.object.Info())

                # self.transform.Position -= movePos
            pass
        pass

    pass