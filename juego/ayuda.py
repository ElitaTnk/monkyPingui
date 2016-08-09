# -*- coding: UTF-8 -*-
"""
    Módulo: ayuda
    Diseño: M.Alejandra
    Código: M.Alejandra y Eliana
    ---
    Este módulo solo contiene la importacion del framework y la clase logo de menu.
    La clase PantallaAyuda es la escena que contiene las instrucciones del juego.

"""
import pilasengine
from menu import Logo
from menu import BotonMejorado


texto_ayuda = "Mové a Pingui con el teclado y saltá sobre el personaje distinto, el que consideres que no se repite ;) .  El nivel se acaba cuando se termina el tiempo. Tenés que hacer al menos 1 puntos por nivel. Si elegis mal, perdes una vida. ¡Cuidado!."

#decode de texto para que se pueda usar acentos
texto_ayuda = texto_ayuda.decode('utf-8')

class PantallaAyuda(pilasengine.escenas.Escena):
    """ esta pantalla utiliza la variable texto_ayuda"""

    def iniciar(self):
        self.pilas.fondos.Tarde()
        self.crear_texto_ayuda()
        self.boton = BotonMejorado(self.pilas, "Volver al inicio", -100)

        self.logo = Logo(self.pilas)

    def crear_texto_ayuda(self):
        self.pilas.actores.Texto("Como se juega?:" , y = 50, fuente = "data/fuentes/Bangers.ttf")
        self.pilas.actores.Texto(texto_ayuda,  magnitud = 16, ancho = 600, y = -30)
