import pygame
from configuraciones import *
from pygame.locals import *
from class_personaje import *
from modo import *
from nivel_2 import *
from class_plataforma import *
from class_proyectil import *
from class_enemigo import *
from class_portal import *
from constantes import *






def nivel_3():
    '''brief: configuraciones del nivel 3'''
    pygame.init()
    #PANTALLA
    ancho_pantalla = 1250
    alto_pantalla = 650
    medidas_pantalla = (ancho_pantalla, alto_pantalla)
    pantalla = pygame.display.set_mode(medidas_pantalla)
    #FONDO
    fondo = pygame.image.load("recursos\\space_boss.jpg")
    fondo = pygame.transform.scale(fondo,medidas_pantalla)
    
    #RELOJ
    FPS = 60
    reloj = pygame.time.Clock()

    #ICONO
    pygame.display.set_caption("Meap War")

    #BOTONES PAUSA
    ancho_boton = 500
    alto_boton = 60
    posicion_x = medidas_pantalla[0] // 2 - ancho_boton // 2
    posicion_2 = medidas_pantalla[1] - alto_boton - 80

    #MUSICA
    pygame.mixer.music.load("recursos\sonidos\phonk.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    musica_pausada = False


    #SCORE
    timer = pygame.USEREVENT
    pygame.time.set_timer(timer, 1000)
    secs_in_game = 0
    puntaje = 0
    ruta_fuente = 'recursos\Planes_ValMore.ttf'
    nivel_terminado = False

    #PAUSA
    ultima_imagen = None
    pausa = False

    #ITEMS
    medidas_moneda = (20,20)
    lista_monedas = []
    medidas_portal = (100,100)
    posicion_portal = (1000, 1000)#lo saco fuera de la pantalla
    portal_terminar_nivel = Portal(medidas_portal, posicion_portal)

    #PLATAFORMAS
    #(derecha/izquierda,arriba/abajo)
    medidas_base = (ancho_pantalla, 50)
    path_base = "recursos\plataformas\\tiles.png"
    #base
    lugar_base = (ancho_pantalla/2, alto_pantalla)
    base = Plataforma(medidas_base, path_base ,lugar_base)
    #plataforma 1
    medidas_plataformas = (1200,30)
    lugar_p1 = (650, 640)#(650, 640)
    p_1 = Plataforma(medidas_plataformas, path_base, lugar_p1)
    #plataforma 2
    medidas_plataformas_2 = (150,30)
    lugar_p2 = (300, 550)
    p_2 = Plataforma(medidas_plataformas_2, path_base, lugar_p2)
    #plataforma 3
    medidas_plataformas_3 = (150,30)
    lugar_p3 = (450, 460)
    p_3 = Plataforma(medidas_plataformas_3, path_base, lugar_p3)
    #plataforma 3
    medidas_plataformas_4 = (150,30)
    lugar_p4 = (230, 350)
    p_4 = Plataforma(medidas_plataformas_4, path_base, lugar_p4)
    #plataforma 5
    medidas_plataformas_5 = (150,30)
    lugar_p5 = (130, 250)
    p_5 = Plataforma(medidas_plataformas_5, path_base, lugar_p5)

    lista_plataformas_con_monedas = []

    for plataforma in lista_plataformas_con_monedas:
        monedas_plataforma = plataforma.generar_monedas(medidas_moneda)#class plataforma
        lista_monedas.extend(monedas_plataforma)

    lista_plataformas = [base,p_1,p_2,p_3,p_4,p_5]#para ver la plataforma


    #PERSONAJE
    posicion_inicial = (0,alto_pantalla-medidas_base[1] - 40)
    tamaño_personaje = (55,65)
    diccionario_animaciones = {}
    diccionario_animaciones["quieto_derecha"] = lista_quieto_derecha
    diccionario_animaciones["quieto_izquierda"] = lista_quieto_izquierda
    diccionario_animaciones["salta_derecha"] = lista_saltar
    diccionario_animaciones["salta_izquierda"] = lista_saltar_izquierda
    diccionario_animaciones["camina_derecha"] = lista_caminar_derecha
    diccionario_animaciones["camina_izquierda"] = lista_caminar_izquierda
    diccionario_animaciones["dispara_derecha"] = lista_disparar_derecha
    diccionario_animaciones["dispara_izquierda"] = lista_disparar_izquierda
    diccionario_animaciones["corre_derecha"] = lista_correr_derecha
    diccionario_animaciones["corre_izquierda"] = lista_correr_izquierda
    diccionario_animaciones["recibe_daño"] = lista_recibir_daño
    diccionario_animaciones["recibe_daño_izquierda"] = lista_recibir_daño_izquierda

    diccionarios_sonidos_personaje = sonidos_personaje

    velocidad_personaje = 6
    
    mi_personaje = Personaje(tamaño_personaje,diccionario_animaciones,posicion_inicial, velocidad_personaje, diccionarios_sonidos_personaje)

    #PROYECTIL
    path_proyectil = "recursos\piedra.png"
    lista_proyectiles = []


    #ENEMIGOS
    diccionario_animaciones_enemigo = {}
    diccionario_animaciones_enemigo["camina_derecha"] = lista_enemigo_tres_caminar_derecha
    diccionario_animaciones_enemigo["camina_izquierda"] = lista_enemigo_tres_caminar_izquierda
    diccionario_animaciones_enemigo["recibir_daño"] = lista_enemigo_tres_recibir_daño
    diccionario_animaciones_enemigo["recibir_daño_izquierda"] = lista_enemigo_tres_recibir_daño_izquierda = girar_imagen(lista_enemigo_tres_recibir_daño, True, False)
    diccionario_animaciones_enemigo["atacar"] = lista_enemigo_tres_atacar
    diccionario_animaciones_enemigo["atacar_izquierda"] = lista_enemigo_tres_atacar_izquierda 
    # diccionario_animaciones_enemigo["muere"] = lista_enemigo_muerto
    # diccionario_animaciones_enemigo["muere_izquierda"] = lista_enemigo_muerto_izquierda

    #ENEMIGO 1
    velocidad_enemigo_1 = 13
    tamaño_enemigo_1 = (300,300)
    puntuacion_enemigo_1 = 3000
    vida_enemigo_1 = 60#60
    enemigo_1 = Enemigo(tamaño_enemigo_1, diccionario_animaciones_enemigo,velocidad_enemigo_1, p_1, puntuacion_enemigo_1, vida_enemigo_1)
    

    lista_enemigos = [enemigo_1]

    run = True
    while run:
        if not pausa:
            pygame.mouse.set_visible(False)
            reloj.tick(FPS)
            pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F3:
                        cambiar_modo()
                    elif event.key == pygame.K_F4:
                        if musica_pausada:
                            pygame.mixer.music.unpause()
                            musica_pausada = False
                        else:
                            pygame.mixer.music.pause()
                            musica_pausada = True
                    elif event.key == pygame.K_ESCAPE:
                        pausa = not pausa
                        if musica_pausada:
                            pygame.mixer.music.unpause()
                            musica_pausada = False
                        else:
                            pygame.mixer.music.pause()
                            musica_pausada = True

            #ACTUALIZACION DE PANTALLA
            pantalla.blit(fondo,(0,0))
            for plataforma in lista_plataformas:
                pantalla.blit(plataforma.superficie,plataforma.rectangulo)
                #p_5.mover_plataforma(1,'x', 900, 200)   #MOVIMENTO DE PLATAFORMA

            mi_personaje.update(pantalla, lista_plataformas)
            nivel_terminado = portal_terminar_nivel.update(pantalla, mi_personaje)
            

            #MOVER PROYECTILES
            if mi_personaje.disparando and mi_personaje.puede_disparar:
                proyectil = Proyectil(path_proyectil, mi_personaje.direccion_disparo, mi_personaje)
                lista_proyectiles.append(proyectil)
                mi_personaje.disparando = False
                mi_personaje.puede_disparar = False

            for proyectil in lista_proyectiles:
                proyectil.mover()
                proyectil.detectar_piso(lista_plataformas)
                proyectil.desaparecer_proyectil()
                if not proyectil.ha_desaparecido:
                    pantalla.blit(proyectil.superficie, proyectil.rectangulo)
                else:
                    lista_proyectiles.remove(proyectil)

            #ENEMIGOS
            for enemigo in lista_enemigos:
                enemigo.update(pantalla, lista_proyectiles, mi_personaje)
                

            #MODO HITBOX
            if get_modo():
                for plataforma in lista_plataformas:
                    plataforma.dibujar_hitbox(pantalla)
                for proyectil in lista_proyectiles:
                    proyectil.dibujar_hitbox(pantalla)
                mi_personaje.dibujar_hitbox(pantalla)
                enemigo_1.dibujar_hitbox(pantalla)

            #MONEDAS
            for moneda in lista_monedas:
                if not moneda.obtenida:
                    moneda.update(pantalla, mi_personaje)
            

            #PUNTAJE
            fuente = pygame.font.Font(ruta_fuente, 36)
            score_archivo = recuperar_puntaje("puntajes.csv")
            score_archivo+=mi_personaje.score
            texto_puntaje = fuente.render("Puntaje: " + str(score_archivo), True, (WHITE))
            pantalla.blit(texto_puntaje, (20, 15))

            #CRONOMETRO
            minutos = secs_in_game // 60
            segundos = secs_in_game % 60

            minutos_str = str(minutos)
            segundos_str = str(segundos)

            minutos_str = minutos_str.zfill(2)
            segundos_str = segundos_str.zfill(2)

            tiempo_str = minutos_str + ":" + segundos_str

            # Renderiza el tiempo en la pantalla
            texto_tiempo = fuente.render("Tiempo: " + tiempo_str, True, (WHITE))
            pantalla.blit(texto_tiempo, (20, 50))

            #TEXTO DEFEAT HIM
            fuente_defeat = pygame.font.Font(ruta_fuente, 72)
            texto_defeat = fuente_defeat.render("DEFEAT HIM", True, (255, 0, 0))  
            pantalla.blit(texto_defeat, (400, 100))

    #CONFIGURACION NIVEL TERMINADO
            dict_puntaje = {}
            if secs_in_game != 0:
                bonus_tiempo = (mi_personaje.score / secs_in_game) * 10
            else:
                bonus_tiempo = 0
            puntaje_total = mi_personaje.score + bonus_tiempo + score_archivo
            dict_puntaje["bonus_tiempo"] = bonus_tiempo
            dict_puntaje["puntaje_juego"] = score_archivo#mi_personaje.score
            dict_puntaje["puntaje_final"] = puntaje_total

#NIVEL TERMINADO CUANDO MUERO
            if mi_personaje.vida <= 0:
                return "pantalla_puntaje", dict_puntaje

#NIVEL TERMINADO CUANDO MATO AL BOSS
            if enemigo.muerto:
                puntaje_total = int(puntaje_total)
                guardar_puntaje("puntajes.csv", puntaje_total)
                return "pantalla_puntaje", dict_puntaje
            pygame.display.flip()
        else:
            pygame.mouse.set_visible(True)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pausa = not pausa
                        if musica_pausada:
                            pygame.mixer.music.unpause()
                            musica_pausada = False
                        else:
                            pygame.mixer.music.pause()
                            musica_pausada = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if boton_volver.collidepoint(event.pos):
                        return "menu_principal", 0
                    if boton_reiniciar.collidepoint(event.pos):
                        return "nivel_3", 0

            fuente_pausa = pygame.font.Font(ruta_fuente, 72)
            texto_pausa = fuente_pausa.render("Pause", True, (LIGHT_YELLOW))
            pantalla.blit(texto_pausa, (ancho_pantalla // 2 -150, alto_pantalla // 2-150))

            tamaño_fuente_boton = 46
            separacion_botones = 15
            
            #boton menu pruncipal
            boton_volver = pygame.Rect(posicion_x - ancho_boton - separacion_botones + 100, posicion_2, ancho_boton + 40, alto_boton)
            fuente = pygame.font.Font(ruta_fuente, tamaño_fuente_boton)
            texto_volver_principal = fuente.render("Volver al menu", True,(LIGHT_YELLOW))
            text_rect_volver_principal = texto_volver_principal.get_rect(center=(medidas_pantalla[0] // 2 - 270, posicion_2 + alto_boton // 2))
            pantalla.blit(texto_volver_principal, text_rect_volver_principal)
            

            #reiniciar nivel
            boton_reiniciar = pygame.Rect(posicion_x  + separacion_botones + 290, posicion_2, ancho_boton - 200, alto_boton)
            fuente = pygame.font.Font(ruta_fuente, tamaño_fuente_boton)
            texto_reiniciar = fuente.render("Reiniciar nivel", True, (LIGHT_YELLOW))
            text_rect_reiniciar = texto_reiniciar.get_rect(center=(medidas_pantalla[0] // 2 + 200, posicion_2 + alto_boton // 2))
            pantalla.blit(texto_reiniciar, text_rect_reiniciar)

            pygame.display.update()

    pygame.quit()

