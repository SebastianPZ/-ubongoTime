import pygame
from models.componente import Componente
from models.boton import Boton
logo = pygame.image.load('assets/Acciones/ubongo logo1.png')
menu = pygame.image.load('assets/Fondos/fondoUbongo.jpg')
widthMenu = menu.get_rect().width
heightMenu = menu.get_rect().height
sub = logo.subsurface((0, 1000 // 3, 1000, 1000 // 3))

class Menu(Componente):
    def __init__(self, window, width = widthMenu, height = heightMenu):
        Componente.__init__(self, window.get_rect().width / 2 - width / 2, window.get_rect().height / 2 - height / 2, width, height)
        self.window = window
        self.logoRect = logo.get_rect()
        self.botonIniciar = None
        self.botonDificultad = None
        self.botonUnJugador = None
        self.botonDosJugadores = None
        self.botonTresJugadores = None
        self.botonDificultadNormal = None
        self.botonDificultadDificil = None
        self.sobreBotonIniciar = False
        self.sobreBotonDificultad = False



    def dibujarMenuPrincipal(self):
        self.window.blit(menu, (self.x, self.y))
        xLogo = (2*self.x + self.width)/2 - self.logoRect.width/2
        yLogo = (2*self.y + self.height)/ 2 - self.logoRect.height / 2 - 100
        self.window.blit(logo, (xLogo, yLogo))
        if not self.sobreBotonIniciar:
            self.botonIniciar = Boton((0, 0, 0), (255, 255, 255), (2*self.x + self.width)/2 - 250/2, yLogo + self.logoRect.height/3 + self.height / 2, 250, 70,
                             "Iniciar juego")
        else:
            self.botonIniciar = Boton((127, 127, 127), (0, 0, 0), (2 * self.x + self.width) / 2 - 250 / 2,
                                      yLogo + self.logoRect.height / 3 + self.height / 2, 250, 70,
                                      "Iniciar juego")

        if not self.sobreBotonDificultad:
            self.botonDificultad = Boton((0, 0, 0), (255, 255, 255), self.botonIniciar.x,
                                         self.botonIniciar.y + self.botonIniciar.height + 40,
                                         250, 70, "Dificultad")
        else:
            self.botonDificultad = Boton((127, 127, 127), (0, 0, 0), self.botonIniciar.x,
                                         self.botonIniciar.y + self.botonIniciar.height + 40,
                                         250, 70, "Dificultad")

        self.botonIniciar.draw(self.window)
        self.botonDificultad.draw(self.window)

    def dibujarMenuJugadores(self):
        self.window.blit(menu, (self.x, self.y))
        xLogo = (2 * self.x + self.width) / 2 - self.logoRect.width / 2
        yLogo = (2 * self.y + self.height) / 2 - self.logoRect.height / 2 - 100
        self.window.blit(logo, (xLogo, yLogo))
        self.botonUnJugador = Boton((0, 0, 0), (255, 255, 255), (2*self.x + self.width)/2 - 250/2, yLogo + self.logoRect.height/3 + self.height / 3, 250, 70,
                             "1 Jugador")
        self.botonDosJugadores = Boton((0, 0, 0), (255, 255, 255), self.botonUnJugador.x, self.botonUnJugador.y + 25, 250, 70,
                             "2 Jugadores")
        self.botonTresJugadores = Boton((0, 0, 0), (255, 255, 255), self.botonDosJugadores.x, self.botonDosJugadores.y + 25, 250, 70,
                             "3 Jugadores")
        self.botonUnJugador.draw(self.window)
        self.botonDosJugadores.draw(self.window)
        self.botonTresJugadores.draw(self.window)
