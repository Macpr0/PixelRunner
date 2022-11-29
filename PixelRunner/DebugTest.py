import pygame
from sys import exit
from Debug import debug

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("Runner")

# Icon
icon_surface = pygame.image.load("player_stand.png")
pygame.display.set_icon(icon_surface)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("white")
    debug(pygame.mouse.get_pos())
    debug(pygame.mouse.get_pressed(), 70)  # 70 is the Y and the X is still 10
    debug("mouse!", pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])  # Follows Player mouse

    pygame.display.update()
    clock.tick(60)

