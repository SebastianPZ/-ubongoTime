import pygame
from models.componente import Componente
from Ubongo.assets.Piezas import LecturaPiezas


class Pieza(Componente):


    def __init__(self, x, y, idPieza, window):

        self.x, self.y = x, y
        self.window = window
        self.piezaImg = pygame.image.load('ubongo/assets/Piezas/Pieza '+ str(idPieza) + '.png')
        self.width = self.piezaImg.get_rect().width
        self.height = self.piezaImg.get_rect().height
        Componente.__init__(self, x, y, self.width, self.height)

        
        self.forma = 0
        self.idPieza = idPieza

    
    def dibujarPieza(self):
        self.window.blit(self.piezaImg, (self.x, self.y) )



    
