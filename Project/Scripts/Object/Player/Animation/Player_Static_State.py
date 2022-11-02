from Scripts.Afx import *

null, RD, LD, UD, DD, RU, LU, UU, DU = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU
}


class Static_State:

    @staticmethod
    def enter(self, event):
        if event == RD:
            self.idle[0] = True
            self.image_dir = 'h'
        elif event == LD:
            self.idle[1] = True
            self.image_dir = 'None'
        elif event == UD:
            self.idle[2] = True
        elif event == DD:
            self.idle[3] = True
        # Key Up
        elif event == RU:
            self.idle[0] = False
        elif event == LU:
            self.idle[1] = False
        elif event == UU:
            self.idle[2] = False
        elif event == DU:
            self.idle[3] = False
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        moveDir = numpy.array([0, 0], dtype= float)
        realSpeed = self.speed + self.addSpeed

        if self.idle[0]:
            moveDir[0] += realSpeed * self.time.OneFrameTime()
        if self.idle[1]:
            moveDir[0] -= realSpeed * self.time.OneFrameTime()
        if self.idle[2]:
            moveDir[1] += realSpeed * self.time.OneFrameTime()
        if self.idle[3]:
            moveDir[1] -= realSpeed * self.time.OneFrameTime()

        self.transform.direction = moveDir
        self.transform.Position += moveDir
        pass

    @staticmethod
    def draw(self):
        pass

    pass
