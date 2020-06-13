import pygame
from models.componente import Componente
from models.LecturaPuzzles import recuperarPiezasDePuzzle
from models.LecturaPuzzles import recuperarPuzzleNormalPorId

class Puzzle(Componente):
    def __init__(self, window, x, y, width, height, idPuzzle, dificultad):
        Componente.__init__(self, x, y, width, height)
        self.window = window
        self.idPuzzle = idPuzzle
        self.image = pygame.image.load('../assets/Puzzles/Puzzle ' + str(self.idPuzzle) + '.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.piezas = recuperarPiezasDePuzzle(self.idPuzzle)
        self.forma = recuperarPuzzleNormalPorId(self.idPuzzle)
        self.dificultad = dificultad,

    def dibujarPuzzle(self):
        self.window.blit(self.image, (self.x, self.y))
