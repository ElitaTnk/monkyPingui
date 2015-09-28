# -*- coding: utf-8 -*-

import pilasengine


pilas = pilasengine.iniciar()

texto_ayuda = """Aca hay que poner las indicaciones de como jugar :D """

class PantallaAyuda(pilasengine.escenas.Escena):
    #en esta pantalla se dan las instrucciones de juego
    #creación de la clase para la nueva pantalla a partir de la clase madre pilas.escena.Escena
    
    def iniciar(self):
        #instanciamos el fondo deseado y creamos métodos para mostrar los textos de ayuda y el boton de volver
        pilas.fondos.Tarde()
        self.crear_texto_ayuda()
        self.boton = pilas.interfaz.Boton("Volver al Inicio")
        self.boton.y = -100
        self.boton.conectar(self.regresa_inicio)


    def crear_texto_ayuda(self):
        pilas.actores.Texto("Como se juega?:" , y = 100)
        pilas.actores.Texto(texto_ayuda)
            
    def regresa_inicio(self):
        #importa la escena de inicio y ejecuta el cambio de pantalla
        self.pilas.escenas.EscenaMenu()

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
        imagen = pilas.imagenes.cargar("data/logo.png")
        logo = pilas.actores.Actor()
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
        pilas.escenas.PantallaAyuda()

    def comenzar_juego(self):
        #lleva a la escena del juego en si mismo
        #self.pilas.escenas.escena_juego.Juego()
        pass
    

    def salir_juego(self):
        #sale del juego
        pilas.terminar()   

pilas.escenas.vincular(PantallaAyuda)
pilas.escenas.vincular(EscenaMenu)
pilas.escenas.EscenaMenu()
pilas.ejecutar()