# -*- coding: UTF-8 -*-

import pilasengine

class Logo(pilasengine.actores.Actor):
    #creacion de clase Logo, para ser utilizada en varias escenas
    def iniciar(self):
        #importamos logo desde carpeta
        self.imagen = "data/imagenes/logo.png"
        self.y = 150

class EscenaMenu(pilasengine.escenas.Escena):
    #Escena principal donde se encuentra el menu para iniciar o ver ayuda o bien salir del juego
    #creación de la clase para la nueva pantalla a partir de la clase madre pilas.escena.Escena

    def iniciar(self):
        #Contenido de la escena principal: logo, menu...
        self.pilas.fondos.Galaxia()
        self.menu_inicial()
        self.logo = Logo(self.pilas)
        self.animacion_entrada_texto(self.logo)
        self.musica_fondo = self.pilas.musica.cargar('data/musica/POL-hello-sunshine-short.wav')
        self.musica_fondo.detener()
        self.musica_fondo.reproducir(repetir = True)

    def animacion_entrada_texto(self, texto):
        texto.escala = 2
        texto.escala = [1], 1.5

    def menu_inicial(self):
        #creamos opciones y instanciamos el menu principal
        opciones = [
            ("Comenzar a jugar", self.comenzar_juego),
            ("Ver ayuda", self.ir_pantalla_ayuda),
            ("Salir", self.salir_juego)
        ]
        self.menu = self.pilas.actores.Menu(opciones, y = 0)

    def ir_pantalla_ayuda(self):
        #lleva a la escena de ayuda
        self.musica_fondo.detener()
        self.pilas.escenas.PantallaAyuda()

    def comenzar_juego(self):
        #lleva a la escena del juego en si mismo
        self.musica_fondo.detener()
        self.pilas.escenas.Nivel(20, 3, 0)

    def salir_juego(self):
        #sale del juego
        self.musica_fondo.detener()
        self.pilas.terminar()

