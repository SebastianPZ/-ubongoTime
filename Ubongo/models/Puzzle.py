import pygame
from models.componente import Componente

class Puzzle(Componente):
    def __init__(self, window, x, y, width, height, idPuzzle, dificultad):
        Componente.__init__(self, x, y, width, height)
        self.window = window
        self.image = pygame.image.load('../assets/Puzzles/Puzzle ' + str(idPuzzle) + '.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.piezas = None
        self.forma = [[]]
        self.dificultad = dificultad,


    def dibujarPuzzle(self):
        self.window.blit(self.image, (self.x, self.y))
