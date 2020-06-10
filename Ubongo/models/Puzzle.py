import pygame
from models.componente import Componente

class Puzzle(Componente):
    def __init__(self, window, x, y, width, height, image, dificultad, piezas):
        Componente.__init__(self, x, y, width, height)
        self.window = window
        self.image = pygame.transform.scale(image, (width, height))
        self.dificultad = dificultad,
        self.piezas = piezas

    def dibujarPuzzle(self):
        self.window.blit(self.image, (self.x, self.y))
