import pygame
from models.menu import Menu
from models.Juego import Juego

mesa = pygame.image.load('assets/Fondos/fondo mesa.png')
pygame.init()


window = pygame.display.set_mode((1920, 1080))

pygame.display.set_caption("Prueba")
run = True
menu = Menu(window)
ubongo = Juego(window)


paraTirarDado = 0
while run:

    window.blit(mesa, (0, 0))
    if ubongo.enMenu:
        ubongo.dibujarMenu()
    if ubongo.enJuego:
        ubongo.dibujarJuego()


    pygame.display.update()

    for event in pygame.event.get():

        posicionMouse = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEMOTION:
            if ubongo.enMenu:
                ubongo.hoverBotonesMenu(posicionMouse)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if ubongo.enMenu:
                ubongo.transicionarMenu(posicionMouse)

        if event.type == pygame.KEYDOWN:
            if ubongo.enJuego:
                ubongo.jugar(event.key)
















