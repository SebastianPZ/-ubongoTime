import pygame
from models.componente import Componente
from models.LecturaPuzzles import recuperarPiezasDePuzzle
from models.LecturaPuzzles import recuperarPuzzlePorId
from models.LecturaPuzzles import recuperarImagenPorIdYDificultad



class Puzzle(Componente):
    def __init__(self, window, x, y, width, height, idPuzzle, dificultad):
        Componente.__init__(self, x, y, width, height)
        self.window = window
        self.idPuzzle = idPuzzle
        self.dificultad = dificultad
        self.image = recuperarImagenPorIdYDificultad(self.idPuzzle, self.dificultad)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, 90)
        self.piezas = recuperarPiezasDePuzzle(self.idPuzzle, self.dificultad)
        self.forma = recuperarPuzzlePorId(self.idPuzzle, self.dificultad)

    def dibujarPuzzle(self):
        self.window.blit(self.image, (self.x, self.y))
