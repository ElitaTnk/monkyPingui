# coding: utf-8

import pilasengine
pilas = pilasengine.iniciar()

#Escena de inicio de juego, para comenzar a jugar el usuario deberá hacer click en el botón de 'comenzar'.

class PantallaBienvenida(pilasengine.escenas.Escena):
	"""definimos una escena nueva a partir de ··ver que corno es pantallaBienvenida·· y va a tener un texto de bienvenida"""
	def iniciar(self, mensaje):
		pilas.fondos.Tarde()
		self.texto = pilas.actores.Texto(mensaje)

#creamos el botón de comenzar
boton = pilas.interfaz.Boton("Comenzar")
boton.y = -100

#acción del botón
def comenzar():
	pilas.escenas.Nivel1()
    
boton.conectar(comenzar)


