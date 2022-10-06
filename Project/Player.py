from Object import *

class Player(Object):
    def __init__(self):
        super(Player, self).__init__()
        self.image = load_image('image/player/Player.png')
        self.image_type = [0,0,46,70]
        self.idle = None

        self.speed = 5
        pass

    def Handle_Event(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                SetRunning(False)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                SetRunning(False)

            right = 0
            left = 1
            up = 2
            down = 3
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    self.idle = left
                if event.key == SDLK_RIGHT:
                    self.idle = right
                if event.key == SDLK_UP:
                    self.idle = up
                if event.key == SDLK_DOWN:
                    self.idle = down
                pass
            if event.type == SDL_KEYUP:
                self.idle = None
                pass

            pass
        self.UpdateHandle()

        pass

    def UpdateHandle(self):
        if self.idle == None:
            return

        right = 0
        left = 1
        up = 2
        down = 3
        if self.idle == left:
            self.transform.Position[0] -= self.speed
        if self.idle == right:
            self.transform.Position[0] += self.speed
        if self.idle == up:
            self.transform.Position[1] += self.speed
        if self.idle == down:
            self.transform.Position[1] -= self.speed

        pass

    pass