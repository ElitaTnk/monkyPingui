# -*- coding: utf-8 -*-

import pilasengine

class EscenaMenu(pilasengine.escenas.Escena):
    #Escena principal donde se encuentra el menu para iniciar o ver ayuda o bien salir del juego
    #creación de la clase para la nueva pantalla a partir de la clase madre pilas.escena.Escena
    
    def iniciar(self):
        #Contenido de la escena principal: logo, menu...
        self.set_logo()
        self.menu_inicial()

    def set_logo(self):
        #importamos logo desde carpeta
        imagen = self.pilas.imagenes.cargar("data/logo.png")
        logo = self.pilas.actores.Actor()
        logo.imagen = imagen
        logo.y = 200

    def menu_inicial(self):
        #creamos opciones y instanciamos el menu principal
        opciones = [
            ("Comenzar a jugar", self.comenzar_juego),
            ("Ver ayuda", self.ir_pantalla_ayuda),
            ("Salir", self.salir_juego)
        ]
        self.menu = self.pilas.actores.Menu(opciones, y = 0)

    def ir_pantalla_ayuda(self):
        self.pilas.escenas.PantallaAyuda()

    def comenzar_juego(self):
        #lleva a la escena del juego en si mismo
        #self.pilas.escenas.escena_juego.Juego()
        pass
    

    def salir_juego(self):
        #sale del juego
        self.pilas.terminar()    

