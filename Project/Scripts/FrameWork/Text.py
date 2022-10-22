from Scripts.FrameWork.Transform import *

class Text:
    def __init__(self, size = 20):
        # 객체 초기화
        self.transform = Transform()
        self.text = 'None'

        self.font = load_font('Font/Saenggeo_Jincheon.otf', size)
        self.color = (0, 0, 0)
        pass

    def __del__(self):
        pass
    pass