# coding: utf-8

import pilasengine
pilas = pilasengine.iniciar()

class EscenaMenu(pilasengine.escenas.Escena):
    #Escena principal donde se encuentra el menu para iniciar o ver ayuda o bien salir del juego
    #creación de la clase para la nueva pantalla a partir de la clase madre pilas.escena.Escena
    
    def iniciar(self):
        #Contenido de la escena principal: logo, menu...
        self.set_logo()
        self.menu_inicial()

    def set_logo(self):
        #importamos logo desde carpeta
        imagen = pilas.imagenes.cargar("data/logo.png")
        logo = pilas.actores.Actor()
        logo.imagen = imagen
        logo.y = 200

    def menu_inicial(self):
        #creamos opciones y instanciamos el menu principal
        opciones = [
            ("Comenzar a jugar", self.comenzar_juego),
            ("Ver ayuda", self.ayuda),
            ("Salir", self.salir_juego)
        ]
        self.menu = pilas.actores.Menu(opciones, y = 0)

    def comenzar_juego(self):
        #lleva a la escena del juego en si mismo
        import escena_juego
        pilas.cambiar_escena(escena_juego.Juego())

    def ayuda(self):
        #lleva a la pantalla de ayuda
        import ayuda
        pilas.cambiar_escena(ayuda.PantallaAyuda())

    def salir_juego(self):
        #sale del juego
        pilas.terminar()    
     
        
        
                
pilas.escenas.vincular(EscenaMenu)
pilas.escenas.EscenaMenu() 
          
pilas.ejecutar()

