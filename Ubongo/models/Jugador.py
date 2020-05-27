import pygame

class Jugador():

    def __init__(self, id, puzzles):
        self.id = id
        self.piezas = None
        self.piezaSeleccionada = None
        self.puzzles = puzzles 
        self.puzzleSeleccionado = None
        self.ficha = None
        self.gemas = None
    
