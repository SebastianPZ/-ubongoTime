import pygame
import random as random

class Juego():
    def __init__(self, jugadores, dificultad):
        self.tablero = None
        self.jugadores = jugadores
        self.numeroRonda = 0
        self.dado = None
        self.temporizador = None
        self.mazoPuzzles = []
        self.dificultad = dificultad

    def asignarPuzzles(self, dificultad):
        puzzles = []
        indice = 0
        for i in range(9):
            while True:
                if dificultad == "facil" :
                    indice = random.randint(0,37)
                elif dificultad == "dificil":
                    indice = random.randint(38,74) 

                if self.mazoPuzzles[indice] != None:
                    puzzles.append(self.mazoPuzzles[indice])
                    self.mazoPuzzles[indice] = None
                    break
                    

        return puzzles

