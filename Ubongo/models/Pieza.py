import pygame
from models.componente import Componente
from models.LecturaPiezas import recuperarPiezaPorId


class Pieza(Componente):

    def __init__(self, x, y, idPieza, window):
        self.window = window
        self.idPieza = idPieza
        self.piezaImg = pygame.image.load('assets\\Piezas\\Pieza_' + str(idPieza) + '.png')
        Componente.__init__(self, x, y, self.piezaImg.get_rect().width, self.piezaImg.get_rect().height)
        self.piezaImgEscalada = pygame.transform.scale(self.piezaImg, (self.width//3, self.height//3))
        self.forma = recuperarPiezaPorId(self.idPieza)


    def dibujarPieza(self):
        self.window.blit(self.piezaImgEscalada, (self.x, self.y))

    def setForma(self, forma):
        self.forma = forma


    
