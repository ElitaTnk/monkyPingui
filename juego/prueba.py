#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pilasengine
import ayuda
import menu
import juego

pilas = pilasengine.iniciar()

pilas.escenas.vincular(menu.EscenaMenu)
pilas.escenas.vincular(ayuda.PantallaAyuda)
pilas.escenas.vincular(juego.Nivel)

pilas.escenas.EscenaMenu()
pilas.ejecutar()