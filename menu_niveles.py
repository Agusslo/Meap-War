import pygame
from constantes import *
from menu import * 

pygame.init()

def niveles(medidas_pantalla):
    '''brief: configuracion de la pantalla para seleccionar el nivel'''
    pygame.init()
    pantalla = pygame.display.set_mode(medidas_pantalla)
    pygame.display.set_caption("Menu de Niveles")
    
    niveles_disponibles = ["Nivel 1", "Nivel 2", "Nivel 3"]
    seleccion = 0  

    fondo = pygame.image.load("recursos/menu_principal/fondo_niveles.jpg") 
    fondo = pygame.transform.scale(fondo, medidas_pantalla)
    
    #musica
    pygame.mixer.music.load("recursos\sonidos\menu_espera.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(niveles_disponibles)
                elif event.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(niveles_disponibles)
                elif event.key == pygame.K_RETURN:
                    if seleccion == 0:
                        return "nivel_1"
                    elif seleccion == 1:
                        return "nivel_2"
                    elif seleccion == 2:
                        return "nivel_3"
                if event.key == pygame.K_F2:
                    mostrar_menu_principal(medidas_pantalla)
        pantalla.blit(fondo, (0, 0))  # Dibuja el fondo en la pantalla.
        fuente = pygame.font.Font(None, 36)
        for i, nivel in enumerate(niveles_disponibles):
            if i == seleccion:
                texto = fuente.render(f"> {nivel} <", True, (BLACK))
            else:
                texto = fuente.render(nivel, True, (BLACK))
            pantalla.blit(texto, (100, 100 + i * 50))

        pygame.display.flip()
    pygame.quit()
