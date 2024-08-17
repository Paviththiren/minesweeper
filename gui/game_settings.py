import numpy as np
import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

class settings:
    def __init__(self,screen):

        self.row_slider = Slider(screen,200,200,400,30,min=1,max=50,step=1)
        self.column_slider = Slider(screen,300,300,400,30,min=1,max=50,step=1)
        self.row_output = TextBox(screen,475,200,50,50,fontSize=30)
        self.column_output = TextBox(screen, 600, 200, 50, 50, fontSize=30)
        self.row_output.disable()
        self.column_output.disable()


