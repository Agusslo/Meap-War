import pygame

pygame.mixer.init()

def reescalar_imagen(lista_imagen, tamaño):
    '''brief: rescala las imagenes'''
    for i in range(len(lista_imagen)):
        lista_imagen[i] = pygame.transform.scale(lista_imagen[i], tamaño)



def girar_imagen(lista_original, flip_x, flip_y):
    '''brief: flip de la lista que pase'''
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen,flip_x,flip_y))
    return lista_girada


# RECTANGULO #---------------------------------------------------------------------------------------------

def obtener_rectangulos(principal)->dict:
    '''brief: obtiene los lados de los rectangulos'''
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right -10, principal.top, 10, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 10, principal.height)
    diccionario["top"] = pygame.Rect(principal.left,principal.top, principal.width, 10)
    return diccionario

#---------------------------------------------------------------------------------------------------------



#SONIDOS PARA EL PERSONAJE--------------------------------------------------------------------------------

sonidos_personaje = {}
sonidos_personaje["caer"] = pygame.mixer.Sound("recursos\sonidos\caer.wav")
sonidos_personaje["tirar"] = pygame.mixer.Sound("recursos\sonidos\\tirar.wav")

#---------------------------------------------------------------------------------------------------------


# LISTAS DE LAS IMAGENES PARA LAS ANIMACIONES#------------------------------------------------------------

lista_caminar_derecha = [
    pygame.image.load("recursos\caminar_derecha\\0.png"),
    pygame.image.load("recursos\caminar_derecha\\1.png"),
    pygame.image.load("recursos\caminar_derecha\\2.png"),
    pygame.image.load("recursos\caminar_derecha\\3.png"),
    pygame.image.load("recursos\caminar_derecha\\4.png"),
    pygame.image.load("recursos\caminar_derecha\\5.png")
]

lista_correr_derecha = [
    pygame.image.load("recursos\correr_derecha\\0.png"),
    pygame.image.load("recursos\correr_derecha\\1.png"),
    pygame.image.load("recursos\correr_derecha\\2.png"),
    pygame.image.load("recursos\correr_derecha\\3.png"),
    pygame.image.load("recursos\correr_derecha\\4.png"),
    pygame.image.load("recursos\correr_derecha\\5.png"),
    pygame.image.load("recursos\correr_derecha\\6.png"),
    pygame.image.load("recursos\correr_derecha\\7.png"),
    pygame.image.load("recursos\correr_derecha\\8.png"),
]

lista_saltar = [
    pygame.image.load("recursos\saltar\\0.png"),
    pygame.image.load("recursos\saltar\\1.png"),
    pygame.image.load("recursos\saltar\\2.png"),
    pygame.image.load("recursos\saltar\\3.png"),
    pygame.image.load("recursos\saltar\\4.png"),
    pygame.image.load("recursos\saltar\\5.png"),
    pygame.image.load("recursos\saltar\\6.png"),
    pygame.image.load("recursos\saltar\\7.png"),
    pygame.image.load("recursos\saltar\\8.png"),
]

lista_disparar_derecha = [
    pygame.image.load("recursos\\tirar_piedra_derecha\\0.png"),
    pygame.image.load("recursos\\tirar_piedra_derecha\\1.png"),
    pygame.image.load("recursos\\tirar_piedra_derecha\\2.png"),
    pygame.image.load("recursos\\tirar_piedra_derecha\\3.png")
]

lista_recibir_daño = [
    pygame.image.load("recursos\\recibir_daño\\0.png"),
    pygame.image.load("recursos\\recibir_daño\\0.png"),
    pygame.image.load("recursos\\recibir_daño\\0.png"),
    pygame.image.load("recursos\\recibir_daño\\0.png"),
    pygame.image.load("recursos\\recibir_daño\\0.png"),
    pygame.image.load("recursos\\recibir_daño\\0.png")]

lista_quieto_derecha = [pygame.image.load("recursos\Pink_Monster.png")]

lista_quieto_izquierda = girar_imagen(lista_quieto_derecha,True,False)

lista_caminar_izquierda = girar_imagen(lista_caminar_derecha, True,False)

lista_saltar_izquierda = girar_imagen(lista_saltar,True,False)

lista_disparar_izquierda = girar_imagen(lista_disparar_derecha, True, False)

lista_correr_izquierda = girar_imagen(lista_correr_derecha,True,False)

lista_recibir_daño_izquierda = girar_imagen(lista_recibir_daño, True, False)

#---------------------------------------------------------------------------------------------------------



#ANIMACIONES ENEMIGOS -----------------------------------------------------------------------------------

#ENEMIGO 1
lista_enemigo_caminar_izquierda = [
    pygame.image.load("enemigos\enemigo_1\caminar_izquierda\\0.png"),
    pygame.image.load("enemigos\enemigo_1\caminar_izquierda\\1.png"),
    pygame.image.load("enemigos\enemigo_1\caminar_izquierda\\2.png"),
    pygame.image.load("enemigos\enemigo_1\caminar_izquierda\\3.png"),
    pygame.image.load("enemigos\enemigo_1\caminar_izquierda\\4.png"),
    pygame.image.load("enemigos\enemigo_1\caminar_izquierda\\5.png")
]

lista_enemigo_caminar_derecha = girar_imagen(lista_enemigo_caminar_izquierda, True,False)

lista_enemigo_recibir_daño_izquierda = [
    pygame.image.load("enemigos\enemigo_1\\recibir_daño\\0.png"),
    pygame.image.load("enemigos\enemigo_1\\recibir_daño\\1.png"),
    pygame.image.load("enemigos\enemigo_1\\recibir_daño\\1.png"),
    pygame.image.load("enemigos\enemigo_1\\recibir_daño\\1.png"),
]

lista_enemigo_recibir_daño = girar_imagen(lista_enemigo_recibir_daño_izquierda, True,False)

lista_enemigo_atacar_izquierda = [
    pygame.image.load("enemigos\enemigo_1\\atacar\\0.png"),
    pygame.image.load("enemigos\enemigo_1\\atacar\\1.png"),
    pygame.image.load("enemigos\enemigo_1\\atacar\\2.png"),
    pygame.image.load("enemigos\enemigo_1\\atacar\\3.png"),
    pygame.image.load("enemigos\enemigo_1\\atacar\\4.png"),
    pygame.image.load("enemigos\enemigo_1\\atacar\\5.png")
]

lista_enemigo_atacar = girar_imagen(lista_enemigo_atacar_izquierda, True,False)

# lista_enemigo_muerto_izquierda = [
#     pygame.image.load("enemigos\enemigo_1\morir\\0.png"),
#     pygame.image.load("enemigos\enemigo_1\morir\\1.png"),
#     pygame.image.load("enemigos\enemigo_1\morir\\2.png"),
#     pygame.image.load("enemigos\enemigo_1\morir\\3.png"),
#     pygame.image.load("enemigos\enemigo_1\morir\\4.png"),
#     pygame.image.load("enemigos\enemigo_1\morir\\5.png"),
# ]
# lista_enemigo_muerto = girar_imagen(lista_enemigo_muerto_izquierda,True,False)

#ENEMIGO 2
lista_enemigo_dos_caminar_derecha = [
    pygame.image.load("enemigos\enemigo_2\caminar_derecha\\0.png"),
    pygame.image.load("enemigos\enemigo_2\caminar_derecha\\1.png"),
    pygame.image.load("enemigos\enemigo_2\caminar_derecha\\2.png"),
    pygame.image.load("enemigos\enemigo_2\caminar_derecha\\3.png"),
    pygame.image.load("enemigos\enemigo_2\caminar_derecha\\4.png"),
    pygame.image.load("enemigos\enemigo_2\caminar_derecha\\5.png")
]

lista_enemigo_dos_caminar_izquierda = girar_imagen(lista_enemigo_dos_caminar_derecha, True,False)

lista_enemigo_dos_recibir_daño_izquierda = [
    pygame.image.load("enemigos\enemigo_2\\recibir_daño\\0.png"),
    pygame.image.load("enemigos\enemigo_2\\recibir_daño\\1.png"),
    pygame.image.load("enemigos\enemigo_2\\recibir_daño\\1.png"),
    pygame.image.load("enemigos\enemigo_2\\recibir_daño\\1.png"),
]

lista_enemigo_dos_recibir_daño = girar_imagen(lista_enemigo_dos_recibir_daño_izquierda, True,False)

lista_enemigo_dos_atacar_izquierda = [
    pygame.image.load("enemigos\enemigo_2\\atacar\\0.png"),
    pygame.image.load("enemigos\enemigo_2\\atacar\\1.png"),
    pygame.image.load("enemigos\enemigo_2\\atacar\\2.png"),
    pygame.image.load("enemigos\enemigo_2\\atacar\\3.png"),
    pygame.image.load("enemigos\enemigo_2\\atacar\\4.png"),
    pygame.image.load("enemigos\enemigo_2\\atacar/5.png")
]

lista_enemigo_dos_atacar = girar_imagen(lista_enemigo_dos_atacar_izquierda, True,False)

# lista_enemigo_dos_muerto_izquierda = [
#     pygame.image.load("enemigos\enemigo_2\morir\\0.png"),
#     pygame.image.load("enemigos\enemigo_2\morir\\1.png"),
# ]
# lista_enemigo_dos_muerto = girar_imagen(lista_enemigo_dos_muerto_izquierda,True,False)

#ENEMIGO 3
lista_enemigo_tres_caminar_derecha = [
    pygame.image.load("enemigos\enemigo_3\caminar_derecha\\0.png"),
    pygame.image.load("enemigos\enemigo_3\caminar_derecha\\1.png"),
    pygame.image.load("enemigos\enemigo_3\caminar_derecha\\2.png"),
    pygame.image.load("enemigos\enemigo_3\caminar_derecha\\3.png"),
    pygame.image.load("enemigos\enemigo_3\caminar_derecha\\4.png"),
    pygame.image.load("enemigos\enemigo_3\caminar_derecha\\5.png"),
    pygame.image.load("enemigos\enemigo_3\caminar_derecha\\6.png")
]

lista_enemigo_tres_caminar_izquierda = girar_imagen(lista_enemigo_tres_caminar_derecha, True,False)

lista_enemigo_tres_recibir_daño_izquierda = [
    pygame.image.load("enemigos\enemigo_3\\recibir_daño\\0.png"),
    pygame.image.load("enemigos\enemigo_3\\recibir_daño\\1.png"),
    pygame.image.load("enemigos\enemigo_3\\recibir_daño\\1.png"),
    pygame.image.load("enemigos\enemigo_3\\recibir_daño\\1.png")
]

lista_enemigo_tres_recibir_daño = girar_imagen(lista_enemigo_tres_recibir_daño_izquierda, True,False)

lista_enemigo_tres_atacar_izquierda = [
    pygame.image.load("enemigos\enemigo_3\\atacar\\0.png"),
    pygame.image.load("enemigos\enemigo_3\\atacar\\1.png"),
    pygame.image.load("enemigos\enemigo_3\\atacar\\2.png"),
    pygame.image.load("enemigos\enemigo_3\\atacar\\3.png"),
    pygame.image.load("enemigos\enemigo_3\\atacar\\4.png"),
    pygame.image.load("enemigos\enemigo_3\\atacar/5.png"),
    pygame.image.load("enemigos\enemigo_3\\atacar\\6.png"),
    pygame.image.load("enemigos\enemigo_3\\atacar/7.png")
]

lista_enemigo_tres_atacar = girar_imagen(lista_enemigo_tres_atacar_izquierda, True,False)

# lista_enemigo_tres_muerto_izquierda = [
#     pygame.image.load("enemigos\enemigo_3\morir\\0.png"),
#     pygame.image.load("enemigos\enemigo_3\morir\\1.png"),
# ]
# lista_enemigo_tres_muerto = girar_imagen(lista_enemigo_tres_muerto_izquierda,True,False)


#---------------------------------------------------------------------------------------------------------

#ANIMACION ITEMS #----------------------------------------------------------------------------------------

lista_animacion_moneda = [
    pygame.image.load("recursos\moneda\\0.png"),
    pygame.image.load("recursos\moneda\\1.png"),
    pygame.image.load("recursos\moneda\\2.png"),
    pygame.image.load("recursos\moneda\\3.png"),
    pygame.image.load("recursos\moneda\\4.png"),
]

sonido_moneda = pygame.mixer.Sound("recursos\sonidos\coin.wav")

lista_portal = [
    pygame.image.load("recursos\portal\\0.png"),
    pygame.image.load("recursos\portal\\1.png"),
    pygame.image.load("recursos\portal\\2.png"),
    pygame.image.load("recursos\portal\\3.png"),
]

#----------------------------------------------------------------------------------------------------------

#LISTA TECLAS PARA NOMBRE DEL SCORE------------------------------------------------------------------------

teclas_letras = {
    pygame.K_a: "A",
    pygame.K_b: "B",
    pygame.K_c: "C",
    pygame.K_d: "D",
    pygame.K_e: "E",
    pygame.K_f: "F",
    pygame.K_g: "G",
    pygame.K_h: "H",
    pygame.K_i: "I",
    pygame.K_j: "J",
    pygame.K_k: "K",
    pygame.K_l: "L",
    pygame.K_m: "M",
    pygame.K_n: "N",
    pygame.K_o: "O",
    pygame.K_p: "P",
    pygame.K_q: "Q",
    pygame.K_r: "R",
    pygame.K_s: "S",
    pygame.K_t: "T",
    pygame.K_u: "U",
    pygame.K_v: "V",
    pygame.K_w: "W",
    pygame.K_x: "X",
    pygame.K_y: "Y",
    pygame.K_z: "Z",
    pygame.K_1: "1",
    pygame.K_2: "2",
    pygame.K_3: "3",
    pygame.K_4: "4",
    pygame.K_5: "5",
    pygame.K_6: "6",
    pygame.K_7: "7",
    pygame.K_8: "8",
    pygame.K_9: "9",
    pygame.K_0: "0"
}
