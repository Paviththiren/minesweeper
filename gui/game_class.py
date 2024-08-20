import numpy as np
import pygame
import pygame_widgets
from clock import clock
from framework import framework
from game_settings import start_screen

class Game:
    def __init__(self):

        #Create Layout
        self.framework = framework()

        #Start Screen & Game Settings
        self.start_screen = start_screen(self.framework.screen)

        #Level

    def update(self):
        self.framework.update()
        if not self.start_screen.level_start:
            self.start_screen.update(self.framework.screen)
        else:
            self.framework.clock.start()
            self.start_screen.disable_start_screen()







