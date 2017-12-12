import pygame
import time
import copy
pygame.init()
(width,height) = (700,500)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("BLUR APPLICATOR")
pygame.display.flip()

chips = [pygame.image.load('Chip1.png'),pygame.image.load('Chip2.png'),pygame.image.load('Chip3.png'),pygame.image.load('Chip4.png'),pygame.image.load('Chip5.png'),pygame.image.load('Chip6.png')]
for x in range(0,len(chips)):
    chips[x] = pygame.transform.scale(chips[x], (235,87))
posX,posy = (0,0)
score = 0
color = [255,255,255]
gray = [100,100,100]
running = True
mouseDown = False
zeroOne=(0,1)
OKButton = pygame.Rect(250,100,100,25)
screen.fill(gray)
green = [0,255,0]
red = [255,0,0]
TextFont = pygame.font.SysFont("monospace", 30)
newLevel = True

ApprovedRejected = 0
blur = False



while running:
    blur = False
    if blur == True:
        screen.fill(gray)
    if newLevel == True:
        posy = 250
        time.sleep(.1)
        if posX < 350-(int(chips[score].get_rect().size[0])/2):
            print(posX)
            blur = True
            posX += 10
        else:
            newLevel = False
            blur = False

    if ApprovedRejected == 2:
        if posy < 550-(int(chips[score].get_rect().size[0])/2):
            print(posX)
            blur = True
            posy += 10
        else:
            posX = -100
            posy = -400
            score += 1
            saveImg = chips[score].copy()
            pygame.image.save(screen,"Chip1.png")
            blur = False
            ApprovedRejected = 0
            newLevel = True

    if ApprovedRejected == 1:
        if posy > -50-(int(chips[score].get_rect().size[0])/2):
            print(posX)
            blur = True
            posy -= 10
        else:
            posX = -100
            posy = -400
            score += 1
            blur = False
            ApprovedRejected = 0
            newLevel = True



    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]:
            mouseDown = True
            if pygame.mouse.get_pos()[0] < 400:
                if pygame.mouse.get_pos()[0] > 300:
                    if pygame.mouse.get_pos()[1] <200:
                        if pygame.mouse.get_pos()[1] > 100:
                            print("Hola")
                            ApprovedRejected = 1
                    if pygame.mouse.get_pos()[1] <475:
                        if pygame.mouse.get_pos()[1] > 375:
                            print("Hola2")
                            ApprovedRejected = 2
            chips[score].set_at((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]),color)
            chips[score].set_at((int(pygame.mouse.get_pos()[0])-241, int(pygame.mouse.get_pos()[1])-251), color)
            chips[score].set_at((int(pygame.mouse.get_pos()[0]) - 240, int(pygame.mouse.get_pos()[1]) - 250), color)
            chips[score].set_at((int(pygame.mouse.get_pos()[0]), int(pygame.mouse.get_pos()[1]) - 251), color)
            chips[score].set_at((int(pygame.mouse.get_pos()[0]), int(pygame.mouse.get_pos()[1]) - 250), color)
            chips[score].set_at((int(pygame.mouse.get_pos()[0]) - 241, int(pygame.mouse.get_pos()[1])), color)
            chips[score].set_at((int(pygame.mouse.get_pos()[0]) - 240, int(pygame.mouse.get_pos()[1])), color)
            chips[score].set_at((int(pygame.mouse.get_pos()[0]) - 240, int(pygame.mouse.get_pos()[1]) - 251), color)
            chips[score].set_at((int(pygame.mouse.get_pos()[0]) - 241, int(pygame.mouse.get_pos()[1]) - 250), color)
        else:
            mouseDown = False
    pygame.display.flip()
    if blur:
        screen.fill(gray)
    screen.blit(chips[score], (posX, posy))

    Yes = TextFont.render("Approved", 1, gray)
    No = TextFont.render("Rejected", 1, gray)
    pygame.draw.rect(screen, green, (300, 100, 100, 100))
    pygame.draw.rect(screen, red, (300, 375, 100, 100))
    screen.blit(Yes, (300, 100))
    screen.blit(No, (300, 375))
