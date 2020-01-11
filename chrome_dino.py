import pygame


WIN_WIDTH = 1000
WIN_HEIGHT = 500
pygame.init()
pygame.display.set_caption("Dino")
screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
dinoRun = [(pygame.image.load("assets/dinorun0000.png")) , (pygame.image.load("assets/dinorun0001.png")),(pygame.image.load("assets/dinoJump0000.png")) ]


class dino:
    '''The class for t-rex'''
    img = dinoRun
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.clk = 0
        self.acc = 9.8

    def move(self):
        self.clk += 1

    def jump(self):

















def dino(x,y,i):
    print(i)

    screen.blit(dinoRun[i],(100,300))

running = True
clk=0
while running:
    clk +=1
    screen.fill((255,255,255))

    dino(1,1,clk%2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()
