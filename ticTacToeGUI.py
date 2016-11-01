import pygame
from Button import *
pygame.init()


#setting width and height
width  = 800
height = 800

clock = pygame.time.Clock()

#buttons
buttonList = []
#colours
red = (255,000,000)
blue = (000,000,255)
green = (000,255,000)
white = (255,255,255)
black = (000,000,000)
lightGrey = (100,100,100)

#screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')

def checkQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def createButtons():
    global buttonList
    for i in range(1,4):
        buttonList.append(Button((250*i)-200,50, 200, 200, white))
        buttonList.append(Button((250*i)-200,300, 200, 200, white))
        buttonList.append(Button((250*i)-200,550, 200, 200, white))

def drawButtons():
    for button in buttonList:
        button.displayButton(screen)
                              
def gameLoop():
    createButtons()
    while True:       
        screen.fill(lightGrey)
        checkQuit()
        mouse = pygame.mouse.get_pos()

        drawButtons()
        #updates the screen
        pygame.display.update()
        clock.tick(30)

gameLoop()
