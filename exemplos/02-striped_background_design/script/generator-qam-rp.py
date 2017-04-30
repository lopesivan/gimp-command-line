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

# Rectangular QAM Constelation __k pair in 2^k = N__

from math import *
from gimpfu import *
from constellations import *

def gen_constellation_qam_r_kp(bg_colour, stars_colour, area_colour, axis_colour, power):

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

	# draw desicion area for one star
	pdb.gimp_context_set_foreground(area_colour)

	x = X_BASE + sin(pi/4) * rad
	y = Y_BASE - cos(pi/4) * rad
	s = sqrt(n) # stars in the side of the main square
	size = ((x - X_BASE) * 2) / (s-1)

	draw_desicion_area(img, layer, x, y, size)

	pdb.gimp_context_set_foreground(axis_colour)
	draw_axis(img, layer, img_width, img_height)

	pdb.gimp_context_set_foreground(stars_colour)
	draw_stars_grid(img, layer, n, rad, X_BASE, Y_BASE)

	float_text = set_text(img, layer, 270, 310, str(n)+"-QAM", 16)
	pdb.gimp_floating_sel_anchor(float_text)
	float_text = set_text(img, layer, 266, 327, "rectangular", 14)
	pdb.gimp_floating_sel_anchor(float_text)
		
	pdb.gimp_selection_none(img)
	pdb.gimp_display_new(img)
		

register(
	"gen_constellation_qam_r_kp",
	"Generate a rectangular QAM modulation constelation",
	"Generate a rectangular QAM modulation constelation",
	"Juanjo Conti",
	"Juanjo Conti",
	"2006",
	"<Toolbox>/Xtns/Python-Fu/Constellations/rectangular-QAM-kpair",
	"",
	[
		(PF_COLOR, "bg_colour", "Color de fondo:", (255,255,255)),
		(PF_COLOR, "stars_colour", "Color de las estrellas:", (0,0,0)),
		(PF_COLOR, "area_colour", "Color del area de desicion:", (232,255,236)),
		(PF_COLOR, "axis_colour", "Color de los ejes de coordenadas:", (232,232,232)),
        (PF_SPINNER, "power", "El numero de estrellas en la constelacion es 2^:", 4, (2,8,2))
	],
	[],
	gen_constellation_qam_r_kp)

main()
