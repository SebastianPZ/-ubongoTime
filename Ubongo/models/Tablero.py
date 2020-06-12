import pygame
from models.componente import Componente

logo = pygame.image.load('assets/Acciones/ubongo logo1.png')
menu = pygame.image.load('assets/Fondos/fondoUbongo.jpg')
tablero = pygame.image.load('assets/Tablero/Tablero.png')
#tablero = pygame.transform.scale(tablero, (731, 188))
tablero = pygame.transform.scale(tablero, (790, 230))

class Tablero(Componente):
    def __init__(self, window, x, y, width = 100, height = 100):
        Componente.__init__(self, window.get_rect().width / 2 - width / 2, window.get_rect().height / 2 - height / 2, width, height)
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def dibujarTablero(self):
        self.window.blit(tablero, (self.x, self.y))



