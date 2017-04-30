#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#
# Copyright 2006 - Juan José Conti <jjconti@gnu.org>
# Copyleft :-)
# Este plug-in de ejemplo fué usado en la Presentación: 
# Creando plug-ins para GIMP con Python realizada en el 
# 1º PythonDay organizado por el Grulic

from random import random, uniform
from gimpfu import *

def gen_sky(width, height, bg_colour, stars_colour, radio_min, radio_max, number_stars, clouds):

	pdb.gimp_context_set_background(bg_colour)
	pdb.gimp_context_set_foreground(stars_colour)

	img = pdb.gimp_image_new(width, height, RGB)
	layer = pdb.gimp_layer_new(img, width, height, RGB_IMAGE, "Stars", 100, NORMAL_MODE)
	pdb.gimp_image_add_layer(img,layer,0)

	pdb.gimp_drawable_fill(layer,BACKGROUND_FILL)

	draw_stars(img, layer, stars_colour, radio_min, radio_max, number_stars)
		
	if clouds == True:
		pdb.python_fu_foggify(img, layer, "Nubes", (255,255,255), 1.5, 10)
		layer = img.layers[0]
		pdb.plug_in_mblur(img, layer, 0, 30, 0, width / 2, height / 2) 

	pdb.gimp_display_new(img)
		
def draw_stars(img, layer, stars_colour, radio_min, radio_max, number_stars):
	
	rayos = 1
	tono = 100
	
	for s in range(number_stars):
		radio = int(uniform(radio_min,radio_max+1))
		x = random() * img.width
		y = random() * img.height
	
		print "Estrella: ",s," - radio: ",radio
		pdb.plug_in_nova(img, layer, x, y, stars_colour, radio, rayos, tono) 
	
register(
	"gen_sky",	
	"Crea un cielo estrellado",	
	"Crea un cielo estrellado",
	"Juanjo Conti",
	"Juanjo Conti",
	"2006",
	"<Toolbox>/Xtns/Python-Fu/Cielo",
	"",
	[
		(PF_INT, "width", "Ancho de la imagen", 500),
		(PF_INT, "height", "Alto de la imagen", 400),
		(PF_COLOR, "bg_colour", "Color de fondo:", (5,35,95)),
		(PF_COLOR, "stars_colour", "Color de las estrellas:", (237,237,237)),
		(PF_SPINNER, "radio_min", "Radio mínimo de cada estrella", 1, (1,10,1)),
		(PF_SPINNER, "radio_max", "Radio máximo de cada estrella", 2, (1,10,1)),
	        (PF_SPINNER, "number_stars", "Número de estrellas", 20, (1,500,1)),
		(PF_TOGGLE, "clouds", "Nubes:", False)
	],
	[],
	gen_sky)

main()
