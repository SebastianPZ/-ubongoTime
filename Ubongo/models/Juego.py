import pygame
import random as random
from models.menu import Menu
from models.Dado import Dado
from models.Puzzle import Puzzle

class Juego():
    def __init__(self, window):
        self.menu = Menu(window)
        self.tablero = None
        self.jugadores = None
        self.numeroRonda = 0
        self.dado = None
        self.temporizador = None
        self.mazoPuzzles = []
        self.dificultad = None
        self.window = window
        self.numeroJugadores = 0
        self.enJuego = False
        self.enMenu = True

    def asignarPuzzles(self, dificultad):
        puzzles = []
        idPuzzle = 0
        for i in range(len(self.jugadores)):
            for _ in range(9):
                if dificultad == "Normal":
                   idPuzzle = random.randint(0,37)
                elif dificultad == "Difícil":
                   idPuzzle = random.randint(38,74)

                puzzleImage = pygame.image.load('../assets/Puzzles/Puzzle ' + str(idPuzzle) + '.png')
                puzzleGenerado = Puzzle(self.window, 350, 550, 400, 300, puzzleImage, dificultad, )
                self.jugadores[i].puzzles.append(puzzleGenerado)


    def asignarFichas(self):
        return None

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




