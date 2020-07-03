import pygame

class Cuadrado():
    def __init__(self, window, numero, x, y, color):
        self.window = window
        self.numero = numero
        self.ladoCuadrado = 35
        self.x = x
        self.y = y
        self.color = color

    def dibujarCuadrado(self, componente, color=None):
        if componente == 'Puzzle':
            pygame.draw.rect(self.window, self.color, (self.x, self.y, self.ladoCuadrado, self.ladoCuadrado))
            pygame.draw.rect(self.window, (0, 0, 0),
                             (self.x, self.y, self.ladoCuadrado, self.ladoCuadrado), 1)
        else:
            pygame.draw.rect(self.window, self.color, (self.x, self.y, self.ladoCuadrado, self.ladoCuadrado))


