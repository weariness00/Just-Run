from Scripts.Object.Monster.Monster import *

class AttackBall(Monster):
    image = load_image('image/Monster/RedBat Monster/Ball_Red.png')
    def __init__(self, target):
        super(AttackBall, self).__init__(target)

        self.image = AttackBall.image
        self.image_type = [0, 0, 32, 32]
        self.isActive = False
        self.isMoveMent = True
        self._speed = 90

        # Transform
        self.transform.Scale *= 0.7

        # Collide
        self.collider.SetCollideBox(numpy.array([[0,0], [32,32] * self.transform.Scale]))
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
        if self.isDeath is True:
            self.isActive = False
        pass

    def OnCollide(self):
        if self.collider.isCollide is False:
            return

        onColliderList = self.collider.OnCollider()

        for collider in onColliderList:
            if collider.tag == "Player":
                self.isActive = False
                self.isMoveMent = True
                print('Playe 충돌 __ AttackBall 에서')
            pass
        pass
    pass

    pass