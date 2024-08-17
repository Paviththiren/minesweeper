import numpy as np
import pygame
class clock:
    def __init__(self):
        self.start_time   = 0
        self.current_time = 0

    def start(self):
        self.start_time = pygame.time.get_ticks()

    def update(self):
        self.current_time = (pygame.time.get_ticks() - self.start_time)//1000

