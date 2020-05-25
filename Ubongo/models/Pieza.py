import pygame
from models.componente import Componente

"""
fh = open("../assets/Piezas/Piezas.txt")
# x = []
# i = 0
# for line in fh.read():
#     y = [v for v in line.split()]
#     if y != []:
#         x[i] = [0] * len(y)
#         x[i].append([])
#     i += 1
# fh.close()
x = []
piezas = ['P0', 'P1', 'P2']



c = 0
for line in fh.readlines():
    y = []
    for n in line.strip().split(','):
        if n == 'Fin':
           c = 1
           break
        else:
            y.append(int(n))
    if c == 0:
        x.append(y)
    else:
        break

print(x)
"""

class Pieza(Componente):


    def __init__(self, x, y, idPieza, window):

        self.x, self.y = x, y
        self.window = window
        self.piezaImg = pygame.image.load('ubongo/assets/Piezas/Pieza '+ str(idPieza) + '.png')
        self.width = self.piezaImg.get_rect().width
        self.height = self.piezaImg.get_rect().height
        Componente.__init__(self, x, y, self.width, self.height)
        #factory para obtener forma
        self.forma = 0
        self.idPieza = idPieza

    
    def dibujarPieza(self):
        self.window.blit(self.piezaImg, (self.x, self.y) )



    
