from Scripts.Object.Monster.Monster import *

class AttackBall(Monster):

    def __init__(self, target):
        super(AttackBall, self).__init__(target)

        self.image = load_image('image/Monster/RedBat Monster/Ball_Red.png')
        self.image_type = [0, 0, 32, 32]
        self.isActive = False
        self.isMoveMent = False
        self._speed = 90

        self.collider.SetCollideBox(numpy.array([[0,0],[6,6]]))
        self.collider.tag = 'Monster Attack'
        pass

    def __del__(self):
        super(AttackBall, self).__del__()
        pass

    def Update(self):
        if self.isActive is False:
            return

        super(AttackBall, self).MoveMent()
        super(AttackBall, self).CheckLifeTime()
        self.time.start = time.time()
        pass

    def OnCollide(self):
        if self.collider.isCollide is False:
            return

        onColliderList = self.collider.OnCollider()

        for collider in onColliderList:
            if collider.tag == "Player":
                self.isMoveMent = False
                self.isActive = False
            pass
        pass
    pass

    pass