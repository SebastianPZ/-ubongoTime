import pygame
from models.menu import Menu
from models.Puzzle import  Puzzle
mesa = pygame.image.load('assets/Fondos/fondo mesa.png')
pygame.init()
window = pygame.display.set_mode((1920, 1080))

pygame.display.set_caption("Prueba")
run = True
menu = Menu(window)
enPantallaInicio = True
enJugadores = False
enDificultad = False
enJuego = False

unJugEnJuego = False
dosJugEnJuego = False
tresJugEnJuego = False
dificultadNormal = False
dificultadDificil = False

puzzleImg1 = pygame.image.load('../assets/Puzzles/Puzzle 1.png')
puzzleImg2 = pygame.image.load('../assets/Puzzles/Puzzle 2.png')
puzzle1 = Puzzle(window, 350, 500, 400, 300, puzzleImg1)
puzzle2 = Puzzle(window, 1200, 500, 400, 300, puzzleImg2)


def dibujarMesa(window):
    window.blit(mesa, (0, 0))

def dibujarMenu():
    menu.dibujarMenu()
    menu.dibujarBotones(enPantallaInicio, enJugadores, enDificultad)

def dibujarJuego():
    window.blit(mesa, (0, 0))
    if unJugEnJuego:
        puzzle1.dibujarPuzzle()
        puzzle2.dibujarPuzzle()


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

        if not enJuego:
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
                        unJugEnJuego = True
                     elif menu.botonDosJugadores.isOver(posicionMouse):
                        enJuego = True
                        enJugadores = False
                        dosJugEnJuego = True
                     elif menu.botonTresJugadores.isOver(posicionMouse):
                         enJuego = True
                         tresJugEnJuego = True
                 elif enDificultad:
                     if menu.botonDificultadNormal.isOver(posicionMouse):
                         enDificultad = False
                         dificultadNormal = True
                         enPantallaInicio = True
                     elif menu.botonDificultadDificil.isOver(posicionMouse):
                         enDificultad = False
                         dificultadDificil = True
                         enPantallaInicio = True
















