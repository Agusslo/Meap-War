import pygame
from pygame.locals import *
from constantes import *

pygame.init()

def mostrar_menu_principal(medidas_pantalla):
    '''brief: configuracion del menu principal'''
    pantalla = pygame.display.set_mode(medidas_pantalla)
    pygame.display.set_caption("Meap War")
    clock = pygame.time.Clock()
    ruta_fuente = 'recursos\Planes_ValMore.ttf'

    # Tamaño de los botones
    tamaño_fuente_botones = 46
    ancho_boton = 100
    alto_boton = 30
    separacion_botones = 50
    posicion_x = (medidas_pantalla[0] - ancho_boton) // 2
    posicion_1 = ((medidas_pantalla[1] - (alto_boton + separacion_botones) * 3) // 2) + separacion_botones * 3
    posicion_2 = posicion_1 + separacion_botones
    posicion_3 = posicion_2 + separacion_botones
    posicion_4 = posicion_3 + separacion_botones

    # Música
    pygame.mixer.music.load("recursos\sonidos\elevador.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)

    # Fondo en movimiento
    scroll = 0
    bg_images = []
    for i in range(2, 6):
        bg_image = pygame.image.load(f"recursos\menu_principal\layers\\{i}.png").convert_alpha()
        bg_image = pygame.transform.scale(bg_image, medidas_pantalla)
        bg_images.append(bg_image)

    fondo_base = pygame.image.load("recursos\menu_principal\layers\\1.png").convert_alpha()
    fondo_base = pygame.transform.scale(fondo_base, medidas_pantalla)

    # Mouse
    new_mouse = pygame.image.load("recursos\mouse.png")
    new_mouse = pygame.transform.scale(new_mouse, (30, 30))

    # Título
    tamano_fuente = 200
    crecimiento = 1

    pygame.mouse.set_visible(False)

    running = True
    while running:
        clock.tick(60)

        # Fondo
        pantalla.blit(fondo_base, (0, 0))
        for x in range(10000):
            speed = 1
            for i in bg_images:
                pantalla.blit(i, ((x * medidas_pantalla[0]) - scroll * speed, 0))
                speed += 0.3
        scroll += 5

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if boton_1.collidepoint(mouse_pos):
                    tamaño_fuente_botones = 66
                    return "nivel_1"
                if boton_2.collidepoint(mouse_pos):
                    return "leaderboards"
                if boton_3.collidepoint(mouse_pos):
                    return "niveles"
                if boton_4.collidepoint(mouse_pos):
                    return "exit"

        # Boton 1(Play)
        boton_1 = pygame.Rect(posicion_x, posicion_1, ancho_boton, alto_boton)
        if boton_1.collidepoint(mouse_pos):
            tamaño_fuente_botones = 66
        else:
            tamaño_fuente_botones = 45
        fuente = pygame.font.Font(ruta_fuente, tamaño_fuente_botones)
        texto = fuente.render("Play", True, (WHITE))
        text_rect = texto.get_rect(center=(medidas_pantalla[0] // 2, posicion_1 + alto_boton // 2))
        pantalla.blit(texto, text_rect)

        # Boton 2(learboard)
        boton_2 = pygame.Rect(posicion_x - 100, posicion_2, ancho_boton * 3, alto_boton)
        if boton_2.collidepoint(mouse_pos):
            tamaño_fuente_botones = 66
        else:
            tamaño_fuente_botones = 45
        fuente = pygame.font.Font(ruta_fuente, tamaño_fuente_botones)
        texto = fuente.render("Leaderboards", True, (WHITE))
        text_rect = texto.get_rect(center=(medidas_pantalla[0] // 2, posicion_2 + alto_boton // 2))
        pantalla.blit(texto, text_rect)

        # Boton 3 (Niveles)
        boton_3 = pygame.Rect(posicion_x, posicion_3, ancho_boton, alto_boton)
        if boton_3.collidepoint(mouse_pos):
            tamaño_fuente_botones = 66
        else:
            tamaño_fuente_botones = 45
        fuente = pygame.font.Font(ruta_fuente, tamaño_fuente_botones)
        texto = fuente.render("Niveles", True, (ORANGE))
        text_rect = texto.get_rect(center=(medidas_pantalla[0] // 2, posicion_3 + alto_boton // 2))
        pantalla.blit(texto, text_rect)



        # Boton 4 (Exit)
        boton_4 = pygame.Rect(posicion_x, posicion_4, ancho_boton, alto_boton)
        if boton_4.collidepoint(mouse_pos):
            tamaño_fuente_botones = 66
        else:
            tamaño_fuente_botones = 45
        fuente = pygame.font.Font(ruta_fuente, tamaño_fuente_botones)
        texto = fuente.render("Exit", True, (WHITE))
        text_rect = texto.get_rect(center=(medidas_pantalla[0] // 2, posicion_4 + alto_boton // 2))
        pantalla.blit(texto, text_rect)


        # Titulo
        fuente = pygame.font.Font(ruta_fuente, tamano_fuente)
        titulo = fuente.render("Meap War", True, (BLACK))
        titulo_rect = titulo.get_rect(center=(medidas_pantalla[0] // 2, medidas_pantalla[1] // 4))
        pantalla.blit(titulo, titulo_rect)

        fuente = pygame.font.Font(ruta_fuente, 25)
        texto = fuente.render("Todos los derechos reservados para Agustin Lopez.", True, (WHITE))
        pantalla.blit(texto, (0, medidas_pantalla[1] - 25))

        tamano_fuente += crecimiento

        # Invierte la dirección del cambio de tamaño si se alcanza un límite
        if tamano_fuente >= 210 or tamano_fuente <= 190:
            crecimiento = -crecimiento

        # Mouse
        pos = pygame.mouse.get_pos()
        pantalla.blit(new_mouse, pos)

        pygame.display.update()

    pygame.quit()
