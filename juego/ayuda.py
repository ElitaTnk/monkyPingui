# -*- coding: UTF-8 -*-
import pilasengine
from menu import Logo

texto_ayuda = "Mové a Pingui con el teclado y saltá sobre el personaje distinto, el que consideres que no se repite ;) .  El nivel se acaba cuando se termina el tiempo. Tenés que hacer al menos 1 puntos por nivel. Si elegis mal, perdes una vida. ¡Cuidado!."

#decode de texto para que se pueda usar acentos 
texto_ayuda = texto_ayuda.decode('utf-8')

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
        self.logo = Logo(self.pilas)

    def crear_texto_ayuda(self):
        self.pilas.actores.Texto("Como se juega?:" , y = 50, fuente = "data/fuentes/Bangers.ttf")
        self.pilas.actores.Texto(texto_ayuda,  magnitud = 16, ancho = 600, y = -30)
            
    def regresa_inicio(self):
        #vuelve la escena de inicio y ejecuta el cambio de pantalla
        self.pilas.escenas.EscenaMenu()

