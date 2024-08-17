import pygame
from game_class import game
import pygame_widgets

pygame.init()

game = game()
running = True

game.framework.clock.start()

while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    game.update()
    game.settings.row_output.setText(game.settings.row_slider.getValue())
    game.settings.column_output.setText(game.settings.column_slider.getValue())
    pygame_widgets.update(events)
    pygame.display.update()

