# -*- coding: utf-8 -*-

import pilasengine
import pilasengine.colores
import random
from threading import Timer



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
    """Clase que permite generar dos figuras iguales y una variable distinta"""

    def __init__(self, pilas, posiciones = [0, -170, 170]):
        """inicio de la clase, si ninguna posicion es pasada usa los valores por default"""
        self.posiciones = posiciones
        self.pilas = pilas

        self.figuras_distintas = [pilas.actores.Zanahoria, pilas.actores.Tortuga, pilas.actores.Aceituna]

        random.shuffle(self.posiciones)
        random.shuffle(self.figuras_distintas)

        self.figura_mono1 = self.pilas.actores.Mono(self.posiciones[0],y = 80) 
        self.figura_mono2 = self.pilas.actores.Mono(self.posiciones[1],y = 80) 
        self.figura_random = self.figuras_distintas[1](self.posiciones[2],y = 80) 

        self.figura_mono1.escala = 0.9
        self.figura_mono2.escala = 0.9
        self.figura_random.escala = 1.4

        self.figura_random.radio_de_colision = 50
        self.permite_colision()

    def eliminar(self):
        """Elimina todas las figuras"""
        self.figura_mono1.eliminar()
        self.figura_mono2.eliminar()
        self.figura_random.eliminar()

    def permite_colision(self):
        """Crea etiquetas para determinar opcion correcta o incorrecta"""
        self.figura_mono1.etiquetas.agregar("opcion_erronea")
        self.figura_mono2.etiquetas.agregar("opcion_erronea")
        self.figura_random.etiquetas.agregar("opcion_correcta")


class Nivel(pilasengine.escenas.Escena):
    """escena del primer nivel.
        Se instancia la barra de tiempo y da inicio.
        Se generan los personajes con sus caracteristicas modificadas para el juego.
        Se vinculan las colisiones y las tareas""" 

    def iniciar(self):
        self.pilas.fondos.Selva()

        self.tiempo = Barra_tiempo(self.pilas)
        self.tiempo.ajustar(30, self.termina_el_tiempo)
        self.tiempo.comenzar()

        #puntaje
        self.puntaje = self.pilas.actores.Puntaje(x = 190, y = 160)
        
        #vidas
        self.vidas = [self.pilas.actores.Estrella(x = -200, y = 200), self.pilas.actores.Estrella(x = -240, y = 200), self.pilas.actores.Estrella(x = -280, y = 200)]
    
        for element in self.vidas:
            element.escala = 0.5

        #Aparecen los personajes del primer nivel
        self.figuras = Set_figuras(self.pilas)
        self.pingui = self.pilas.actores.Pingu(x = 0, y = -170)
        self.pingui.radio_de_colision = 50
        self.pingui.centro = ("centro", "centro")
        self.pingui.etiquetas.agregar("pingui")
        self.pingui.aprender(self.pilas.habilidades.LimitadoABordesDePantalla)

        self.pilas.colisiones.agregar("pingui", "opcion_correcta", self.acierta)
        self.pilas.colisiones.agregar("pingui", "opcion_erronea", self.erronea)

        self.pilas.tareas.condicional(3, self.refrescar_figuras)
        self.pilas.tareas.condicional(1, self.chequear_vidas)

  
    def eliminar_set_figuras(self):
        """elimina el set entero de figuras"""
        if self.figuras != None:
            self.figuras.eliminar()
            self.figuras = None

       
    def termina_el_tiempo(self):
        """Se ejecuta cuando el tiempo llega a 0"""
        self.pilas.avisar("Se acabo el tiempo, Fin del primer nivel")
        self.eliminar_set_figuras()
        self.pingui.eliminar()


    def acierta(self):
        """Efecto de la colision correcta"""
        if self.figuras != None:
            self.puntaje.aumentar(10)
            self.eliminar_set_figuras()

    def erronea(self):
        """Efecto de la colision incorrecta"""
        if self.figuras != None:
            self.eliminar_set_figuras()
            self.vidas[0]._destruir()
            self.vidas.pop(0)


    def refrescar_figuras(self):
        """Si hubo una colision y hay tiempo vuelve a generar las figuras"""
        if self.figuras == None:
            self.figuras = Set_figuras(self.pilas)

        if self.tiempo.tiempo != 0 and self.chequear_vidas() == True:
            return True

    def regresa_inicio(self):
        #vuelve la escena de inicio y ejecuta el cambio de pantalla
        self.pilas.escenas.EscenaMenu()

    def animacion_textoPerder(self, texto):
        self.textoFin.escala = 2
        self.textoFin.escala = [1], 1.5

    def chequear_vidas(self):
        if len(self.vidas) == 0:
            self.textoFin = self.pilas.actores.Texto("Perdiste!!!")
            
            self.animacion_textoPerder(self.textoFin)
            self.boton = self.pilas.interfaz.Boton("Volver al Inicio")
            self.boton.y = -100
            self.boton.conectar(self.regresa_inicio)
            self.eliminar_set_figuras()
            self.tiempo.detener()
            self.pingui.eliminar()
            self.puntaje.eliminar()
            return False

        else:
            return True
