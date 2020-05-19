import pygame, time
from models.player import Player

pygame.init()
# ....set_mode((width, height))
displayWidth = 850
displayHeight = 480
window = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'),
             pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'),
             pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'),
             pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'),
             pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'),
            pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'),
            pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'),
            pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'),
            pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

clock = pygame.time.Clock()



def redrawGameWindow():

    #window.fill((0, 0, 0))
    #bg: background , (0, 0): position
    window.blit(bg, (0, 0))
    man.draw(window, walkLeft, walkRight, char)
    pygame.display.update()

#mainloop
man = Player(300, 410, 64, 64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.velocity:
        man.x -= man.velocity
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x + man.width + man.velocity < displayWidth:
        man.x += man.velocity
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0 or man.y == 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
