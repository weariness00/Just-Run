from Scripts.Object.Player.Skill.Skill import *


class LevelUP_PopUp(Object):

    def __init__(self):
        super(LevelUP_PopUp, self).__init__()
        # 객체 초기화

        # Box UI 초기화
        self.boxObject = [Object() for i in range(3)]
        for i, boxObj in enumerate(self.boxObject):
            boxObj.image = load_image('image/UI/PopUp/Yellow.png')
            boxObj.image_type = [0, 0, 24, 24]
            boxObj.transform.Position += [Instance.windowSize[0]//2, 150 * i + 300]
            boxObj.transform.Scale += [25, 5]
            pass

        pass

    def __del__(self):
        pass

    pass