import pygame
from models.componente import Componente
from models.LecturaPiezas import recuperarPiezaPorId


class Pieza(Componente):

    def __init__(self, x, y, idPieza, window):
        self.window = window
        self.idPieza = idPieza
        self.piezaImg = pygame.image.load('assets\\Piezas\\Pieza_' + str(idPieza) + '.png')
        self.anchoLargo = self.definirAnchoYLargo()
        Componente.__init__(self, x, y, self.anchoLargo[0], self.anchoLargo[1])
        self.piezaImgEscalada = pygame.transform.scale(self.piezaImg, (self.width, self.height))
        self.forma = recuperarPiezaPorId(self.idPieza)



    def definirAnchoYLargo(self):
        switcher = {
            0: [70, 105],
            1: [140, 70],
            2: [140, 35],
            3: [140, 35],
            4: [105, 105],
            5: [105, 70],
            6: [35, 70],
            7: [140, 70],
            8: [70, 70],
            9: [70, 105],
            10: [70, 70],
            11: [70, 105]
        }
        return switcher.get(self.idPieza)


    def dibujarPieza(self):
        self.window.blit(self.piezaImgEscalada, (self.x, self.y))

    def setForma(self, forma):
        self.forma = forma

    def rotarPieza(self):
        self.piezaImgEscalada = pygame.transform.rotate(self.piezaImgEscalada, 90)
        ##############################################
        # invertir columnas y filas

        matrizResultante = []

        cantidadFilas = len(self.forma)
        cantidadColumnas = len(self.forma[0])

        # crear cantidadFilenecientas columnas
        for f in range(cantidadColumnas):
            matrizResultante.append([])

        # hasta aqui ya tengo la matriz con C filas

        # asigno valores
        for c in range(cantidadColumnas):
            # Mientras que f sea > -1, se le restará 1, comenzando desde cantidadFilas-1
            for f in range(cantidadFilas):
                matrizResultante[c].append(self.forma[f][cantidadColumnas - c - 1])

        self.forma = matrizResultante
        print(self.forma)


    def flipearPieza(self):
        self.piezaImgEscalada = pygame.transform.flip(self.piezaImgEscalada, True, False)

        cantidadFilas = len(self.forma)

        if cantidadFilas == 1:
            return self.forma

        cantidadColumnas = len(self.forma[0])

        matrizResultante = self.forma[:]

        for fila in range(cantidadFilas):
            for columna in range(cantidadColumnas//2):
                matrizResultante[fila][columna], matrizResultante[fila][cantidadColumnas - 1] \
                    = matrizResultante[fila][cantidadColumnas - 1],  matrizResultante[fila][columna]
        self.forma = matrizResultante
        print(self.forma)