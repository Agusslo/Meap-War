import pygame
from constantes import *
from menu import *
from crear_csv import *

pygame.init()

def victoria(medidas_pantalla):
    '''brief: configuracion de la pantalla final para la victoria'''
    pygame.init()
    pantalla = pygame.display.set_mode(medidas_pantalla)
    pygame.display.set_caption("VICTORIA!!")

    fondo = pygame.image.load("recursos/menu_principal/victoria.jpg")
    fondo = pygame.transform.scale(fondo, medidas_pantalla)

    # Score
    score_archivo = recuperar_puntaje("puntajes.csv")

    # música
    pygame.mixer.music.load("recursos\sonidos\menu_espera.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)

    fuente_grande = pygame.font.Font(None, 96)
    fuente_puntaje = pygame.font.Font(None, 40)
    texto_victoria = fuente_grande.render("¡Felicidades, has ganado el juego!", True, (WHITE))
    texto_puntaje = fuente_puntaje.render(f"Puntaje del juego: {score_archivo}", True, (LIGHT_YELLOW))
    
    rect_texto = texto_victoria.get_rect(center=(medidas_pantalla[0] // 2, medidas_pantalla[1] // 4))
    rect_puntaje = texto_puntaje.get_rect(topleft=(20, medidas_pantalla[1] - 80))

    # Opciones de menú
    opciones = ["Volver al Menú Principal"]
    seleccion = 0

    running = True
    while running:
        eventos = pygame.event.get()
        for event in eventos:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # enter
                    if seleccion == 0:
                        return "menu_principal"

        pantalla.blit(fondo, (0, 0))
        pantalla.blit(texto_victoria, rect_texto)
        pantalla.blit(texto_puntaje, rect_puntaje)

        # mini menu
        fuente = pygame.font.Font(None, 36)
        for i, opcion in enumerate(opciones):
            if i == seleccion:
                texto = fuente.render(f"> {opcion} <", True, (WHITE))
            else:
                texto = fuente.render(opcion, True, (WHITE))
            pantalla.blit(texto, (100, 400 + i * 50))

        pygame.display.flip()

    pygame.quit()
