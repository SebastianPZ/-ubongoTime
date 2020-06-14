import pygame
from models.menu import Menu
from models.Puzzle import Puzzle
from models.PantallaJuego import PantallaJuego
from models.factory.PiezaFactory import PiezaFactory
from models.Juego import Juego

mesa = pygame.image.load('assets/Fondos/fondo mesa.png')
pygame.init()


#window = pygame.display.set_mode((1680, 1050))
#Comenten el de abajo y descomenten el de arriba si su pantalla es más pequeña
window = pygame.display.set_mode((1920, 1080))

pygame.display.set_caption("Prueba")
run = True
menu = Menu(window)
ubongo = Juego(window)



# enPantallaInicio = True
# enJugadores = False
# enDificultad = False
# enJuego = False
#
# unJugEnJuego = False
# dosJugEnJuego = False
# tresJugEnJuego = False
# dificultadNormal = False
# dificultadDificil = False
#
# puzzleImg1 = pygame.image.load('../assets/Puzzles/Puzzle 1.png')
# puzzleImg2 = pygame.image.load('../assets/Puzzles/Puzzle 2.png')
# puzzle1 = Puzzle(window, 350, 550, 400, 300, puzzleImg1, 1, [[1, 2, 3], [3, 4, 1]])
# puzzle2 = Puzzle(window, 1300, 550, 400, 300, puzzleImg2, 1,  [[1, 2, 3], [2, 5, 1]])
#
# dadoValor = 1
# piezasPuzzle1 = []
# piezasPuzzle2 = []
# i = 50
# for piezaId in puzzle1.piezas[dadoValor]:
#     piezasPuzzle1.append(PiezaFactory.crearPieza(250 + i, 770, piezaId, window))
#     i += 50
# j = 50
# for piezaId in puzzle2.piezas[dadoValor]:
#     piezasPuzzle2.append(PiezaFactory.crearPieza(1200 + j, 770, piezaId, window))
#     j += 50







# def dibujarPiezas():
#     for pieza in piezasPuzzle1:
#         pieza.dibujarPieza()
#     for pieza in piezasPuzzle2:
#         pieza.dibujarPieza()


#############################################
#           MOVIMIENTO DE PIEZAS
#############################################
# def moverPiezas(event, piezaId):
#     # con la letra Q se cambia de pieza
#     # con la letra E se gira y con la R se invierte
#     # W, A, S, D para el movimiento
#
#     if event.key == pygame.K_a:
#         piezasPuzzle1[piezaSeleccionadaId].x -= 30
#     elif event.key == pygame.K_w:
#         piezasPuzzle1[piezaSeleccionadaId].y -= 30
#     elif event.key == pygame.K_s:
#         piezasPuzzle1[piezaSeleccionadaId].y += 30
#     elif event.key == pygame.K_d:
#         piezasPuzzle1[piezaSeleccionadaId].x += 30
#     elif event.key == pygame.K_e:
#         # girar pieza
#         pass
#     elif event.key == pygame.K_r:
#         # invertir
#         pass
#     return
#############################################

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
















