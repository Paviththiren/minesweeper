import numpy as np
import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button

class start_screen:
    def __init__(self,screen):

        self.level_start = False
        self.font = pygame.font.SysFont('Bookman Old Style',20)

        self.title_font = pygame.font.SysFont('Bookman Old Style', 70)
        self.text_surf = self.title_font.render('Minesweeper', True, (0, 0, 0))
        self.text_surf.set_alpha(255)

        self.row_slider = Slider(screen,300,290,400,20,min=1,max=50,step=1,initial=25,colour=(100,100,100),curved=False)
        self.row_output = TextBox(screen, 420, 325, 150, 50, borderThickness=0, font=self.font, fontSize=40,colour=(180, 180, 180))
        self.row_output.disable()

        self.column_slider = Slider(screen,300,400,400,20,min=1,max=50,step=1,initial=25,colour=(100,100,100),curved=False)
        self.column_output = TextBox(screen, 420, 435, 150, 50,borderThickness=0, font=self.font,fontSize=40,colour=(180,180,180))
        self.column_output.disable()

        self.mines_slider = Slider(screen,300,500,400,20,min=0,max=50,step=1,initial=1,colour=(100,100,100),curved=False)
        self.mines_output = TextBox(screen, 420, 535, 150, 50,borderThickness=0, font=self.font,fontSize=40,colour=(180,180,180))
        self.mines_output.disable()

        self.start_button = Button(screen,445,625,100,50,text="Start",fontSize=40,font=self.font,radius=10,onClick = self.start_level)

    def update(self,screen):
        self.mine_slider_update()
        self.row_output.setText(("Rows: " + str(self.row_slider.getValue())).center(13))
        self.column_output.setText(("Columns: " + str(self.column_slider.getValue())).center(2))
        self.mines_output.setText(("Mines: " + str(self.mines_slider.getValue())).center(13))
        screen.blit(self.text_surf,(280,118))

    def disable_start_screen(self):
        self.row_slider.hide()
        self.row_output.hide()
        self.column_slider.hide()
        self.column_output.hide()
        self.mines_slider.hide()
        self.mines_output.hide()
        self.start_button.hide()

    def start_level(self):
        self.level_start = True

    def mine_slider_update(self):
        current_value = self.mines_slider.getValue()
        row_value = self.row_slider.getValue()
        column_value = self.column_slider.getValue()

        #If the current value is higher than the new max possible value --> reduce to max value
        if current_value > row_value*column_value:
            self.mines_slider.setValue(row_value*column_value)

        #Error occurs when row and column = 1 --> exception
        if row_value == 1 and column_value == 1:
            set_value = 1
        else:
            set_value = row_value*column_value          #new max value

        self.mines_slider.__setattr__('max',set_value)



