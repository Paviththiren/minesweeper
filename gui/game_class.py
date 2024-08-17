import numpy as np
import pygame
import pygame_widgets
from clock import clock
from framework import framework
from game_settings import settings

class game:
    def __init__(self):

        #Create Layout
        self.framework = framework()

        #Settings
        self.settings = settings(self.framework.screen)

    def update(self):
        self.framework.update()


