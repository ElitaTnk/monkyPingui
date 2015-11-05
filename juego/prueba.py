#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pilasengine
import ayuda
import menu
import juego
import resultados

pilas = pilasengine.iniciar()

pilas.escenas.vincular(menu.EscenaMenu)
pilas.escenas.vincular(ayuda.PantallaAyuda)
pilas.escenas.vincular(juego.Nivel)
pilas.escenas.vincular(juego.Nivel_2)
pilas.escenas.vincular(resultados.Resultados)
pilas.escenas.vincular(resultados.Ranking)
pilas.escenas.EscenaMenu()
pilas.ejecutar()
