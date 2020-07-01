import pygame
import copy
import random as random
from models.menu import Menu
from models.factory.PuzzleFactory import PuzzleFactory
from models.factory.PiezaFactory import PiezaFactory
from models.Dado import Dado
from models.Puzzle import Puzzle
from models.utils.movimientosJugador import definirMovimientosJugador
from models.Jugador import Jugador
from models.PantallaJuego import PantallaJuego

class Juego():

    def __init__(self, window):
        self.window = window
        self.menu = Menu(window)
        self.pantallaJuego = PantallaJuego(window)
        self.tablero = None
        self.jugadores = []
        self.numeroRonda = 0
        self.dado = Dado(300, 300, 100, 100, self.window)
        self.temporizador = None
        self.mazoPuzzles = []
        self.dificultad = ""
        self.numeroJugadores = 0
        self.enJuego = False
        self.enMenu = True
        self.enRonda = False

    def crearJugadores(self):
        for id in range(self.numeroJugadores):
            self.jugadores.append(Jugador(id, definirMovimientosJugador(id)))

    def asignarPuzzles(self, dificultad):
        idPuzzle = 0
        x = 0
        y = 650
        espaciado = 0
        if self.numeroJugadores == 2:
            x = 350
            espaciado = 850
        elif self.numeroJugadores == 3:
            x = 200
            espaciado = 600
        elif self.numeroJugadores == 4:
            x = 155
            espaciado = 450
        for i in range(self.numeroJugadores):
            if i != 0:
                x += espaciado
            for _ in range(9):
                if dificultad == "Normal":
                   idPuzzle = 1#random.randint(1,8)
                elif dificultad == "Difícil":
                   idPuzzle = random.randint(1,34)
                puzzleGenerado = PuzzleFactory.crearPuzzle(x, y, idPuzzle, self.window, dificultad)
                self.jugadores[i].puzzles.append(puzzleGenerado)
            
            #####
            self.jugadores[i].puzzleSeleccionado = copy.copy(self.jugadores[i].puzzles[0])
            self.jugadores[i]._puzzleSeleccionadoForma = copy.deepcopy(self.jugadores[i].puzzleSeleccionado.forma)



    def dibujarPuzzles(self):
        for i in range(self.numeroJugadores):
            self.jugadores[i].puzzles[self.numeroRonda].dibujarPuzzle()

    def asignarPiezas(self):
        pieza = None

        for i in range(self.numeroJugadores):

            jugador = self.jugadores[i]
            x = jugador.puzzleSeleccionado.x
            codigosPiezas = jugador.puzzleSeleccionado.piezas[self.dado.posicion]
            y = jugador.puzzleSeleccionado.y + jugador.puzzleSeleccionado.height + 35

            for j in range(len(codigosPiezas)):
                if j > 0 and pieza != None:
                    x += pieza.width
                pieza = PiezaFactory.crearPieza(x, y, codigosPiezas[j], self.window)
                jugador.piezas.append(pieza)

            self.jugadores[i].piezaSeleccionada = self.jugadores[i].piezas[0]

    def dibujarPiezas(self):
        for i in range(self.numeroJugadores):
            for j in range(len(self.jugadores[i].piezas)):
                self.jugadores[i].piezas[j].dibujarPieza()

    def dibujarMenu(self):
        if self.enMenu:
            self.menu.dibujarMenu()
            self.menu.dibujarBotones()

    def hoverBotonesMenu(self, pos):
        self.menu.hoverBotonesMenu(pos)

    #aqui esta el monstruo
    def transicionarMenu(self, posicionMouse):
        if self.menu.enPantallaInicio:
            if self.menu.botonIniciar.isOver(posicionMouse):
                self.menu.enPantallaInicio = False
                self.menu.enJugadores = True
            elif self.menu.botonDificultad.isOver(posicionMouse):
                self.menu.enPantallaInicio = False
                self.menu.enDificultad = True

        elif self.menu.enJugadores:
            if self.dificultad != "":

                if self.menu.botonUnJugador.isOver(posicionMouse):
                    self.numeroJugadores = 2
                elif self.menu.botonDosJugadores.isOver(posicionMouse):
                    self.numeroJugadores = 3
                elif self.menu.botonTresJugadores.isOver(posicionMouse):
                    self.numeroJugadores = 4
                if self.menu.botonUnJugador.isOver(posicionMouse) or self.menu.botonDosJugadores.isOver(posicionMouse) or self.menu.botonTresJugadores.isOver(posicionMouse):
                    
                    self.menu.enJugadores = False
                    self.crearJugadores()
                    self.asignarPuzzles(self.dificultad)
                    self.asignarPiezas()
                    self.enJuego = True
                    self.enMenu = False

            if self.menu.botonRegresar.isOver(posicionMouse):
                self.menu.enPantallaInicio = True
                self.menu.enJugadores = False
        elif self.menu.enDificultad:
            if self.menu.botonDificultadNormal.isOver(posicionMouse):
                self.menu.enDificultad = False
                self.menu.enPantallaInicio = True
                self.dificultad = "Normal"
            elif self.menu.botonDificultadDificil.isOver(posicionMouse):
                self.menu.enDificultad = False
                self.menu.enPantallaInicio = True
                self.dificultad = "Difícil"
            elif self.menu.botonRegresar.isOver(posicionMouse):
                self.menu.enPantallaInicio = True
                self.menu.enDificultad = False


    def dibujarJuego(self):
        self.pantallaJuego.dibujarTablero()
        self.dibujarPuzzles()
        self.dibujarPiezas()


    def tirarDado(self):
        self.pantallaJuego.dado.tirarDado()

    #en realidad lo que hace es ejecutar una accion disparada con alguna tecla  
    def ejecutarAccion(self, movimiento):
        
        #debo verificar que tecla es, para saber que accion se realizara

        #la ronda no esta iniciada y se presiono la tecla de iniciar?:
        #  iniciarRonda

        if self.enRonda == False and movimiento == pygame.K_CAPSLOCK:
            self.iniciarRonda()
        
        for i in range(self.numeroJugadores):

            if self.jugadores[i].movimientoFicha == False:
                #si ningun jugador ha presionado una tecla, continuar
                if not self.jugadores[i].moverPieza(movimiento):
                    continue
                self.jugadores[i].validarColision()
                #supongo que aqui tambien tengo que ver lo del movimiento de los peones
            else:
                self.jugadores[i].moverFicha(movimiento)

    def iniciarRonda(self):

        self.enRonda = True
        #       tirar dado
        self.tirarDado()

        #       obtener el puzzle de encima del monticulo
        for i in range(self.numeroJugadores):
            self.jugadores[i].puzzleSeleccionado = copy.copy(self.jugadores[i].puzzles[0])
            self.jugadores[i]._puzzleSeleccionadoForma = copy.deepcopy(self.jugadores[i].puzzleSeleccionado.forma)

        #       obtener las piezas de la cartilla segun el dado
        self.asignarPiezas()


        #       resolver (con tiempo)
        #       el que ya haya completado su puzzle, podrá mover su ficha X espacios
        #       mover fichaJugador
        #       comenzar nueva ronda
        return


