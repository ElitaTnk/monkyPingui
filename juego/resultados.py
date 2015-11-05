# -*- coding: utf-8 -*-

import pilasengine
import pilasengine.colores
from operator import itemgetter

lista_ranking = []

class Resultados(pilasengine.escenas.Escena):
    def iniciar(self, numero):
        self.cantidad = str(numero)
        
        self.sonido_de_festejo = self.pilas.sonidos.cargar("data/musica/festejo.wav")
        self.sonido_de_festejo.reproducir()

        self.fondo = self.pilas.fondos.Galaxia(dy=-5)
        self.fondo.imagen = self.pilas.imagenes.cargar("data/imagenes/fondo.png")
        self.fondo.imagen.repetir_vertical = True
        self.fondo.imagen.repetir_horizontal = True

        self.texto_puntaje = self.pilas.actores.Actor()
        self.texto_puntaje.imagen = "data/imagenes/resultado.png"
        self.texto_puntaje.y = 50
        self.texto_puntaje.escala = 1
        
        self.texto_cantidad = self.pilas.actores.Texto(self.cantidad, fuente = "data/Bangers.ttf", magnitud = 60)
        self.texto_cantidad.y = -50
        self.texto_cantidad.x = 0
        self.texto_cantidad.color = pilasengine.colores.blanco

        self.nombre_jugador = self.pilas.interfaz.IngresoDeTexto("Ale&Eli", limite_de_caracteres=8) 

        self.boton = self.pilas.interfaz.Boton("Ver ranking")
        self.boton.conectar(self.ver_ranking)
        self.boton.y = -100

    def ver_ranking(self):
        self.pilas.escenas.Ranking(self.cantidad, self.nombre_jugador)


class Ranking(pilasengine.escenas.Escena):
    def iniciar(self, numero, nombre):
        self.fondo = self.pilas.fondos.Galaxia(dy=-5)
        self.fondo.imagen = self.pilas.imagenes.cargar("data/imagenes/fondo.png")
        self.fondo.imagen.repetir_vertical = True
        self.fondo.imagen.repetir_horizontal = True

        self.musica_fondo = self.pilas.sonidos.cargar("data/musica/turn_down_for_what_ringtone.wav")
        self.musica_fondo.reproducir()

        self.boton = self.pilas.interfaz.Boton("Volver al Inicio")
        self.boton.conectar(self.regresa_inicio)
        self.boton.y = -100

        self.pingui = self.pilas.actores.Actor()
        self.pingui.imagen = "data/imagenes/tdfw.png"
        self.pingui.y = -200
        self.pingui.x = 200

        self.score = (str(nombre.texto), numero)

        global lista_ranking
        lista_ranking.append(self.score)
        lista_ranking =  sorted(lista_ranking,key=itemgetter(0))
        lista_ranking =  sorted(lista_ranking,key=itemgetter(1), reverse=True)
        idx = 0
        ajuste_altura = 200

        for item in lista_ranking:
            idx+=1
            ajuste_altura-=50
            nombre_jugador = item[0]
            puntaje_jugador = item[1]
            linea =  str(idx) + " - " + nombre_jugador + " ................... " + puntaje_jugador + "\n"
            
            ranking_linea = self.pilas.actores.Texto(linea, x = -200, y = ajuste_altura)
            ranking_linea.centro = ("izquierda", "centro")

    def regresa_inicio(self):
        self.musica_fondo.detener()
        self.pilas.escenas.EscenaMenu()