import pygame
from models.menu import Menu
mesa = pygame.image.load('assets/Fondos/fondo mesa.png')
pygame.init()
window = pygame.display.set_mode((1600, 900))

pygame.display.set_caption("Prueba")
run = True
menu = Menu(window)
enPantallaInicio = True
enJugadores = False
enDificultad = False
enJuego = False

def dibujarMesa(window):
    window.blit(mesa, (0, 0))

def dibujarMenu():
    menu.dibujarMenu()
    menu.dibujarBotones(enPantallaInicio, enJugadores, enDificultad)


def dibujarJuego():
    window.blit(mesa, (0, 0))
    font = pygame.font.SysFont('comicsans', 90)
    text = font.render("UBONGOOOOO", 1, (255, 0, 0))
    window.blit(text,(500, 450))

while run:

    dibujarMesa(window)
    dibujarMenu()
    if enJuego:
        dibujarJuego()

    pygame.display.update()

    for event in pygame.event.get():

        posicionMouse = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEMOTION:
            if enPantallaInicio:
                menu.validarPosicionInicio(posicionMouse)
            elif enJugadores:
                menu.validarPosicionJugadores(posicionMouse)
            elif enDificultad:
                menu.validarPosicionDificultad(posicionMouse)

        if event.type == pygame.MOUSEBUTTONDOWN:
             if enPantallaInicio:
                if menu.botonIniciar.isOver(posicionMouse):
                    enPantallaInicio = False
                    enJugadores = True
                elif menu.botonDificultad.isOver(posicionMouse):
                    enPantallaInicio = False
                    enDificultad = True
             elif enJugadores:
                 if menu.botonUnJugador.isOver(posicionMouse):
                    enJuego = True
                    enJugadores = False
                 elif menu.botonDosJugadores.isOver(posicionMouse):
                    enJuego = True
                    enJugadores = False
                 elif menu.botonTresJugadores.isOver(posicionMouse):
                     enJuego = True
                     enJugadores = False
             elif enDificultad:
                 if menu.botonDificultadNormal.isOver(posicionMouse):
                     enDificultad = False
                     enPantallaInicio = True
                 elif menu.botonDificultadDificil.isOver(posicionMouse):
                     enDificultad = False
                     enPantallaInicio = True
















