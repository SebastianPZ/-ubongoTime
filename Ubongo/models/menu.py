import pygame
from models.componente import Componente
from models.utils.boton import Boton
from models.logo import Logo
logo = pygame.image.load('assets/Acciones/ubongo logo1.png')
menu = pygame.image.load('assets/Fondos/fondoUbongo.jpg')
widthMenu = menu.get_rect().width
heightMenu = menu.get_rect().height
sub = logo.subsurface((0, 1000 // 3, 1000, 1000 // 3))

class Menu(Componente):
    def __init__(self, window, width = widthMenu, height = heightMenu):
        Componente.__init__(self, window.get_rect().width / 2 - width / 2, window.get_rect().height / 2 - height / 2, width, height)
        self.window = window
        self.logo = Logo()
        self.logo.x = (2 * self.x + self.width) / 2 - self.logo.width / 2
        self.logo.y = (2 * self.y + self.height) / 2 - self.logo.height / 2 - 100
        self.botonIniciar = Boton((0, 0, 0), (255, 255, 255), (2*self.x + self.width)/2 - 250/2, self.logo.y + self.logo.height/3 + self.height / 2, 250, 70, "Iniciar juego")
        self.botonDificultad = Boton((0, 0, 0), (255, 255, 255), self.botonIniciar.x, self.botonIniciar.y + self.botonIniciar.height + 40, 250, 70, "Dificultad")
        self.botonUnJugador = Boton((0, 0, 0), (255, 255, 255), (2*self.x + self.width)/2 - 250/2, self.logo.y + self.logo.height/3 + self.height / 3 + 50, 250, 70, "1 Jugador")
        self.botonDosJugadores = Boton((0, 0, 0), (255, 255, 255), self.botonUnJugador.x, self.botonUnJugador.y + self.botonUnJugador.height + 25, 250, 70, "2 Jugadores")
        self.botonTresJugadores = Boton((0, 0, 0), (255, 255, 255), self.botonDosJugadores.x, self.botonDosJugadores.y + self.botonDosJugadores.height + 25, 250, 70, "3 Jugadores")
        self.botonDificultadNormal = Boton((0, 0, 0), (255, 255, 255), (2*self.x + self.width)/2 - 250/2, self.logo.y + self.logo.height/3 + self.height / 2, 250, 70, "Normal (3 piezas)")
        self.botonDificultadDificil = Boton((0, 0, 0), (255, 255, 255), self.botonDificultadNormal.x, self.botonDificultadNormal.y + self.botonDificultadNormal.height + 40, 250, 70, "Difícil (4 piezas)")
        self.botonRegresar = Boton((0, 0, 0), (255, 255, 255), 100, 100 , 250, 70, "Regresar")
        self.enPantallaInicio = True
        #enJugadores: variable que determina si estas en la pantalla de elegir jugadores o no
        self.enJugadores = False
        self.enDificultad = False

    def dibujarMenu(self):
        self.window.blit(menu, (self.x, self.y))
        self.logo.dibujarLogo(self.window)

    def dibujarBotones(self):
        if self.enPantallaInicio:
            self.botonIniciar.draw(self.window)
            self.botonDificultad.draw(self.window)
        elif self.enJugadores:
            self.botonUnJugador.draw(self.window)
            self.botonDosJugadores.draw(self.window)
            self.botonTresJugadores.draw(self.window)
            self.botonRegresar.draw(self.window)
        elif self.enDificultad:
            self.botonDificultadNormal.draw(self.window)
            self.botonDificultadDificil.draw(self.window)
            self.botonRegresar.draw(self.window)

    def validarHoverPosicionInicio(self, pos):
        if self.botonIniciar.isOver(pos):
            self.botonIniciar.hover((127, 127, 127), (0, 0, 0))
        elif self.botonDificultad.isOver(pos):
            self.botonDificultad.hover((127, 127, 127), (0, 0, 0))
        else:
            self.botonIniciar.setColores((0, 0, 0), (255, 255, 255))
            self.botonDificultad.setColores((0, 0, 0), (255, 255, 255))

    def validarHoverPosicionJugadores(self, pos):
        if self.botonUnJugador.isOver(pos):
            self.botonUnJugador.hover((127, 127, 127), (0, 0, 0))
        elif self.botonDosJugadores.isOver(pos):
            self.botonDosJugadores.hover((127, 127, 127), (0, 0, 0))
        elif self.botonTresJugadores.isOver(pos):
            self.botonTresJugadores.hover((127, 127, 127), (0, 0,0))
        else:
            self.botonUnJugador.setColores((0, 0, 0), (255, 255, 255))
            self.botonDosJugadores.setColores((0, 0, 0), (255, 255, 255))
            self.botonTresJugadores.setColores((0, 0, 0), (255, 255, 255))


    def validarHoverPosicionDificultad(self, pos):
        if self.botonDificultadNormal.isOver(pos):
            self.botonDificultadNormal.hover((127, 127, 127), (0, 0, 0))
        elif self.botonDificultadDificil.isOver(pos):
            self.botonDificultadDificil.hover((127, 127, 127), (0, 0, 0))
        else:
            self.botonDificultadNormal.setColores((0, 0, 0), (255, 255, 255))
            self.botonDificultadDificil.setColores((0, 0, 0), (255, 255, 255))

    def validarHoverPosicionRegresar(self, pos):
        if self.botonRegresar.isOver(pos):
            self.botonRegresar.hover((127, 127, 127), (0, 0, 0))
        else:
            self.botonRegresar.setColores((0, 0, 0), (255, 255, 255))

    def hoverBotonesMenu(self, pos):

        if self.enPantallaInicio:
            self.validarHoverPosicionInicio(pos)
        elif self.enJugadores:
            self.validarHoverPosicionJugadores(pos)
            self.validarHoverPosicionRegresar(pos)
        elif self.enDificultad:
            self.validarHoverPosicionDificultad(pos)
            self.validarHoverPosicionRegresar(pos)
            


