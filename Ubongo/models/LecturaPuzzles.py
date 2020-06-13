def recuperarPuzzlePorId(idPuzzle, dificultad):
    fh = None
    if dificultad == "Normal":
        fh = open('assets\\Puzzles\\PuzzlesDificultadNormal.txt', 'r')
    else:
        fh = open('assets\\Puzzles\\PuzzlesDificultadDificil.txt', 'r')
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



def recuperarPiezasDePuzzle(idPuzzle):
    fh = open('assets\\Puzzles\\PiezasDeCadaPuzzle.txt', 'r')
    c = 0
    listaPiezas = []
    matrizPiezas = []
    for line in fh.readlines():
        if line.strip() == '#Piezas ' + str(idPuzzle):
            c = 1
            continue
        if c == 1:
            for n in line.strip().split(','):
                listaPiezas.append(int(n))
            matrizPiezas.append(listaPiezas)
            listaPiezas = []
    return matrizPiezas