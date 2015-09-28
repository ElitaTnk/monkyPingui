# -*- coding: utf-8 -*-

import pilasengine

texto_ayuda = """Aca hay que poner las indicaciones de como jugar :D """


class PantallaAyuda(pilasengine.escenas.Escena):
    #en esta pantalla se dan las instrucciones de juego
    #creación de la clase para la nueva pantalla a partir de la clase madre pilas.escena.Escena
    
    def iniciar(self):
        #instanciamos el fondo deseado y creamos métodos para mostrar los textos de ayuda y el boton de volver
        self.pilas.fondos.Tarde()
        self.crear_texto_ayuda()
        self.boton = self.pilas.interfaz.Boton("Volver al Inicio")
        self.boton.y = -100
        self.boton.conectar(self.regresa_inicio)


    def crear_texto_ayuda(self):
        self.pilas.actores.Texto("Como se juega?:" , y = 100)
        self.pilas.actores.Texto(texto_ayuda)
            
    def regresa_inicio(self):
        #importa la escena de inicio y ejecuta el cambio de pantalla

        self.pilas.escenas.EscenaMenu()

