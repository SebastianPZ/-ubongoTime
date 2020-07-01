import pygame

def definirMovimientosFichas(idJugador):
    if idJugador == 0:
        return [pygame.K_w, pygame.K_s]
    elif idJugador == 1:
        return [pygame.K_UP, pygame.K_DOWN]