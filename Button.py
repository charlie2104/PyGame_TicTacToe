import pygame
class Button:
    text = ""
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def displayButton(self, screen):
        pygame.draw.rect(screen,self.colour,[self.x,self.y,self.width,self.height])

    
