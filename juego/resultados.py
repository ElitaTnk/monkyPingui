# -*- coding: utf-8 -*-
"""
    Módulo: Resultados
    Diseño: Eliana
    Código: M.Alejandra y Eliana
    ---
    Este módulo contiene la clase Resultados, cuya escena muestra el resultado final obtenido, para lo cual necesita los parámetros 'puntos' y 'vidas'.
    También la clase Ranking, que es la escena final, que toma los mismos parámetros anteriormente mencionados, junto con 'nombre' y los usa para generar una lista de resultados.
"""
import pilasengine
import pilasengine.colores
from operator import itemgetter
from menu import BotonMejorado

lista_ranking = []

class Resultados(pilasengine.escenas.Escena):
    """Escena para mostrar el resultado final y dar la opcion de poner un nombre para el ranking.
        El nombre debe tener maximo 7 caracteres, de lo contratrio se trunca y muestra los primeros 7.
        Si nombre es una cadena vacia se reemplaza por la opcion default: Ale&Eli.
    """
    def iniciar(self, vidas, puntos):
        self.vidas = str(vidas)
        self.puntos = str(puntos)

        self.sonido_de_festejo = self.pilas.sonidos.cargar("data/musica/festejo.wav")
        self.sonido_de_festejo.reproducir()

        self.fondo = self.pilas.fondos.Galaxia(dy=-5)
        self.fondo.imagen = self.pilas.imagenes.cargar("data/imagenes/fondo.png")
        self.fondo.imagen.repetir_vertical = True
        self.fondo.imagen.repetir_horizontal = True

        self.texto_puntaje = self.pilas.actores.Actor()
        self.texto_puntaje.imagen = "data/imagenes/resultado.png"
        self.texto_puntaje.y = 90
        self.texto_puntaje.escala = 1

        self.texto_puntos = self.pilas.actores.Texto(self.puntos, fuente = "data/fuentes/Bangers.ttf", magnitud = 60, y = 20)
        self.texto_puntos.color = pilasengine.colores.blanco

        self.nombre_jugador = self.pilas.interfaz.IngresoDeTexto("Ale&Eli", limite_de_caracteres=8, y = -50)
        self.nombre_jugador.decir("Escribi tu nombre, maximo 7 letras")

        self.boton = BotonMejorado(self.pilas, "Ver ranking", -100, 0, False ,self.ver_ranking )

    def ver_ranking(self):
        self.pilas.escenas.Ranking(self.vidas, self.puntos, self.nombre_jugador)

class PantallaFinal(pilasengine.escenas.Escena):
    """ Escena base para ser usada con modificaciones para ranking en modo simple o endRound en modo versus  """
    def iniciar(self):
        self.fondo = self.pilas.fondos.Galaxia(dy=-5)
        self.fondo.imagen = self.pilas.imagenes.cargar("data/imagenes/fondo.png")
        self.fondo.imagen.repetir_vertical = True
        self.fondo.imagen.repetir_horizontal = True

        self.musica_fondo = self.pilas.sonidos.cargar("data/musica/turn_down_for_what_ringtone.wav")
        self.musica_fondo.reproducir()

        self.boton = BotonMejorado(self.pilas, "Volver al inicio", -200)

        self.pingui = self.pilas.actores.Actor()
        self.pingui.imagen = "data/imagenes/tdfw.png"
        self.pingui.y = -120
        self.pingui.x = 200

        self.anteojos = self.pilas.actores.Actor()
        self.anteojos.imagen = "data/imagenes/tdfw-glasses.png"
        self.anteojos.y = 300
        self.anteojos.x = 200
        self.anteojos.y = [-120], 6

        self.titulo = self.pilas.actores.Texto("Ranking", fuente = "data/fuentes/Bangers.ttf", magnitud = 60, y = 185, x = -180)
        self.titulo_puntos = self.pilas.actores.Texto("Puntos", fuente = "data/fuentes/Bangers.ttf", magnitud = 20, y = 175, x = 0)
        self.titulo_vidas = self.pilas.actores.Texto("Vidas", fuente = "data/fuentes/Bangers.ttf", magnitud = 20, y = 175, x = 70)

    def ordenarResultados(self, listaDeResultados):
        #ordena los resultados en forma de lista de manera:
        listaDeResultados =  sorted(listaDeResultados,key=itemgetter(0)) #alfabeticamente
        listaDeResultados =  sorted(listaDeResultados,key=itemgetter(2), reverse=True) #por puntaje
        listaDeResultados =  sorted(listaDeResultados,key=itemgetter(1), reverse=True) #por vidas

        listaDeResultados = listaDeResultados[:10]

        return listaDeResultados


    def listarResultados(self, listaDeResultados):
        #crea una lista visual ordenada de los elementos dentro de la lista de resultados
        idx = 0
        ajuste_altura = 178

        #itero sobre la lista para armar las lineas del ranking
        for item in listaDeResultados:
            idx+=1 #subo la enumeracion
            ajuste_altura-=30 #por cada iteracion resta 30 para que no se pisen las lineas
            nombre_jugador = item[0]
            vidas_jugador = item[1]
            puntaje_jugador = item[2]
            if idx == 10:
                linea =  str(idx) + " - " + str(nombre_jugador) + ".............." + str(puntaje_jugador) + "....." + str(vidas_jugador)
            else:
                linea =  " " + str(idx) + " - " + str(nombre_jugador) + ".............." + str(puntaje_jugador) + "....." + str(vidas_jugador)

            self.ranking_linea = self.pilas.actores.Texto(linea, fuente = "data/fuentes/VT323-Regular.ttf", x = -300, y = ajuste_altura)
            self.ranking_linea.centro = ("izquierda", "centro") #cambio el centro del objeto para que quede centrado a la izquierda.


class Ranking(PantallaFinal):
    """Escena final de Ranking, donde se listan las 10 mejores jugadas de la ejecución actual, ordenadas.
    """
    def iniciar(self, vidas, puntos, nombre):
        PantallaFinal.iniciar(self)

        #preparo el texto recibido en el input, para poder manejarlo como str y usarlo luego en el actor
        self.nombre = str(nombre.texto)

        if len(self.nombre) == 0:
            self.nombre = "Ale&Eli"
        elif len(self.nombre) < 7:
            self.nombre = self.nombre.ljust(7) #alinea a la izquierda si el width es menor a 7

        self.nombre = self.nombre[:7] #trunco por si se pasa de 7

        #creo tupla
        self.score = (self.nombre, vidas, puntos)
        global lista_ranking
        lista_ranking.append(self.score)


        self.listarResultados(self.ordenarResultados(lista_ranking))

class EndRound(PantallaFinal):
    """Pantalla de resultados para el versus """
    def iniciar(self, versusResultados):
        PantallaFinal.iniciar(self)

        self.versusResultados = versusResultados

        #comparo los resultados de ambos jugadores, si no son iguales lista los resultados y crea otras imagenes.
        if self.compararResultados(self.ordenarResultados(self.versusResultados)) == False:
            self.listarResultados(self.ordenarResultados(self.versusResultados))
            self.otroPingui = self.pilas.actores.Actor()
            self.otroPingui.imagen = "data/imagenes/perdedor.png"
            self.otroPingui.y = -120
            self.otroPingui.x = -200

            self.ganador = self.ordenarResultados(self.versusResultados)
            self.textoGanador = self.pilas.actores.Texto("Ganador " + self.ganador[0][0], fuente = "data/fuentes/Bangers.ttf", magnitud = 60, y = 20)

    def compararResultados(self, resultados):
        #toma el puntaje y lo compara con el siguiente, luego hace lo mismo con las vidas, si ambos son iguales se empata. Sino sale del loop 
        maximo = 0
        vidas = 0
        for score in resultados:
            if score[2] > maximo and score[1] > vidas:
                maximo = score[2]
                vidas = score[1]
            elif score[2] == maximo:
                if score[1] == vidas:
                    self.listarResultados(resultados)
                    self.empatados = self.pilas.actores.Texto("Empatados", fuente = "data/fuentes/Bangers.ttf", magnitud = 60, y = 20)
                    self.otroPingui = self.pilas.actores.Actor()
                    self.otroPingui.imagen = "data/imagenes/tdfw2.png"
                    self.otroPingui.y = -120
                    self.otroPingui.x = -200

                    self.cadenas = self.pilas.actores.Actor()
                    self.cadenas.imagen = "data/imagenes/thuglife.png"
                    self.cadenas.y = 300
                    self.cadenas.x = -220
                    self.cadenas.y = [-30], 6
                else:
                    return False
            else:
                return False
