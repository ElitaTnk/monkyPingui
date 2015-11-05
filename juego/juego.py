# -*- coding: utf-8 -*-

import pilasengine
import pilasengine.colores
import random

class Barra_tiempo(pilasengine.actores.Temporizador):
    """ nueva barra de tiempo, con imagen y cambio de argumentos"""
    def iniciar(self):
        self.imagen = "data/imagenes/152-clock.png"
        self.texto = self.pilas.actores.Texto("0")
        self.texto.color = pilasengine.colores.verde
        self.y = 185
        self.x = 260
        self.texto.y = 120
        self.texto.x = 255

class Set_figuras():
    """Clase que permite generar dos figuras iguales y una variable distinta"""

    def __init__(self, pilas, posiciones = [0, -170, 170]):
        """inicio de la clase, si ninguna posicion es pasada usa los valores por default"""
        self.posiciones = posiciones
        self.pilas = pilas

        self.figuras_distintas = [pilas.actores.Zanahoria, pilas.actores.Tortuga, pilas.actores.Aceituna]

        random.shuffle(self.posiciones)
        random.shuffle(self.figuras_distintas)

        self.figura_mono1 = self.pilas.actores.Mono(self.posiciones[0],y = 70)
        self.figura_mono2 = self.pilas.actores.Mono(self.posiciones[1],y = 70)
        self.figura_random = self.figuras_distintas[1](self.posiciones[2],y = 70)

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

    def iniciar(self, tiempo, cantidad_vidas, cantidad_puntos):
        self.cantidad_puntos = cantidad_puntos
        self.cantidad_vidas = cantidad_vidas

        self.fondo = self.pilas.fondos.Fondo()
        self.fondo.imagen = self.pilas.imagenes.cargar("data/imagenes/granja.png")

        self.tiempo = Barra_tiempo(self.pilas)
        self.tiempo.ajustar(tiempo, self.termina_el_tiempo)
        self.tiempo.comenzar()

        self.puntaje = self.pilas.actores.Puntaje(x = 10, y = 200)
        self.puntaje.definir(self.cantidad_puntos)
        self.texto = self.pilas.actores.Texto("Puntaje:")
        self.texto.color = pilasengine.colores.negro
        self.texto.y = 200
        self.texto.x = -50

        self.sonido_de_error = self.pilas.sonidos.cargar("data/musica/pedito.wav")
        self.sonido_de_acierto = self.pilas.sonidos.cargar("data/musica/acierto.wav")
        self.sonido_de_perder = self.pilas.sonidos.cargar("data/musica/perdedor.wav")
        self.musica_fondo = self.pilas.musica.cargar("data/musica/POL-across-the-skies-short.wav")
        self.musica_fondo.reproducir(repetir = True)
        
        #vidas
        self.vidas_posiciones = [-200, -240, -280]
        self.vidas = (self.pilas.actores.Estrella()* self.cantidad_vidas)

        #itero sobre self.vidas que es un grupo, luego por cada elemento de ese grupo asigno las posciones de la lista
        for element, pos in zip(self.vidas, self.vidas_posiciones):
            element.escala = 0.5
            element.y = 200
            element.x = pos

        #Aparecen los personajes
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

    def aumentar_puntaje(self):
        self.puntaje.aumentar(1)
        self.animacion_textoEscalar(self.puntaje)
        self.cantidad_puntos += 1       #es importante tambien aumentar la variable

    def eliminar_set_figuras(self):
        """elimina el set entero de figuras"""
        if self.figuras != None:
            self.figuras.eliminar()
            self.figuras = None

    def termina_el_tiempo(self):
        """Se ejecuta cuando el tiempo llega a 0"""
        self.pingui.eliminar()

        """si no te mueves te da la opcion de regresar al inicio. si hay puntaje pasas al siguiente nivel"""
        if self.puntaje.obtener() == 0:
            self.pilas.avisar ("NO TE MOVISTE... PERDISTE!!!!, ")
            self.boton = self.pilas.interfaz.Boton("Volver al Inicio")
            self.boton.conectar(self.regresa_inicio)
            self.boton.y = -100
            self.musica_fondo.detener()
            self.sonido_de_perder.reproducir()
        else:
            self.textoFin = self.pilas.actores.Texto("FIN DEL PRIMER NIVEL", fuente = "data/Bangers.ttf", magnitud = 60)
            self.siguiente = self.pilas.interfaz.Boton("pasar al siguiente nivel")
            self.siguiente.y = -200
            self.siguiente.conectar(self.pasar_siguiente)

    def acierta(self):
        """Efecto de la colision correcta"""
        if self.figuras != None:
            self.aumentar_puntaje()
            self.eliminar_set_figuras()
            self.sonido_de_acierto.reproducir()

    def erronea(self):
        """Efecto de la colision incorrecta"""
        if self.figuras != None:
            self.eliminar_set_figuras()
            self.vidas[0].eliminar()
            self.sonido_de_error.reproducir()
            self.cantidad_vidas-= 1

    def refrescar_figuras(self):
        """Si hubo una colision y el tiempo no es ni 0 ni 1 ~ porque cuando se acaba se pone en 1 ~ vuelve a generar las figuras"""
        if self.figuras == None:
            self.figuras = Set_figuras(self.pilas)

        if self.tiempo.tiempo != 0 and self.tiempo.tiempo != 1 and self.chequear_vidas() == True:
            return True

    def regresa_inicio(self):
        self.pilas.escenas.EscenaMenu()

    def animacion_textoEscalar(self, texto):
        texto.escala = 2
        texto.escala = [1], 1.5

    def chequear_vidas(self):
        """Tarea que se fija la condicion de las vidas.
        Si las vidas son igual a 0 entonces ejecuta una serie de tareas para indicar que se acabo el juego.
        Si aun hay vidas retorna True para que la tarea siga ejecutandose.
        """

        if self.tiempo.tiempo < 10:
            self.tiempo.texto.color = pilasengine.colores.rojo

        if len(self.vidas) == 0:
            self.textoFin = self.pilas.actores.Texto("Perdiste!!!")
            self.textoFin.color = pilasengine.colores.rojo
            self.animacion_textoEscalar(self.textoFin)
            self.boton = self.pilas.interfaz.Boton("Volver al Inicio")
            self.boton.y = -100
            self.boton.conectar(self.regresa_inicio)
            self.eliminar_set_figuras()
            self.tiempo.detener()
            self.pingui.eliminar()
            self.sonido_de_perder.reproducir()
            return False

        else:
            return True

    def pasar_siguiente(self):
        self.pilas.escenas.Nivel_2(4,self.cantidad_vidas, self.cantidad_puntos)


class Nivel_2(Nivel):
    """ Esta clase hereda de Nivel por lo que solo sobreescribimos las cosas que cambian como el fondo y algunas acciones"""
    def iniciar(self, tiempo, vidas, puntos):
        Nivel.iniciar(self, tiempo, vidas, puntos)
        self.fondo = self.pilas.fondos.Volley()
        self.sonido_de_ganar = self.pilas.sonidos.cargar("data/musica/aplausos.wav")

    def termina_el_tiempo(self):
        self.textoFin = self.pilas.actores.Texto("FIN DEL JUEGO", fuente = "data/Bangers.ttf", magnitud = 60)
        self.pingui.eliminar()
        self.siguiente = self.pilas.interfaz.Boton("Ver resultados")
        self.siguiente.y = -200
        self.siguiente.conectar(self.ver_resultados)
        self.musica_fondo.detener()
        self.sonido_de_ganar.reproducir()

    def ver_resultados(self):
        self.puntaje_final = self.puntaje.obtener()
        self.pilas.escenas.Resultados(self.puntaje_final)


class Resultados(pilasengine.escenas.Escena):
    def iniciar(self, numero):
        self.cantidad = str(numero)
        
        self.sonido_de_festejo = self.pilas.sonidos.cargar("data/musica/festejo.wav")
        self.fondo = self.pilas.fondos.Galaxia(dy=-5)
        self.fondo.imagen = self.pilas.imagenes.cargar("data/imagenes/fondo.png")
        self.fondo.imagen.repetir_vertical = True
        self.fondo.imagen.repetir_horizontal = True
        self.texto_puntaje = self.pilas.actores.Actor()
        self.texto_puntaje.imagen = "data/imagenes/resultado.png"
        self.texto_puntaje.y = 50
        self.texto_puntaje.escala = 1
        self.musica_fondo = self.pilas.sonidos.cargar("data/musica/turn_down_for_what_ringtone.wav")
        self.musica_fondo.reproducir()
        
        self.texto_cantidad = self.pilas.actores.Texto(self.cantidad, fuente = "data/Bangers.ttf", magnitud = 60)
        self.texto_cantidad.y = -50
        self.texto_cantidad.x = 0
        self.texto_cantidad.color = pilasengine.colores.blanco

        self.boton = self.pilas.interfaz.Boton("Volver al Inicio")
        self.boton.conectar(self.regresa_inicio)
        self.boton.y = -100

        self.sonido_de_festejo.reproducir()

        self.pingui = self.pilas.actores.Actor()
        self.pingui.imagen = "data/imagenes/tdfw.png"
        self.pingui.y = -200
        self.pingui.x = 200

    def regresa_inicio(self):
        self.musica_fondo.detener()
        self.pilas.escenas.EscenaMenu()