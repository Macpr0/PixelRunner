import pygame

pygame.init()
font = pygame.font.Font(None, 50)


def debug(info, y=10, x=10):  # Setting y as first because we use it more
    display_surf = pygame.display.get_surface()  # Gets our Display surface
    debug_surf = font.render(str(info), True, "white")  # Create text surface
    debug_rect = debug_surf.get_rect(topleft=(x, y))  # Created rectangle around text
    pygame.draw.rect(display_surf, "Black", debug_rect)  # Create black rect behind display surf
    display_surf.blit(debug_surf, debug_rect)