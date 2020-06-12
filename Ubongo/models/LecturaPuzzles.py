def recuperarPuzzleNormalPorId(idPuzzle):
    fh = open('assets\\Puzzles\\PuzzlesDificultadNormal.txt', 'r')
    c = 0
    matrizPuzzle = []
    partePuzzle = []
    for line in fh.readlines():
        if line.strip() == '#Puzzle ' + str(idPuzzle):
            c = 1
            continue
        if c == 1:
            if line.strip() == '#Piezas ' + str(idPuzzle):
                c = 0
                break
            else:
                for n in line.strip().split(','):
                    partePuzzle.append(int(n))
                matrizPuzzle.append(partePuzzle)
                partePuzzle = []


    return matrizPuzzle

def leerPiezasPorDado(d)
