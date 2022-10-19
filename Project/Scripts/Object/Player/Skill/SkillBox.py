from Scripts.FrameWork.Object import *
from Scripts.FrameWork.Animation import *

class SkillBox(Object):

    def __init__(self):
        super(SkillBox, self).__init__()
        # 객체 초기화
        self.image = load_image('image/UI/Skill/SkillBox.png')
        self.image_type = [0, 0, 96, 96]

        # Transform
        self.transform.Position += [Instance.windowSize[0]//2, 100]

        pass

    def __del__(self):
        pass

    pass