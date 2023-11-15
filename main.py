import pygame
from menu import *
from pantalla_final import *
from nivel_1 import *
from nivel_2 import *
from nivel_3 import *
from leaderborads import *
from menu_niveles import *
from victoria import *


def main():
    pygame.init()
    #PANTALLA
    ancho_pantalla = 1200
    alto_pantalla = 600
    medidas_pantalla = (ancho_pantalla, alto_pantalla)
    pantalla = pygame.display.set_mode(medidas_pantalla)

    estado = "menu_principal"
    puntaje = {}
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if estado == "menu_principal":
            estado = mostrar_menu_principal(medidas_pantalla)
        elif estado == "nivel_1":  
            estado, puntaje = nivel_1()
        elif estado == "nivel_2":  
            estado, puntaje = nivel_2()
        elif estado == "nivel_3":
            estado, puntaje = nivel_3()
        elif estado == "pantalla_puntaje":
            estado = mostrar_pantalla_final(medidas_pantalla, puntaje)
        elif estado == "leaderboards":
            estado = leaderbord(medidas_pantalla)
        elif estado == "niveles":
            estado = niveles(medidas_pantalla)
        elif estado == "victoria":
            estado = victoria(medidas_pantalla)
        elif estado == "exit":
            running = False
            break

    pygame.quit()

if __name__ == "__main__":
    main()
