import pygame
from models.componente import Componente



class Pieza(Componente):

    def __init__(self, x, y, idPieza, window):
        self.window = window
        self.piezaImg = pygame.image.load('../assets/Piezas/Pieza '+ str(idPieza) + '.png')
        Componente.__init__(self, x, y, self.piezaImg.get_rect().width, self.piezaImg.get_rect().height)
        self.piezaImgEscalada = pygame.transform.scale(self.piezaImg, (self.width//2, self.height//2))
        self.forma = [[]]
        self.idPieza = idPieza

    
    def dibujarPieza(self):
        self.window.blit(self.piezaImgEscalada, (self.x, self.y))

    def setForma(self, forma):
        self.forma = forma


    
