#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
	Módulo: monkyPingui
	Diseño: M.Alejandra y Eliana
	Código: M.Alejandra y Eliana
	---

	Este es el archivo principal del juego monkyPingui.
	Contiene las importaciones de todos los modulos y es donde se vinculan las escenas.
	La escena Menu debe ser la primera en ser mostrada por lo que se ejecuta justo antes de pilas.

 """
import pilasengine
import ayuda
import menu
import juego
import resultados
import versus

pilas = pilasengine.iniciar()

pilas.escenas.vincular(menu.EscenaMenu)
pilas.escenas.vincular(ayuda.PantallaAyuda)
pilas.habilidades.vincular(juego.Girar_como_reloj)
pilas.escenas.vincular(juego.Nivel)
pilas.escenas.vincular(juego.Nivel_2)
pilas.escenas.vincular(resultados.Resultados)
pilas.escenas.vincular(resultados.Ranking)
pilas.escenas.vincular(versus.Round)
pilas.escenas.EscenaMenu()
pilas.ejecutar()
