import pygame
import random as random
from models.menu import Menu
from models.factory.PuzzleFactory import PuzzleFactory
from models.factory.PiezaFactory import PiezaFactory
from models.Dado import Dado
from models.Puzzle import Puzzle

class Juego():

    def __init__(self, window):
        self.window = window
        self.menu = Menu(window)
        self.tablero = None
        self.jugadores = []
        self.numeroRonda = 0
        self.dado = Dado(300, 300, 100, 100, self.window)
        self.temporizador = None
        self.mazoPuzzles = []
        self.dificultad = None
        self.numeroJugadores = 0
        self.enJuego = False
        self.enMenu = True

    def setJugadores(self, numeroJugadores):
        self.numeroJugadores = numeroJugadores

    def asignarPuzzles(self, dificultad):
        idPuzzle = 0
        x = 0
        y = 550
        espaciado = 0
        if self.numeroJugadores == 2:
            x = 350
            espaciado = 850
        elif self.numeroJugadores == 3:
            x = 250
            espaciado = 650
        elif self.numeroJugadores == 4:
            x = 175
            espaciado = 450
        for i in range(self.numeroJugadores):
            if i != 0:
                x += espaciado
            for _ in range(9):
                if dificultad == "Normal":
                   idPuzzle = random.randint(0,37)
                elif dificultad == "Difícil":
                   idPuzzle = random.randint(38,74)
                puzzleGenerado = PuzzleFactory.crearPuzzle(x, y, idPuzzle, self.window, dificultad)
                self.jugadores[i].puzzles.append(puzzleGenerado)
            self.jugadores[i].puzzleSeleccionado = self.jugadores[i].puzzles[0]

    def dibujarPuzzles(self):
        for i in range(self.numeroJugadores):
            self.jugadores[i].puzzles[self.numeroRonda].dibujarPuzzle()

    def asignarPiezas(self):
        x = 200
        espaciadoPiezas = 20
        y = 770
        espaciadoJugador = 0
        if self.numeroJugadores == 2:
            espaciadoJugador = 850
        elif self.numeroJugadores == 3:
            espaciadoJugador = 650
        elif self.numeroJugadores == 4:
            espaciadoJugador = 450
        for i in range(self.numeroJugadores):
            if i != 0:
                x += espaciadoJugador
            jugador = self.jugadores[i]
            codigosPiezas = jugador.puzzles[jugador.puzzleSeleccionado].piezas[self.dado.posicion]
            for j in range(len(codigosPiezas)):
                if j != 0:
                    x += espaciadoPiezas
                jugador.piezas.append(PiezaFactory.crearPieza(x, y, codigosPiezas[i], self.window))

    def dibujarPiezas(self):
        for i in range(self.numeroJugadores):
            for j in range(len(self.jugadores[i].piezas)):
                self.jugadores[i].piezas[j].dibujarPieza()

    def dibujarMenu(self):
        if self.enMenu:
            self.menu.dibujarMenu()
            self.menu.dibujarBotones()

    def hoverBotonesMenu(self, pos):

        if self.menu.enPantallaInicio:
            self.menu.validarPosicionInicio(pos)
        elif self.menu.enJugadores:
            self.menu.validarPosicionJugadores(pos)
        elif self.menu.enDificultad:
            self.menu.validarPosicionDificultad(pos)

    def transicionarMenu(self, posicionMouse):

        if self.menu.enPantallaInicio:
            if self.menu.botonIniciar.isOver(posicionMouse):
                self.menu.enPantallaInicio = False
                self.menu.enJugadores = True
            elif self.menu.botonDificultad.isOver(posicionMouse):
                self.menu.enPantallaInicio = False
                self.menu.enDificultad = True

        elif self.menu.enJugadores:
            if self.menu.botonUnJugador.isOver(posicionMouse):
                self.menu.enJugadores = False
                self.numeroJugadores = 1
                self.enJuego = True
                self.enMenu = False
            elif self.menu.botonDosJugadores.isOver(posicionMouse):
                self.menu.enJugadores = False
                self.numeroJugadores = 2
                self.enJuego = True
                self.enMenu = False
            elif self.menu.botonTresJugadores.isOver(posicionMouse):
                self.menu.enJugadores = False
                self.numeroJugadores = 3
                self.enJuego = True
                self.enMenu = False

        elif self.menu.enDificultad:
            if self.menu.botonDificultadNormal.isOver(posicionMouse):
                self.menu.enDificultad = False
                self.menu.enPantallaInicio = True
                self.dificultad = "Normal"
            elif self.menu.botonDificultadDificil.isOver(posicionMouse):
                self.menu.enDificultad = False
                self.menu.enPantallaInicio = True
                self.dificultad = "Difícil"




