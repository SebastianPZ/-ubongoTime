import pygame
import copy
class Jugador():
    def __init__(self, id, listaMovimientos):
        self.id = id
        self.piezas = []
        self.piezaSeleccionada = None
        self.puzzles = []
        self.puzzleSeleccionado = None
        self.ficha = None
        self.gemas = None
        self.listaMovimientos = listaMovimientos

    def moverPieza(self, movimiento):

        if movimiento == self.listaMovimientos[0]:
            self.piezaSeleccionada.y -= 35
            self.piezaSeleccionada.generarPieza()

        elif movimiento == self.listaMovimientos[1]:
            self.piezaSeleccionada.y += 35
            self.piezaSeleccionada.generarPieza()

        elif movimiento == self.listaMovimientos[2]:
            self.piezaSeleccionada.x -= 35
            self.piezaSeleccionada.generarPieza()

        elif movimiento == self.listaMovimientos[3]:
            self.piezaSeleccionada.x += 35
            self.piezaSeleccionada.generarPieza()

        elif movimiento == self.listaMovimientos[4]:
            self.cambiarPiezaSeleccionada()

        elif movimiento == self.listaMovimientos[5]:
            self.piezaSeleccionada.rotarPieza()
            self.piezaSeleccionada.generarPieza()

        elif movimiento == self.listaMovimientos[6]:
            self.piezaSeleccionada.flipearPieza()
            self.piezaSeleccionada.generarPieza()
        else:
            return False
        print("Puzzle #" + str(self.puzzleSeleccionado.idPuzzle))
        print(f'Coordenadas: ({str(self.puzzleSeleccionado.x)} , {str(self.puzzleSeleccionado.y)})')
        print("Pieza #" + str(self.piezaSeleccionada.idPieza))
        print(f'Coordenadas: ({str(self.piezaSeleccionada.x)} , {str(self.piezaSeleccionada.y)})')

        return True

    def cambiarPiezaSeleccionada(self):
        idPiezaSeleccionada = self.piezas.index(self.piezaSeleccionada)
        if idPiezaSeleccionada == len(self.piezas) - 1:
            self.piezaSeleccionada = self.piezas[0]
        else:
            self.piezaSeleccionada = self.piezas[idPiezaSeleccionada + 1]

    def validarColision(self):
        if self.puzzleSeleccionado.colisionConPieza(self.piezaSeleccionada):
            matrizPieza = self.piezaSeleccionada.forma
            matrizPuzzle = self.puzzleSeleccionado.forma
            xPuz = self.puzzleSeleccionado.x
            xPie = self.piezaSeleccionada.x
            yPuz = self.puzzleSeleccionado.y
            yPie = self.piezaSeleccionada.y
            columnaIniPuz = columnaIniPie = 0
            filaIniPuz = filaIniPie = 0
            diferenciaX = (xPie - xPuz)//35
            diferenciaY = (yPuz - yPie)//35

            if diferenciaX < 0:
                columnaIniPie = abs(diferenciaX)
            else:
                columnaIniPuz = abs(diferenciaX)
            if diferenciaY <= 0:
                filaIniPuz = abs(diferenciaY)
            else:
                filaIniPie = abs(diferenciaY)

            _filaIniPuz = copy.copy(filaIniPuz)
            while columnaIniPuz < self.puzzleSeleccionado.width//35 and \
                columnaIniPuz < self.piezaSeleccionada.width//35 + abs(diferenciaX):
                filaIniPuz = copy.copy(_filaIniPuz)
                while filaIniPuz < self.puzzleSeleccionado.height // 35 and \
                    filaIniPuz < self.piezaSeleccionada.height // 35 + abs(diferenciaY):
                    if matrizPuzzle[filaIniPuz][columnaIniPuz] != -2:
                        matrizPuzzle[filaIniPuz][columnaIniPuz] = matrizPieza[filaIniPie][columnaIniPie]
                    filaIniPie += 1
                    filaIniPuz += 1

                columnaIniPie += 1
                columnaIniPuz += 1
        print(self.puzzleSeleccionado.forma)