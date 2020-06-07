fh = open("Piezas.txt")

piezas = ['P1', 'P0', 'P7', 'P8']


def procesarPiezas(piezas):
    x = []
    y = []
    z = []
    visitados = 0
    c = 0
    contador = 0
    for line in fh.readlines():
        if contador == 0:
            if visitados < len(piezas):
                for pieza in piezas:
                    if line.strip() == pieza:
                        visitados += 1
                        c = 1
                        break
            else:
                break
        if c == 1 and contador == 0:
            contador += 1
            continue
        elif c != 1:
            continue
        if contador > 0:
            if line.strip() == "Fin":
                contador = 0
                c = 0
                z.append(y)
                y = []
                continue
            for n in line.strip().split(','):
                 x.append(int(n))
            y.append(x)
            x = []
            contador += 1

    return z

z = procesarPiezas(piezas)

for elemento in z:
    print(elemento)
print(piezas)
