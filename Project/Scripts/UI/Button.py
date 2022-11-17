from Scripts.FrameWork.Object import *

class Button(Object):
    image = load_image('image/UI/Button.png')
    renderList = None
    def __init__(self, death=0):
        super(Button, self).__init__()
        self.isClick = False

        self.name = "Button"
        self.image = Button.image
        self.image_type = [0, 0, 167, 48]
        self.frameCount = 0

        Button.renderList.AddObject(self, death)
        pass

    def __del__(self):
        super(Button, self).__del__()
        pass

    def Update(self):
        self.Handle_Event()

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

    def OnMouse(self, event, dot):
        if event.type == SDL_MOUSEMOTION:
            x = event.x
            y = Instance.windowSize[1] - event.y
            if dot[0][0] <= x <= dot[1][0] and dot[0][1] <= y <= dot[1][1] and self.frameCount != 2:
                self.frameCount = 1
            elif self.frameCount != 2:
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
            else:
                self.frameCount = 0
        pass
    pass
