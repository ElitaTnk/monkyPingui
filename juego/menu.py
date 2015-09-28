# -*- coding: utf-8 -*-

import pilasengine
import ayuda
#import escena_juego
#pilas = pilasengine.iniciar()

class EscenaMenu(pilasengine.escenas.Escena):
    #Escena principal donde se encuentra el menu para iniciar o ver ayuda o bien salir del juego
    #creación de la clase para la nueva pantalla a partir de la clase madre pilas.escena.Escena
    
    def iniciar(self):
        #Contenido de la escena principal: logo, menu...
        self.set_logo()
        self.menu_inicial()
        #self.pilas.eventos.click_de_mouse.conectar(self._iniciar_el_juego)

    def set_logo(self):
        #importamos logo desde carpeta
        imagen = pilasengine.imagenes.cargar("data/logo.png")
        logo = pilasengine.actores.Actor()
        logo.imagen = imagen
        logo.y = 200

    def menu_inicial(self):
        #creamos opciones y instanciamos el menu principal
        opciones = [
            ("Comenzar a jugar", self.comenzar_juego),
            ("Ver ayuda", self.ir_pantalla_ayuda),
            ("Salir", self.salir_juego)
        ]
        self.menu = pilas.actores.Menu(opciones, y = 0)

    def ir_pantalla_ayuda(self):
        pilasengine.escenas.vincular(ayuda.PantallaAyuda)
        pilasengine.escenas.PantallaAyuda()

    def comenzar_juego(self):
        #lleva a la escena del juego en si mismo
        #self.pilasengine.escenas.escena_juego.Juego()
        pass
    

    def salir_juego(self):
        #sale del juego
        pilasengine.terminar()    
     
            
pilasengine.escenas.vincular(EscenaMenu)
pilasengine.escenas.EscenaMenu()
#pilas.escenas.vincular(escena_juego.Juego)
