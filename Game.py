import pygame
from random import randint

pygame.init()
win = pygame.display.set_mode((500, 500))#This is the main window where I showing game
pygame.display.set_caption("Game")#This is the name of the window
clock = pygame.time.Clock()

ground_y = 370#Players distanse of the ground
x, y = 50, ground_y
width, height = 128, 128#Players parametrs
vel = 5

isJump = False
jumpCount = 10
animCount = 0

left = False
right = False
lastMove = "left"

"""This is loading images"""
movLeft = [pygame.image.load('ant/Beg0.png'), pygame.image.load('ant/Beg1.png'),
           pygame.image.load('ant/Beg2.png'), pygame.image.load('ant/Beg3.png')]
movSpace = [pygame.image.load('ant/Skok0.png'), pygame.image.load('ant/Skok1.png'),
            pygame.image.load('ant/Skok2.png'), pygame.image.load('ant/Skok3.png')]
bg = pygame.image.load('ant/1.jpg')
payerStand = pygame.image.load('ant/Sidit1.png')


"""This function generate random colors for the SHELL"""
def rand_color():
    return(randint(0, 255), randint(0, 255), randint(0, 255))

"""This class, hou bilding shell, function 'draw' drawind shell"""
class shell():
    def __init__(self, x, y, radius, facing, color=None):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def loadImag():
    global animCount
    win.blit(bg, (0, 0))#Background image "bd - variable name", coords (0,0), where is the image squash

    if animCount + 1 >= 20:
        animCount = 0

    if win.blit(movLeft[animCount // 5], (x, y)):
        animCount += 1
    elif win.blit(movSpace[animCount // 5], (x, y)):
        animCount += 1
    else:
        win.blit(payerStand, (x, y))

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


run = True
bullets = []#List shell
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keyboard = pygame.key.get_pressed()
    if keyboard[pygame.K_f]:#Shooting!
        if lastMove == "left":
            facing = -1
        else:
            facing = 1

        if len(bullets) < 100:
            bullets.append(shell(round(x + width // 2), round(y + height // 2), 5, facing, rand_color()))

    if keyboard[pygame.K_LEFT] and x > 5:
        x -= vel
        left = True
        lastMove = "left"
    elif keyboard[pygame.K_RIGHT] and x < 500 - width - 5:
        x += vel
        right = True
        lastMove = "right"
    else:
        left = False
        right = False
        animCount = 0
    if not (isJump):
        if keyboard[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    loadImag()
pygame.quit()
