#!/usr/bin/env python
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
# Copyright 2006 - Juan Jose Conti <jjconti@gnu.org>
# Copyleft :-)
#
# Circular QAM Constelation --multi lines--

from math import *
from gimpfu import *
from constellations import *

def gen_constellation_qam_c_m(bg_colour, stars_colour, circles_colour, axis_colour, power):

	img_width = img_height = 350
	n = int(pow(2,power))
	diam = img_width * 0.8
	rad = diam / 2
	X_BASE = Y_BASE = img_width / 2
	
	img = pdb.gimp_image_new(img_width, img_height, RGB)
	layer = pdb.gimp_layer_new(img, img_width, img_height, RGB_IMAGE, "QAM", 100, NORMAL_MODE)
	pdb.gimp_image_add_layer(img,layer,0)

	pdb.gimp_context_set_background(bg_colour)
	pdb.gimp_drawable_fill(layer,BACKGROUND_FILL)

	circles = max(1, n / 4)
	rad_offset = rad / circles
	i = circles
	
	pdb.gimp_context_set_foreground(circles_colour)
	
	while(i > 0):
		draw_circle(img, layer, X_BASE, Y_BASE, i * rad_offset)
		i -= 1

	pdb.gimp_context_set_foreground(axis_colour)
	draw_axis(img, layer, img_width, img_height)

	pdb.gimp_context_set_foreground(stars_colour)
	starts_per_circle = min(n, 4)
	i = circles
	while(i > 0):
		draw_stars_circle(img, layer, min(n,4), i * rad_offset, X_BASE, Y_BASE, i%2 + 1, n)
		i -= 1
	
	float_text = set_text(img, layer, 275, 310, str(n)+"-QAM", 16)
	pdb.gimp_floating_sel_anchor(float_text)
	float_text = set_text(img, layer, 277, 327, "circular-m", 14)
	pdb.gimp_floating_sel_anchor(float_text)
		
	pdb.gimp_selection_none(img)
	pdb.gimp_display_new(img)
		

register(
	"gen_constellation_qam_c_m",
	"Generate a QAM modulation constelation",
	"Generate a QAM modulation constelation",
	"Juanjo Conti",
	"Juanjo Conti",
	"2006",
	"<Toolbox>/Xtns/Python-Fu/Constellations/circular-QAM-multiline",
	"",
	[
		(PF_COLOR, "bg_colour", "Color de fondo:", (255,255,255)),
		(PF_COLOR, "stars_colour", "Color de las estrellas:", (0,0,0)),
		(PF_COLOR, "circles_colour", "Color de las circunferencias:", (216,255,255)),
		(PF_COLOR, "axis_colour", "Color de los ejes de coordenadas:", (232,232,232)),
        (PF_SPINNER, "power", "El numero de estrellas en la constelacion es 2^:", 3, (1,8,1))
	],
	[],
	gen_constellation_qam_c_m)

main()
