from Scripts.FrameWork.UI import *
from Scripts.UI.Text import Text
from Scripts.FrameWork.Timer import Timer

class InputFiled(UI):
    image = load_image('image/UI/Button.png')

    exceptionKey = (None, SDLK_F1, SDLK_F2, SDLK_F3, SDLK_F4, SDLK_F5, SDLK_F6, SDLK_F7, SDLK_F8, SDLK_F9, SDLK_F10, SDLK_F11, SDLK_F12, \
                    SDLK_DELETE, SDLK_INSERT, SDLK_HOME, SDLK_END, SDLK_PAGEUP, SDLK_PAGEDOWN, SDLK_UP, SDLK_DOWN, \
                    SDLK_KP_0, SDLK_KP_1, SDLK_KP_2, SDLK_KP_3, SDLK_KP_4, SDLK_KP_5, SDLK_KP_6, SDLK_KP_7, SDLK_KP_8, SDLK_KP_9, \
                    SDLK_KP_PLUS, SDLK_KP_MINUS, SDLK_KP_AMPERSAND, SDLK_LCTRL, SDLK_LSHIFT, SDLK_LALT, SDLK_LGUI, SDLK_RCTRL, SDLK_RSHIFT, SDLK_RALT, SDLK_RGUI
                    )
    def __init__(self, death = 0):
        super(InputFiled, self).__init__()

        # filed의 Value가 바뀔때 호출
        self.OnTextChangeCall = []
        self.OnValueChangeCall = []

        # Text Filed 초기화
        self.Text = Text()
        self.Text.text = ""

        self.explainText = Text()
        self.explainText.font = self.explainText.fontList[Text.list[1]]
        self.explainText.type = "Middle"
        self.explainText.text = "입력해주세요."
        self.explainText.transform = self.transform

        self.isValueChange = False
        self.isClick = False
        self.mousePos = [0,0]

        self.name = "InputFiled"
        self.image = InputFiled.image
        self.image_type = [0, 0, 167, 48]
        self.frameCount = 3

        UI.renderList.AddObject(self, death)

        # text 커서 관련
        self.textCursorImage = TextCursor(death)
        self.textCursorImage.parentTransform = self.Text.transform
        self.textCursorImage.transform.Scale *= 0.3
        self.textCursorImage.textScale = self.Text.lineSpacing
        pass

    def __del__(self):
        pass

    def Update(self):
        if self.isClick is True:
            self.OnFiled()
            pass
        pass

    def EventCall(self):
        for action in self.OnTextChangeCall:
            action(self.Text.text)
        if self.isValueChange is True:
            for action in self.OnValueChangeCall:
                action()
        pass

    def Handle_Event(self):
        w = self.image_type[2] * self.transform.Scale[0] / 2
        h = self.image_type[3] * self.transform.Scale[1] / 2
        dot = [[self.transform.Position[0] - w, self.transform.Position[1] - h],
               [self.transform.Position[0] + w, self.transform.Position[1] + h]]
        for event in Object.events:
            self.ClickMouse(event, dot)
            pass
        pass

    def OnFiled(self):
        for event in Object.events:
            if event.type == SDL_KEYDOWN:
                if event.key in InputFiled.exceptionKey: return
                if event.key is SDLK_LEFT:
                    if self.textCursorImage.textIndex > 0:
                        self.textCursorImage.textIndex -= 1
                elif event.key is SDLK_RIGHT:
                    if len(self.Text.text) > self.textCursorImage.textIndex:
                        self.textCursorImage.textIndex += 1
                    pass
                elif event.key is SDLK_SPACE:
                    self.Text.text += ' '
                    self.textCursorImage.textIndex += 1
                    pass
                elif event.key is SDLK_BACKSPACE or event.key is SDLK_DELETE:
                    if len(self.Text.text) is 0: return
                    self.Text.text = self.Text.text[:-1]
                    self.textCursorImage.textIndex -= 1
                    pass
                elif event.key is SDLK_KP_ENTER or event.key is SDLK_RETURN:
                    self.isClick = False
                    self.textCursorImage.SetActive(False)
                    self.CheckExplainText()
                    pass
                else:
                    self.Text.text += chr(event.key)
                    self.textCursorImage.textIndex += 1
                    self.isValueChange = True
                    pass
                self.Text.transform.Position = self.transform.Position + [-self.image_type[2] * self.transform.Scale[0]// 2 + 100, 0]
                pass
        pass

    def ClickMouse(self, event, dot):
        if event.type == SDL_MOUSEBUTTONDOWN or event.type == SDL_MOUSEBUTTONUP:
            x = event.x
            y = Instance.windowSize[1] - event.y

        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT and \
                    dot[0][0] <= x <= dot[1][0] and dot[0][1] <= y <= dot[1][1]:
                self.isClick = True
                self.textCursorImage.SetActive(True)
                self.explainText.SetActive(False)
                pass
            else:
                self.isClick = False
                self.textCursorImage.SetActive(False)
                self.CheckExplainText()
                pass
        pass

    def CheckExplainText(self):
        if len(self.Text.text) == 0:
            self.explainText.SetActive(True)
        else:
            self.explainText.SetActive(False)

    pass

class TextCursor(UI):
    textCursorImage = load_image('image/UI/TextCursor.png')
    def __init__(self, death):
        super(TextCursor, self).__init__()
        self.image = TextCursor.textCursorImage
        self.image_type = [0, 0, 10, 100]

        self.timer = Timer()
        self.timer.Start()

        self.textScale = None
        self.textIndex = 0
        self.parentTransform = None
        self.frameCount = 0

        self.isActive = False

        UI.renderList.AddObject(self, death)
        pass

    def __del__(self):
        pass

    def Update(self):
        self.transform.Position = self.parentTransform.Position + [15 * self.textIndex, 0]

        if self.timer.Time() > 0.5:
            self.timer.Start()
            index = self.frameCount % 2
            self.image_type[0] = 10 * index
            self.frameCount += 1
        pass

    pass