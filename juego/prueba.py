# -*- coding: utf-8 -*-

import pilasengine
import ayuda
import menu

pilas = pilasengine.iniciar()
pilas.escenas.vincular(menu.EscenaMenu)
pilas.escenas.vincular(ayuda.PantallaAyuda)
pilas.escenas.EscenaMenu()
pilas.ejecutar()