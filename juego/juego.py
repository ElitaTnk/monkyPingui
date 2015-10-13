# -*- coding: utf-8 -*-

import pilasengine
import pilasengine.colores



class Barra_tiempo(pilasengine.actores.Temporizador):
    #nueva barra de tiempo, con imagen y cambio de argumentos
    def iniciar(self):
        self.imagen = "data/152-clock.png"
        self.texto = self.pilas.actores.Texto("0")
        self.texto.color = pilasengine.colores.negro
        self.y = 160
        self.x = 260
        self.texto.y = 100
        self.texto.x = 250
        

class Nivel(pilasengine.escenas.Escena):
        #escena del primer nivel. Se instancia la barra de tiempo,personajes y da inicio
       def iniciar(self):
        self.pilas.fondos.Selva()
        self.tiempo = Barra_tiempo(self.pilas)      
        #se asigna un mensaje al final
        self.tiempo.ajustar(30, self.hola_mundo)
        self.tiempo.comenzar()
        self.personajes()
        

       def personajes(self): 
           self.mono = self.pilas.actores.Mono()
           self.mono.x = -180
           self.mono1 = self.pilas.actores.Mono() 
           self.mono1.x = 0
           self.zanahoria = self.pilas.actores.Zanahoria()
           self.zanahoria.x = 180 
           self.nave = self.pilas.actores.NaveRoja()
           self.nave.y = -180 
                       
       def hola_mundo(self):
            self.pilas.avisar("Fin del primer nivel")   
     
  
 
  
              
    
   
    



   
        
        
        
       
    
    
