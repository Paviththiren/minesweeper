import numpy as np
import pygame
import pygame_widgets
from clock import clock

class framework:
    def __init__(self):
        # Screen Setup
        pygame.display.set_caption("Minesweeper")
        self.screen = pygame.display.set_mode((985,920))

        #Load Assets
        self.background = pygame.image.load("../Assets/background.jpg")
        self.icon = pygame.image.load("../Assets/game_icon.png")
        self.font = pygame.font.SysFont('Bookman Old Style', 30)

        #Setup Time
        self.clock = clock()


    def update(self):
        self.clock.update()
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.font.render("Time: "+str(self.clock.current_time), True, (0, 0, 0)), (570, 860))


