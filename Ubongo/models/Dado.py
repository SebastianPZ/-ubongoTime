from models.componente import Componente
import pygame
import random

class Dado(Componente):
    def __init__(self, x, y, width, height, window):
        Componente.__init__(self, x, y, width, height)
        self.window = window
        self.posicion = 0
        self.image = pygame.image.load('../assets/Dado/Dado ' + str(self.posicion + 1) + ' 1.png')

    def tirarDado(self):
        self.posicion = random.randint(0, 5)
        self.image = pygame.image.load('../assets/Dado/Dado ' + str(self.posicion + 1) + ' 1.png')

    def dibujar(self):
        self.window.blit(self.image, (self.x, self.y))

