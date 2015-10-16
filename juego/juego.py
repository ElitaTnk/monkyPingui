# -*- coding: utf-8 -*-

import pilasengine
import pilasengine.colores
import random


class Barra_tiempo(pilasengine.actores.Temporizador):
    #nueva barra de tiempo, con imagen y cambio de argumentos
    def iniciar(self):
        self.imagen = "data/152-clock.png"
        self.texto = self.pilas.actores.Texto("0")
        self.texto.color = pilasengine.colores.negro
        self.y = 160
        self.x = 260
        self.texto.y = 100
        self.texto.x = 250

class Set_figuras():
    #Clase que genera tres figuras con posicion variada
    def __init__(self, pilas, posiciones = [0, -170, 170]):
        self.posiciones = posiciones
        self.pilas = pilas

        self.figuras_distintas = [pilas.actores.Zanahoria, pilas.actores.Tortuga, pilas.actores.Aceituna]

        random.shuffle(self.posiciones)
        random.shuffle(self.figuras_distintas)

        print(self.figuras_distintas[1])
        self.figura_mono1 = self.pilas.actores.Mono(self.posiciones[0],y = 100) 
        self.figura_mono2 = self.pilas.actores.Mono(self.posiciones[1],y = 100) 
        self.figura_random = self.figuras_distintas[1](self.posiciones[2],y = 100) 

        self.figura_mono1.escala = 0.9
        self.figura_mono2.escala = 0.9
        self.figura_random.escala = 1.4

        self.figura_random.radio_de_colision = 100

    def eliminar(self):
        self.figura_mono1.eliminar()
        self.figura_mono2.eliminar()
        self.figura_random.eliminar()


class Nivel(pilasengine.escenas.Escena):
    #escena del primer nivel. Se instancia la barra de tiempo y da inicio, 
    def iniciar(self):
        self.pilas.fondos.Selva()
        self.tiempo = Barra_tiempo(self.pilas)

        #puntaje
        self.puntaje = self.pilas.actores.Puntaje(x = 190, y = 160)
        
        #vidas
        self.vidas = [self.pilas.actores.Estrella(x = -200, y = 200), self.pilas.actores.Estrella(x = -240, y = 200), self.pilas.actores.Estrella(x = -280, y = 200)]
    
        for element in self.vidas:
            element.escala = 0.5

        #Aparecen los personajes del primer nivel
        self.pingui = self.pilas.actores.Pingu(x = 0, y = -170)
        self.pingui.radio_de_colision = 100
        self.figuras = Set_figuras(self.pilas)

        self.figuras.figura_mono1.etiquetas.agregar("opcion_erronea")
        self.figuras.figura_mono2.etiquetas.agregar("opcion_erronea")
        self.figuras.figura_random.etiquetas.agregar("opcion_correcta")
        self.pingui.etiquetas.agregar("pingui")

        #se asigna un mensaje al final

        self.tiempo.ajustar(30, self.hola_mundo)
        self.tiempo.comenzar()

        #pingui no se salga de la pantalla
        self.pingui.aprender(self.pilas.habilidades.LimitadoABordesDePantalla)

        self.pilas.colisiones.agregar("pingui", "opcion_correcta", self.acierta)
        self.pilas.colisiones.agregar("pingui", "opcion_erronea", self.erronea)
          
    def hola_mundo(self):
        self.pilas.avisar("Fin del primer nivel")
        self.figuras.eliminar()
        self.pingui.eliminar()


    def acierta(self):
        self.figuras.figura_random.eliminar()
        self.puntaje.aumentar(10)

    def erronea(self):
        self.figuras.eliminar()
        self.vidas[0]._destruir()


"""
aciertos = []
errores = []
figuras = []

def cuanto_toca_figura_bien(personaje, figura):
    i.eliminar()
    puntos.aumentar(10)
    puntos.escala = 2
    puntos.escala = [1], 0.2
    puntos.rotacion = random.randint(30, 60)
    puntos.rotacion = [0], 0.2

#pilas.colisiones.agregar(vaca, items, cuanto_toca_item)


def crear_set():
    un_set = Set_figuras(pilas)
    figuras.append(un_set)
    return True

pilas.tareas.agregar(3.3, crear_set)


def cuanto_toca_figura_mal(vaca, enemigo):
    vaca.perder()
    enemigo.eliminar()

#pilas.colisiones.agregar(vaca, enemigos, cuanto_toca_enemigo)
"""
