import pygame, sys

pygame.init()

window_size = (800,600)

screen = pygame.display.set_mode(window_size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.display.update()
