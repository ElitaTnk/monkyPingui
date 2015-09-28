# -*- coding: utf-8 -*-

import pilasengine
import menu



texto_ayuda = """Aca hay que poner las indicaciones de como jugar :D """
#pilas = pilasengine.iniciar()

class PantallaAyuda(pilasengine.escenas.Escena):
    #en esta pantalla se dan las instrucciones de juego
    #creación de la clase para la nueva pantalla a partir de la clase madre pilas.escena.Escena
    
    def iniciar(self):
        #instanciamos el fondo deseado y creamos métodos para mostrar los textos de ayuda y el boton de volver
        pilasengine.fondos.Tarde()
        self.crear_texto_ayuda()
        self.boton = pilasengine.interfaz.Boton("Volver al Inicio")
        self.boton.y = -100
        self.boton.conectar(self.regresa_inicio)


    def crear_texto_ayuda(self):
        pilasengine.actores.Texto("Como se juega?:" , y = 100)
        pilasengine.actores.Texto(texto_ayuda)
            
    def regresa_inicio(self):
        #importa la escena de inicio y ejecuta el cambio de pantalla
        pilasengine.escenas.vincular(menu.EscenaMenu)
        self.pilasengine.escenas.EscenaMenu()
        

pilasengine.escenas.vincular(PantallaAyuda)
pilasengine.escenas.PantallaAyuda()

