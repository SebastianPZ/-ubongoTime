from models import componente

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


# class Pieza(componente):
#     def __init__(self, x, y, width, height, forma, tipoPieza):
#
#         componente.__init__(self, x, y, width, height)
#         self.forma = forma
#         self.tipoPieza = tipoPieza

    
