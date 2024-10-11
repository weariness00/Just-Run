from Scripts.FrameWork.UI import *

class Button(UI):
    image = load_image('image/UI/Button.png')

    clickSound = load_wav('Music/Button/Click.wav')
    onMouseSound = load_wav('Music/Button/OnMouse.wav')
    def __init__(self, death=0):
        super(Button, self).__init__()
        self.OnValueChange = []

        self.isClick = False
        self.isOnMouse = False
        self.mousePos = [0,0]

        self.name = "Button"
        self.image = Button.image
        self.image_type = [0, 0, 167, 48]
        self.frameCount = 0

        UI.renderList.AddObject(self, death)
        pass

    def __del__(self):
        super(Button, self).__del__()
        pass

    def Update(self):
        self.image_type[0] = self.image_type[2] * self.frameCount
        pass

    def Handle_Event(self):
        w = self.image_type[2] * self.transform.Scale[0] / 2
        h = self.image_type[3] * self.transform.Scale[1] / 2
        dot = [[self.transform.Position[0] - w, self.transform.Position[1] - h],
               [self.transform.Position[0] + w, self.transform.Position[1] + h]]
        for event in Object.events:
            self.OnMouse(event, dot)
            self.ClickMouse(event, dot)
            pass
        pass

    def EventCall(self):
        for action in self.OnValueChange:
            action()
        pass

    def OnMouse(self, event, dot):
        if event.type == SDL_MOUSEMOTION:
            x = event.x
            y = Instance.windowSize[1] - event.y
            if dot[0][0] <= x <= dot[1][0] and dot[0][1] <= y <= dot[1][1] and self.frameCount != 2:
                if not self.isOnMouse:
                    Button.onMouseSound.set_volume(10)
                    Button.onMouseSound.play()
                self.isOnMouse = True
                self.frameCount = 1
                self.mousePos = numpy.array([x,y], dtype=float)
            elif self.frameCount != 2:
                self.isOnMouse = False
                self.frameCount = 0
        pass
    pass

    def ClickMouse(self, event, dot):
        if event.type == SDL_MOUSEBUTTONDOWN or event.type == SDL_MOUSEBUTTONUP:
            x = event.x
            y = Instance.windowSize[1] - event.y

        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT and \
                    dot[0][0] <= x <= dot[1][0] and dot[0][1] <= y <= dot[1][1]:
                self.frameCount = 2
        elif event.type == SDL_MOUSEBUTTONUP:
            if event.button == SDL_BUTTON_LEFT and \
                    dot[0][0] <= x <= dot[1][0] and dot[0][1] <= y <= dot[1][1]:
                self.isClick = True
                Button.clickSound.set_volume(10)
                Button.clickSound.play()
            else:
                self.frameCount = 0
        pass
    pass
