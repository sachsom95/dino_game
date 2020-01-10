import pygame

#initializing the pygame to lead all function
pygame.init()

# while True:
#     screen = pygame.display.set_mode((800,600))
#using just seems to crash it need a quit method

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480


def player(x,y):
    screen.blit(playerImg,(x,y))




#game loop
running =  True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left pressed")

            if event.key == pygame.K_RIGHT:
                print("right pressed")



    player(playerX,playerY )
    pygame.display.update()