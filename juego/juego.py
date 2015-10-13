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

    def eliminar(self):
        self.figura_mono1.eliminar()
        self.figura_mono2.eliminar()
        self.figura_random.eliminar()


class Nivel(pilasengine.escenas.Escena):
    #escena del primer nivel. Se instancia la barra de tiempo y da inicio, 
    def iniciar(self):
        self.pilas.fondos.Selva()
        self.tiempo = Barra_tiempo(self.pilas)
        
        #Aparecen los personajes del primer nivel
        self.pingui = self.pilas.actores.Pingu(x = 0, y = -170)
        self.figuras = Set_figuras(self.pilas)
        
        #se asigna un mensaje al final
        self.tiempo.ajustar(30, self.hola_mundo)
        self.tiempo.comenzar()
          
    def hola_mundo(self):
        self.pilas.avisar("Fin del primer nivel")
        self.figuras.eliminar()
        self.pingui.eliminar()
