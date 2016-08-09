# -*- coding: utf-8 -*-
"""
    Módulo: Juego
    Diseño: Eliana
    Código: M.Alejandra y Eliana
    ---
    Este módulo contiene la importacion del framework, la libreria de colores y el módulo random de python.
    La clase Barra_tiempo nos permite tener el actor Temporizador con todos sus atributos modificados, si bien no se usa en otros módulos su modificación queda mas clara de esta manera y luego solamente es instanciada por Nivel.
    La clase Nivel necesita 3 parámetros obligatoriamente, el tiempo que se quiere dure esa escena, las vidas que va a tener el usuario y la cantidad de puntos al iniciar.
    En ella se generan los personajes, se llama a las tareas de actualizar a los personajes, cheuqear vidas, etc.
    La clase Nivel_2 hereda de Nivel, por lo que también requiere de esos 3 parámetros.
    Mayormente mantiene las funciones de la clase madre excepto por 'termina_el_tiempo', que debe chequear de manera distinta el puntaje y mostrar otro tipo de información.
    Esta escena se conecta con resultados, por lo que en el método de 'ver_resultados' se hace la llamada a 'Resultados' pasando los parámetros correspondientes.

"""
import pilasengine
import pilasengine.colores
import random
from menu import BotonMejorado

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


class Girar_como_reloj(pilasengine.habilidades.Habilidad):
    """Habilidad personalizada semejante a las agujas de un reloj """
    def actualizar(self):
        self.receptor.rotacion -= 360 / 60

class Set_figuras():
    """Clase que permite generar dos figuras iguales y una variable distinta.
        Al inicio de la misma, si ninguna posicion es pasada usa los valores por default"
    """

    def __init__(self, pilas, posiciones = [0, -170, 170]):
        self.posiciones = posiciones
        self.pilas = pilas

        self.figuras_distintas = [pilas.actores.Zanahoria, pilas.actores.Tortuga, pilas.actores.Aceituna]

        random.shuffle(self.posiciones)
        random.shuffle(self.figuras_distintas)

        self.figura_mono1 = self.pilas.actores.Mono(self.posiciones[0],y = 65)
        self.figura_mono2 = self.pilas.actores.Mono(self.posiciones[1],y = 65)
        self.figura_random = self.figuras_distintas[1](self.posiciones[2],y = 65)

        self.figura_mono1.escala = 0.9
        self.figura_mono2.escala = 0.9
        self.figura_random.escala = 1.4

        self.figura_random.radio_de_colision = 45
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
        self.aguja_reloj = self.pilas.actores.Actor()
        self.aguja_reloj.imagen = "data/imagenes/aguja-reloj.png"
        self.aguja_reloj.centro = ("centro", "abajo")
        self.aguja_reloj.aprender(self.pilas.habilidades.Girar_como_reloj)
        self.aguja_reloj.y = 185
        self.aguja_reloj.x = 260

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
            self.pilas.avisar ("NO TE MOVISTE... PERDISTE!!!!")
            self.boton = BotonMejorado(self.pilas, "Volver al inicio", -100)
            self.musica_fondo.detener()
            self.sonido_de_perder.reproducir()
        else:
            self.textoFin = self.pilas.actores.Texto("FIN DEL PRIMER NIVEL", fuente = "data/fuentes/Bangers.ttf", magnitud = 60)
            self.siguiente = BotonMejorado(self.pilas, "pasar al siguiente nivel", -200, 0, False ,self.pasar_siguiente )

    def acierta_callback(self):
        """Efecto de la colision correcta"""
        self.aumentar_puntaje()
        self.eliminar_set_figuras()
        self.sonido_de_acierto.reproducir()

    def acierta(self):
        """Si la colision es correcta los monos sonrien y la tarea acierta_callback es ejecutada 0.1s ~sino no se ve los monos sonreir~"""
        if self.figuras != None:
            self.figuras.figura_mono1.sonreir()
            self.figuras.figura_mono2.sonreir()
            self.pilas.tareas.una_vez(0.1, self.acierta_callback)

    def erronea_callback(self):
        """Efecto de la colision erronea"""
        self.vidas[0].eliminar()
        self.sonido_de_error.reproducir()
        self.cantidad_vidas-= 1
        self.eliminar_set_figuras()

    def erronea(self):
        """Si la colision es erronea los monos sonrien y la tarea erronea_callback es ejecutada 0.1s ~sino no se ve los monos gritar~"""
        if self.figuras != None:
            self.figuras.figura_mono1.gritar()
            self.figuras.figura_mono2.gritar()
            self.pilas.tareas.una_vez(0.1, self.erronea_callback)


    def refrescar_figuras(self):
        """Si hubo una colision y el tiempo no es ni 0 ni 1 ~ porque cuando se acaba se pone en 1 ~ vuelve a generar las figuras"""
        if self.figuras == None:
            self.figuras = Set_figuras(self.pilas)

        if self.tiempo.tiempo != 0 and self.tiempo.tiempo != 1 and self.chequear_vidas() == True:
            return True

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
            self.textoFin = self.pilas.actores.Texto("Perdiste!!!", fuente = "data/fuentes/Bangers.ttf", magnitud = 60)
            self.textoFin.color = pilasengine.colores.rojo
            self.animacion_textoEscalar(self.textoFin)
            self.boton = BotonMejorado(self.pilas, "Volver al inicio", -100)
            self.eliminar_set_figuras()
            self.tiempo.detener()
            self.pingui.eliminar()
            self.sonido_de_perder.reproducir()
            return False

        else:
            return True

    def pasar_siguiente(self):
        self.pilas.escenas.Nivel_2(3,self.cantidad_vidas, self.cantidad_puntos)


class Nivel_2(Nivel):
    """ Esta clase hereda de Nivel por lo que solo sobreescribimos las cosas que cambian como el fondo y algunas acciones"""
    def iniciar(self, tiempo, vidas, puntos):
        Nivel.iniciar(self, tiempo, vidas, puntos)
        self.fondo = self.pilas.fondos.Volley()
        self.sonido_de_ganar = self.pilas.sonidos.cargar("data/musica/aplausos.wav")
        self.puntaje_inicial = puntos

    def termina_el_tiempo(self):
        """si no te mueves te da la opcion de regresar al inicio. si hay puntaje pasas al siguiente nivel"""
        if self.puntaje_inicial == self.cantidad_puntos:
            self.pilas.avisar ("NO TE MOVISTE... PERDISTE!!!!, ")
            self.boton = BotonMejorado(self.pilas, "Volver al inicio", -100)
            self.musica_fondo.detener()
            self.sonido_de_perder.reproducir()
            self.pingui.eliminar()
        else:
            self.textoFin = self.pilas.actores.Texto("FIN DEL JUEGO", fuente = "data/fuentes/Bangers.ttf", magnitud = 60)
            self.pingui.eliminar()
            self.siguiente = BotonMejorado(self.pilas, "Ver resultados", -200, 0, False ,self.ver_resultados )
            self.musica_fondo.detener()
            self.sonido_de_ganar.reproducir()

    def ver_resultados(self):
        self.puntaje_final = self.puntaje.obtener()
        self.pilas.escenas.Resultados(self.cantidad_vidas, self.puntaje_final)
