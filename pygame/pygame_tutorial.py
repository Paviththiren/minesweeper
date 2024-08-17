import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

#Titel and Icon
pygame.display.set_caption("Minesweeper")

#<a href="https://www.flaticon.com/free-icons/bomb" title="bomb icons">Bomb icons created by Pixel perfect - Flaticon</a>
icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)

font = pygame.font.SysFont('Calibri Light',50)

start = True

running = True
while running:
    if start:
        start_time = pygame.time.get_ticks()
        start = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = (pygame.time.get_ticks() - start_time)//1000
    screen.fill((128,128,128))
    screen.blit(font.render("Time: "+str(current_time),True,(0,0,0)),(600,48))

    pygame.display.update()



