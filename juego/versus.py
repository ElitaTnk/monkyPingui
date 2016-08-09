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
from menu import BotonMejorado

player_setResultados = []

class Round(Nivel):
    """Hereda de nivel, utiliza solo los metodos que necesita y se cambian algunas funciones. """
    def iniciar(self, tiempo, vidas, puntos, player):
        Nivel.iniciar(self, tiempo, vidas, puntos)
        self.player = player

        #muestro a que jugador pertenece el turno
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

        #Si jugo el player 1 le toca al player 2, sino vamos a la pantalla de resultados
        if self.player == "Player 1":
            self.siguiente = BotonMejorado(self.pilas, "Juega Player 2", -200, 0, False ,self.pasar_siguiente )
        else:
            self.siguiente = BotonMejorado(self.pilas, "Ver resultados", -200, 0, False ,self.ver_resultados_versus )
            #copio el contenido de player_setResultados a otra lista, para poder resetear la original cada vez que termina el 2do round.
            self.versusResultados = list(player_setResultados)

    def pasar_siguiente(self):
        self.pilas.escenas.Round(10, 3, 0, "Player 2")

    def ver_resultados_versus(self):
        #elimino el contenido de la lista para que este en 0 cuando un nuevo versus se juegue.
        del player_setResultados[:]
        self.pilas.escenas.EndRound(self.versusResultados)
