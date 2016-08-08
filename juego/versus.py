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

player_setResultados = []

class Round(Nivel):
    """Hereda de nivel, solo necesitamos cambiar algunas cosas y agregar otras? """
    def iniciar(self, tiempo, vidas, puntos, player):
        Nivel.iniciar(self, tiempo, vidas, puntos)
        self.player = player

        self.avisoPlayer = self.pilas.actores.Texto(self.player)
        self.avisoPlayer.color = pilasengine.colores.rojo
        self.avisoPlayer.x = 100
        self.avisoPlayer.y = 200

    def termina_el_tiempo(self):
        self.pingui.eliminar()
        self.puntaje_final = self.puntaje.obtener()
        puntaje_texto = "Puntaje:" + str(self.puntaje_final)

        self.player_set = (self.player, self.cantidad_vidas, self.puntaje_final)

        global player_setResultados
        player_setResultados.append(self.player_set)

        self.textoFin = self.pilas.actores.Texto(puntaje_texto , fuente = "data/fuentes/Bangers.ttf", magnitud = 60)
        self.musica_fondo.detener()

        if self.player == "Player 1":
            self.siguiente = self.pilas.interfaz.Boton("Juega el player 2")
            self.siguiente.y = -200
            self.siguiente.conectar(self.pasar_siguiente)
        else:
            self.siguiente = self.pilas.interfaz.Boton("Ver resultados")
            self.siguiente.y = -200
            self.versusResultados = list(player_setResultados)

            self.siguiente.conectar(self.ver_resultados_versus)

    def pasar_siguiente(self):
        self.pilas.escenas.Round(6, 3, 0, "Player 2")

    def ver_resultados_versus(self):
        del player_setResultados[:]
        self.pilas.escenas.EndRound(self.versusResultados)
