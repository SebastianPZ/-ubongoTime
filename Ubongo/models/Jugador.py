import pygame

class Jugador():
    def __init__(self, id, listaMovimientos):
        self.id = id
        self.piezas = []
        self.piezaSeleccionada = 0
        self.puzzles = None
        self.puzzleSeleccionado = None
        self.ficha = None
        self.gemas = None
        self.listaMovimientos = listaMovimientos
    
    def moverPieza(self, movimiento):
        if movimiento == self.listaMovimientos[0]:
            self.piezas[self.piezaSeleccionada].y -= 30
        elif movimiento == self.listaMovimientos[1]:
            self.piezas[self.piezaSeleccionada].y += 30
        elif movimiento == self.listaMovimientos[2]:
            self.piezas[self.piezaSeleccionada].x -= 30
        elif movimiento == self.listaMovimientos[3]:
            self.piezas[self.piezaSeleccionada].x += 30
        elif movimiento == self.listaMovimientos[4]:
            pass
        elif movimiento == self.listaMovimientos[5]:
            pass

    def cambiarPuzzleSeleccionado(self):
        self.puzzleSeleccionado += 1


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
