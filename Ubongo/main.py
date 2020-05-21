import pygame
from models.menu import Menu
mesa = pygame.image.load('assets/Fondos/fondo mesa.png')
pygame.init()
window = pygame.display.set_mode((1600, 900))

pygame.display.set_caption("Prueba")
run = True
menu = Menu(window)

def dibujarPantallaInicio(window):
    window.blit(mesa, (0, 0))
    menu.dibujarMenu()


dibujarPantallaInicio(window)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    dibujarPantallaInicio(window)
    pygame.display.update()















