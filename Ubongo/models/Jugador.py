import pygame

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

        elif movimiento == self.listaMovimientos[1]:
            self.piezaSeleccionada.y += 35

        elif movimiento == self.listaMovimientos[2]:
            self.piezaSeleccionada.x -= 35

        elif movimiento == self.listaMovimientos[3]:
            self.piezaSeleccionada.x += 35

        elif movimiento == self.listaMovimientos[4]:
            self.cambiarPiezaSeleccionada()

        elif movimiento == self.listaMovimientos[5]:
            self.piezaSeleccionada.rotarPieza()

        elif movimiento == self.listaMovimientos[6]:
            self.piezaSeleccionada.flipearPieza()
        else:
            return False
        return True



    def cambiarPiezaSeleccionada(self):
        idPiezaSeleccionada = self.piezas.index(self.piezaSeleccionada)
        if idPiezaSeleccionada == len(self.piezas) - 1:
            self.piezaSeleccionada = self.piezas[0]
        else:
            self.piezaSeleccionada = self.piezas[idPiezaSeleccionada + 1]

    def validarColision(self):
        print(str(self.puzzleSeleccionado.colisionConPieza(self.piezaSeleccionada)))
