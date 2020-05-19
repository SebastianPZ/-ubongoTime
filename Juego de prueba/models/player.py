class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, window, walkLeft, walkRight, char):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            window.blit(walkLeft[int(self.walkCount // 3)], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            window.blit(walkRight[int(self.walkCount // 3)], (self.x, self.y))
            self.walkCount += 1
        else:
            window.blit(char, (self.x, self.y))