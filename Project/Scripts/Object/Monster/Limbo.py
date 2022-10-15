from Scripts.Object.Monster.Monster import *

class Limbo(Monster):
    def __init__(self, target):
        # Objcet
        super(Limbo, self).__init__(target)
        self.name = 'Limbo'
        self.isActive = False

        # Transform
        self.transform.Scale = self.transform.Scale * 0.2

        # Animaiton
        self._defaultName = 'image/Monster/Limbo Monster/'
        self.ChangeSprite('Idle')

        self._speed = 300

        self._targetPlayer = target
        pass

    def __del__(self):
        pass

    def ChangeSprite(self, state):
        if state == "Idle":
            self._sprite_Name = 'Idle'
            self.image_type = [0, 0, 312, 269]
            self._ani_Frame = 2
        elif state == "Working":
            pass

        ani_Name = Instance.SetPngName(self._defaultName, self._sprite_Name)
        self.image = load_image(ani_Name)

    def Copy(self):
        return Limbo(self._targetPlayer)

    pass