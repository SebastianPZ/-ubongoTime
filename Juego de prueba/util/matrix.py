import colorama 
colorama.init()

from colorama import Fore, Back, Style


#filas: input[n]
#columnas: input[f][c]
input =  [
    [1, 0],
    [1, 1],
    [0, 1]]

input2 = [
    [1, 0, 0],
    [1, 1, 1],
    [0, 0, 1]]

input3 = [
    [1, 1, 1],
    [1, 1, 0]]

input4 = [
    [0, 0, 1, 0],
    [1, 1, 1, 1]]

expected =  [
    [0, 1, 1],
    [1, 1, 0]
]

def reflejarVerticalmente(matrizOriginal):
    matrizResultante = []

    cantidadFilas = len(matrizOriginal)
    cantidadColumnas = len(matrizOriginal[0])

    matrizResultante = matrizOriginal[:]
    #Aplicar Divide y venceras (?) 

    #si la matriz tiene columnas par, dividir entre 2
    #10/2 = 5   range(5)
    #si la matriz tiene columnas impar ¿?

     
            #f,n = f,0
            #f,0 = f,n
            
            #f,n-1 = f,0+1
            #f,0+1 = f,n-1

            #f,n-2 = f,0+2
            #f,0+2 = f,n-2

    """
    if cantidadColumnas % 2 != 0:
        ultimoIndice = cantidadColumnas // 2 - 1
    else:
        ultimoIndice = cantidadColumnas // 2 
    """
    if cantidadColumnas == 1:
        return matrizOriginal
    
    #1//2 = 0 - 1 = -1 no
    #2//2 = 1 - 1 = 0 no  
    #3//2 = 2 - 1 = 1 ok
    #4//2 = 2 - 1 = 1 ok
    #5//2 = 2 - 1 = 1 no ()
    #6//2 
    ultimoIndice = cantidadColumnas - 1

    for f in range(cantidadFilas):
        for c in range(cantidadColumnas//2):
            #swap
            #a = matrizOriginal[f][0 + c]
            #matrizResultante[f][ultimoIndice - c] = a
            #b = matrizOriginal[f][ultimoIndice - c]
            #matrizResultante[f][0 + c] = b

            matrizResultante[f][ultimoIndice - c], matrizResultante[f][0 + c] =  matrizResultante[f][0 + c], matrizResultante[f][ultimoIndice - c]

    #    if cantidadColumnas % 2 != 0:
    #       for f in range(cantidadFilas):
    #          matrizResultante[f][cantidadColumnas//2 + 1] = matrizOriginal

    return matrizResultante

def reflejarHorizontalmente(matrizOriginal):
    matrizResultante = []

    cantidadFilas = len(matrizOriginal)
    cantidadColumnas = len(matrizOriginal[0])

    matrizResultante = matrizOriginal[:]
    
    if cantidadFilas == 1:
        return matrizOriginal

    ultimoIndice = cantidadFilas - 1

    for c in range(cantidadColumnas):
        for f in range(cantidadFilas//2):
            matrizResultante[ultimoIndice-f][c], matrizResultante[0+f][c] = matrizResultante[0+f][c], matrizResultante[ultimoIndice-f][c]

    return matrizResultante

def rotarMatriz(matrizOriginal):
    #invertir columnas y filas
    
    matrizResultante = []

    cantidadFilas = len(matrizOriginal)
    cantidadColumnas = len(matrizOriginal[0])

    #crear cantidadFilenecientas columnas
    for f in range(cantidadColumnas):
        matrizResultante.append([])

    #hasta aqui ya tengo la matriz con C filas

    #asigno valores
    for c in range(cantidadColumnas):
        #Mientras que f sea > -1, se le restará 1, comenzando desde cantidadFilas-1
        for f in range(cantidadFilas-1, -1, -1):
            matrizResultante[c].append(matrizOriginal[f][c]) 
    
    return matrizResultante

def testRotacionMatrices(matriz):

    print("\nPieza original:")
    imprimir(matriz)

    for i in range(4):
        print("\Pieza rotada en sentido horario " + str(i))
        matriz = rotarMatriz(matriz)

        imprimir(matriz)
     
def testReflejarHorizontal(matriz):

    print(Fore.GREEN + "\nPieza original:")
    print(Style.RESET_ALL)
    imprimir(matriz)

    print("\Pieza reflejada horizontalmente ")
    matriz = reflejarHorizontalmente(matriz)

    imprimir(matriz)

def testReflejarVertical(matriz):

    print(Fore.GREEN + "\nPieza original:")
    print(Style.RESET_ALL)
    imprimir(matriz)

    print("\Pieza reflejada verticalmente ")
    matriz = reflejarVerticalmente(matriz)

    imprimir(matriz)
                

def imprimir(matriz):
    for f in range(len(matriz)):
        for c in range (len(matriz[0]) ):
            if matriz[f][c] == 1:
                print(Fore.RED + '1', end=" ")
            else:
                print(Fore.WHITE + '0', end=" ")
                    
        print("\n")
    
    print(Style.RESET_ALL)

                
    

testRotacionMatrices(input)
testRotacionMatrices(input2)
testRotacionMatrices(input3)
testRotacionMatrices(input4)

testReflejarHorizontal(input)
testReflejarHorizontal(input2)
testReflejarHorizontal(input3)
testReflejarHorizontal(input4)

testReflejarVertical(input)
testReflejarVertical(input2)
testReflejarVertical(input3)
testReflejarVertical(input4)





