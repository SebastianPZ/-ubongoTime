import pygame
from models.menu import Menu
mesa = pygame.image.load('assets/Fondos/fondo mesa.png')
pygame.init()
window = pygame.display.set_mode((1600, 900))

pygame.display.set_caption("Prueba")
run = True
menu = Menu(window)
enPantallaDeInicio = True
enPantallaSeleccionJugadores = False
enPantallaSeleccionDificultad = False
enJuego = False

def dibujarMesa(window):
    window.blit(mesa, (0, 0))

def dibujarPantallaInicio(window):
    menu.dibujarMenuPrincipal()

def dibujarPantallaSeleccionJugadores(window):
    menu.dibujarMenuJugadores()

def dibujarPantallaDeJuego(window):
    font = pygame.font.SysFont('comicsans', 70)
    text = font.render("PUTO EL QUE LO LEA :V", 1, (0, 0, 0))
    window.blit(text, (580, 400))

def validarHoverEnPantallaInicio(menu, pos):
    if menu.botonIniciar.isOver(pos):
        menu.sobreBotonIniciar = True
    elif menu.botonDificultad.isOver(pos):
        menu.sobreBotonDificultad = True
    else:
        menu.sobreBotonIniciar = False
        menu.sobreBotonDificultad = False



while run:

    dibujarMesa()
    if enPantallaDeInicio:
        dibujarPantallaInicio(window)
    elif enJuego:
        dibujarPantallaDeJuego(window)
    pygame.display.update()

    for event in pygame.event.get():

        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEMOTION:
            if enPantallaDeInicio:
                validarHoverEnPantallaInicio(menu, pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if enPantallaDeInicio:
                if menu.botonIniciar.isOver(pos):
                    enPantallaSeleccionJugadores = True
                    enPantallaDeInicio = False
                    print(enJuego)
                    print(enPantallaDeInicio)
                elif menu.botonDificultad.isOver(pos):
                    print("Juanelv es puto")















