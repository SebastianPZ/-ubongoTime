from models.componente import Componente
import pygame
import random

class Dado(Componente):
    def __init__(self, x, y, width, height, window):
        Componente.__init__(self, x, y, width, height)
        self.window = window
        self.image = pygame.image.load('../assets/Dado/Dado 1.png')

    def dibujarDado(self):
        self.window.blit(self.image, (self.x, self.y))

    def dadoUno(self):
        self.image = pygame.image.load('../assets/Dado/Dado 1.png')

    def dadoDos(self):
        self.image = pygame.image.load('../assets/Dado/Dado 2.png')

    def dadoTres(self):
        self.image = pygame.image.load('../assets/Dado/Dado 3.png')

    def dadoCuatro(self):
        self.image = pygame.image.load('../assets/Dado/Dado 4.png')

    def dadoCinco(self):
        self.image = pygame.image.load('../assets/Dado/Dado 5.png')

    def dadoSeis(self):
        self.image = pygame.image.load('../assets/Dado/Dado 6.png')

    def tirarDado(self):
        aleatorio = random.randint(1, 6)
        if aleatorio == 1:
            self.dadoUno()
        elif aleatorio == 2:
            self.dadoDos()
        elif aleatorio == 3:
            self.dadoTres()
        elif aleatorio == 4:
            self.dadoCuatro()
        elif aleatorio == 5:
            self.dadoCinco()
        elif aleatorio == 6:
            self.dadoSeis()

    def dibujar(self):
        self.window.blit(self.image, (self.x, self.y))

