# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

class PantallaBienvenida(pilasengine.escenas.Escena):

    def iniciar(self, mensaje):
        pilas.fondos.Tarde()
        self.texto = pilas.actores.Texto(mensaje)
        
pilas.escenas.vincular(PantallaBienvenida)
pilas.escenas.PantallaBienvenida("MonkyPingui\n Bienvenido")

boton = pilas.interfaz.Boton("Comenzar")
boton.y = -100

def comenzar():
    pilas.escenas.Normal()
    
boton.conectar(comenzar)

pilas.ejecutar()