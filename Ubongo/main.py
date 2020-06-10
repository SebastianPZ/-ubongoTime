import pygame
from models.menu import Menu
from models.Puzzle import Puzzle
from models.PantallaJuego import PantallaJuego
from models.PiezaFactory import PiezaFactory

mesa = pygame.image.load('assets/Fondos/fondo mesa.png')
pygame.init()
window = pygame.display.set_mode((1920, 1080))

pygame.display.set_caption("Prueba")
run = True
menu = Menu(window)
pantallaJuego = PantallaJuego(window)
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
puzzle1 = Puzzle(window, 350, 550, 400, 300, puzzleImg1, 1, [[1, 2, 3], [3, 4, 1]])
puzzle2 = Puzzle(window, 1300, 550, 400, 300, puzzleImg2, 1,  [[1, 2, 3], [2, 5, 1]])

dadoValor = 1
piezasPuzzle1 = []
piezasPuzzle2 = []
i = 50
for piezaId in puzzle1.piezas[dadoValor]:
    piezasPuzzle1.append(PiezaFactory.crearPieza(250 + i, 770, piezaId, window))
    i += 50
j = 50
for piezaId in puzzle2.piezas[dadoValor]:
    piezasPuzzle2.append(PiezaFactory.crearPieza(1200 + j, 770, piezaId, window))
    j += 50


def dibujarMesa(window):
    window.blit(mesa, (0, 0))
    pantallaJuego.dibujarTablero()


def dibujarMenu():
    window.blit(mesa, (0, 0))
    menu.dibujarMenu()
    menu.dibujarBotones(enPantallaInicio, enJugadores, enDificultad)

def dibujarJuego():
    window.blit(mesa, (0, 0))
    if unJugEnJuego:
        pantallaJuego.dibujarTablero()
        puzzle1.dibujarPuzzle()
        puzzle2.dibujarPuzzle()

def dibujarPiezas():
    for pieza in piezasPuzzle1:
        pieza.dibujarPieza()
    for pieza in piezasPuzzle2:
        pieza.dibujarPieza()

while run:

    dibujarMenu()
    if enJuego:
        pantallaJuego.dibujarTablero()
        dibujarJuego()
        dibujarPiezas()
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
















