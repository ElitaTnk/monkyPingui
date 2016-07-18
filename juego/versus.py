# -*- coding: utf-8 -*-
"""
    Módulo: Versus
    Diseño: Eliana
    Código: Eliana
    ---
    Módulo para el modo player versus player. Cada player tiene un round de tiempo. Al finalizar ambos rounds se comparan los resultados y se proclama al ganador.

"""
import pilasengine
import pilasengine.colores
import random
from juego import Nivel


class Round(Nivel):
    """Hereda de nivel, solo necesitamos cambiar algunas cosas y agregar otras? """
    def iniciar(self, tiempo, vidas, puntos, player):
        Nivel.iniciar(self, tiempo, vidas, puntos)
        self.player = player
        if self.player == 1:
            self.avisoPlayer = self.pilas.actores.Texto("Player 1")
            self.texto.color = pilasengine.colores.rojo
            self.texto.y = 200
            self.texto.x = -50

    def termina_el_tiempo(self):
        self.pingui.eliminar()
        self.puntaje_final = self.puntaje.obtener()
        puntaje_texto = "Puntaje:" + str(self.puntaje.obtener())
        self.textoFin = self.pilas.actores.Texto(puntaje_texto , fuente = "data/fuentes/Bangers.ttf", magnitud = 60)
        self.musica_fondo.detener()

        if self.player == 1:
            self.siguiente = self.pilas.interfaz.Boton("Juega el player 2")
            self.siguiente.y = -200
            self.siguiente.conectar(self.pasar_siguiente)
        else:
            self.siguiente = self.pilas.interfaz.Boton("Ver resultados")
            self.siguiente.y = -200
            self.siguiente.conectar(self.ver_resultados)

    def pasar_siguiente(self):
        self.pilas.escenas.Round(6, 3, 0, 2)

    def ver_resultados(self):
        self.puntaje_final = self.puntaje.obtener()
        self.pilas.escenas.Resultados(self.cantidad_vidas, self.puntaje_final)
