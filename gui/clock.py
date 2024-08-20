import numpy as np
import pygame
class clock:
    def __init__(self):
        self.clock_start = False
        self.start_time = 0
        self.current_time = 0

    def start(self):
        if not self.clock_start:
            self.start_time = pygame.time.get_ticks()
            self.clock_start = True


    def update(self):
        if self.clock_start:
            self.current_time = (pygame.time.get_ticks() - self.start_time)//1000

