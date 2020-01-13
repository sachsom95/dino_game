import pygame
import sys
WIN_WIDTH = 1200
WIN_HEIGHT = 500
pygame.init()
pygame.display.set_caption("Dino")
screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT),pygame.FULLSCREEN)
# screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
dinoRun = [(pygame.image.load("assets/dinorun0000.png")) , (pygame.image.load("assets/dinorun0001.png")),(pygame.image.load("assets/dinoJump0000.png")) ]
ground_img = pygame.image.load("assets/Ground.png")

class dino:
    '''The class for t-rex'''
    img = dinoRun
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.clk = 0
        self.acc = 9.8
        self.vel = 0
        self.img_count = 0
        self.height = self.y

    def move(self):
        self.clk += 1
        displacement = -self.vel * self.clk + ((1.5) * self.clk**2)
        if displacement > 300:
            displacement = 300
        self.y = displacement
        print(self.y)
    def jump(self):
        self.vel = -10.5
        self.clk = 0
        self.height = self.y
        print("space pressed")

    def draw (self , screen):
        clock = pygame.time.Clock()
        clock.tick(60)
        self.img_count +=1
        if self.y < 300:
            self.dino_img = self.img[2]
            screen.blit(self.dino_img,(self.x,self.y))
            # problem i had when i didnt set counter to 0 was it kept runing the jump image as counter went beyond 4
            self.img_count = 0
        if self.img_count <= 2 and self.y == 300:
            self.dino_img = self.img[0]
        elif self.img_count <= 4 and self.y == 300:
            self.dino_img =self.img[1]
            self.img_count = 0


        screen.blit(self.dino_img,(self.x,self.y))

class ground:
    def __init__(self,y):
        self.y = y
        self.img = ground_img
        self.x = 0
    def draw(self,offset,screen):
        self.x += 3
        if self.x > 533:
            self.x = 0
        x_coordinate = self.x - offset
        screen.blit(self.img,(-x_coordinate,self.y))






def main(screen):

    obj = dino(100,300)
    obj_ground = ground(400)
    running = True
    clk = 0
    while running:
        clk += 1
        screen.fill((255, 255, 255))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    obj.jump()
                if event.key ==pygame.K_ESCAPE:
                    running = False
                    sys.exit()

        obj.draw(screen)
        obj_ground.draw(0,screen)
        obj_ground.draw(533,screen)
        obj_ground.draw(1066,screen)
        obj_ground.draw(1066+533, screen)
        obj.move()
        pygame.display.update()


main(screen)
