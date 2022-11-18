from Scripts.FrameWork.Object import *
from Scripts.FrameWork.Animation import *
from Scripts.FrameWork.UI import UI

class SkillBox(Object):

    def __init__(self):
        super(SkillBox, self).__init__()
        # 객체 초기화
        self.image = load_image('image/UI/Skill/SkillBox.png')
        self.image_type = [0, 0, 96, 96]

        self.transform.Scale *= 1.2

        # Transform
        self.transform.Position += [Instance.windowSize[0]//2, 100]
        UI.renderList.AddObject(self, 1)
        pass

    def __del__(self):
        pass

    pass