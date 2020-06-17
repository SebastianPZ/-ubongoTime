import pygame

class CuadradoPuzzle():
    def __init__(self, window, numero, x, y):
        self.window = window
        self.black = (0, 0, 0)
        self.grey = (204, 207, 204)
        self.numero = numero
        self.ladoCuadrado = 35
        self.x = x
        self.y = y

    def dibujarCuadradoPuzzle(self):
        pygame.draw.rect(self.window, self.grey, (self.x, self.y, self.ladoCuadrado, self.ladoCuadrado))
        pygame.draw.rect(self.window, self.black,
                                         (self.x, self.y, self.ladoCuadrado, self.ladoCuadrado), 1)

