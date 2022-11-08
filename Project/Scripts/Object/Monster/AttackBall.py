from Scripts.Object.Monster.Monster import *

class AttackBall(Monster):
    image = load_image('image/Monster/RedBat Monster/Ball_Red.png')
    image_type = [0, 0, 32, 32]
    def __init__(self):
        super(AttackBall, self).__init__()

        self.image = AttackBall.image
        self.image_type = AttackBall.image_type
        self.isActive = False
        self.isMoveMent = True
        self.moveDir = [0,0] # 공이 나아가는 방향
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

        self.MoveMent()
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

    def MoveMent(self):
        if self.isMoveMent is False:
            return

        self.transform.Position += self.moveDir
        pass

    def OnObject(self):   # 오브젝트 활성화 할씨 호출
        self.collider.isCollide = True
        self.isActive = True
        self.isMoveMent = True
        self.lifeStart = time.time()

        dir = Monster.target.transform.Position - self.transform.Position
        dir = dir/numpy.linalg.norm(dir)

        self.moveDir = dir
        pass

    pass