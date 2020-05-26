import pygame
from models.componente import Componente
logo = pygame.image.load('assets/Acciones/ubongo logo1.png')

class Logo(Componente):
    def __init__(self, width = logo.get_rect().width, height = logo.get_rect().height):
        Componente.__init__(self, 0, 0, width, height)
        self.imagen = logo

    def dibujarLogo(self, window):
        window.blit(self.imagen, (self.x, self.y))