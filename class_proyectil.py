import pygame

class Proyectil():
    #la imagen se la paso en cada nivel
    def __init__(self, path_imagen, direccion, personaje) -> None:
        tamaño = (20,20)
        self.superficie = pygame.image.load(path_imagen)
        self.superficie = pygame.transform.scale(self.superficie, tamaño)
        self.rectangulo = self.superficie.get_rect()
        self.posicion = personaje.rectangulo.x + personaje.ancho/2, personaje.rectangulo.y + personaje.alto/2
        self.rectangulo.x = self.posicion[0]
        self.rectangulo.y = self.posicion[1]
        self.direccion = direccion
        self.velocidad = 12
        self.recorrido = 0
        self.daño = True
        self.desaparicion = False
        self.ha_desaparecido = False
        self.tiempo_inicial = pygame.time.get_ticks()

    def mover(self):
        '''brief: mueve el proyectil en izquierda y derecha'''
        if self.direccion == "derecha":
            self.rectangulo.x += self.velocidad
            self.recorrido += 1
        else:
            self.rectangulo.x -= self.velocidad
            self.recorrido += 1
        if self.recorrido >= 15:
            self.velocidad = 8
            self.rectangulo.y += 15

    def detectar_piso(self, plataformas):
        '''brief: detecta el suelo de la plataforma(cuando disparo la bala queda en el suelo)'''
        for plataforma in plataformas:
            if self.rectangulo.colliderect(plataforma.lados["top"]):
                self.velocidad = 0
                self.rectangulo.y = plataforma.lados["main"].top - 10
                self.daño = False
                self.desaparicion = True
                break

    def desaparecer_proyectil(self):
        '''brief: desaparezco la bala que queda en el suelo'''
        if self.desaparicion == True:
            tiempo_actual = pygame.time.get_ticks()
            tiempo_transcurrido = tiempo_actual - self.tiempo_inicial
            if tiempo_transcurrido >= 2000:
                self.ha_desaparecido = True

    def dibujar_hitbox(self, pantalla):
        '''brief: dibujo la hitbox'''
        pygame.draw.rect(pantalla,"Red",self.rectangulo,1)

