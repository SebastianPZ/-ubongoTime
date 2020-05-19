import pygame, time

mesa = pygame.image.load('assets/Fondos/fondo mesa.png')
menu = pygame.image.load('assets/Fondos/fondoUbongo.jpg')

pygame.init()
window = pygame.display.set_mode((1600, 900))

pygame.display.set_caption("Prueba")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.time.delay(100)
    pygame.draw.circle(window, (255, 0, 0), (80, 80), 14)
    window.blit(mesa, (0, 0))
    window.blit(menu, (184, 100))
    pygame.display.update()


pygame.quit()  