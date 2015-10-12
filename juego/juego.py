# -*- coding: utf-8 -*-

import pilasengine
import pilasengine.colores

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

class Nivel(pilasengine.escenas.Escena):
    #escena del primer nivel. Se instancia la barra de tiempo y da inicio, se asigna un mensaje al final
    def iniciar(self):
        self.pilas.fondos.Selva()
        self.tiempo = Barra_tiempo(self.pilas)
        self.tiempo.ajustar(20, self.hola_mundo)
        self.tiempo.comenzar()

    def hola_mundo(self):
        self.pilas.avisar("Fin del primer nivel")
