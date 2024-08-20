import pygame
from game_class import Game
import pygame_widgets

pygame.init()

game = Game()
running = True

while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    game.update()
    pygame_widgets.update(events)
    pygame.display.update()

