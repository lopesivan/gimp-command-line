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

# Rectangular QAM Constelation __2nd way__

from math import *
from gimpfu import *
from constellations import *

def gen_constellation_qam_r_ko2(bg_colour, stars_colour, area_colour, axis_colour, power):

	img_width = img_height = 350
	n = int(pow(2,power))
	diam = img_width * 0.8
	rad = diam / 2.
	X_BASE = Y_BASE = img_width / 2.
	
	img = pdb.gimp_image_new(img_width, img_height, RGB)
	layer = pdb.gimp_layer_new(img, img_width, img_height, RGB_IMAGE, "QAM", 100, NORMAL_MODE)
	pdb.gimp_image_add_layer(img,layer,0)

	pdb.gimp_context_set_background(bg_colour)
	pdb.gimp_drawable_fill(layer,BACKGROUND_FILL)

	pdb.gimp_context_set_foreground(axis_colour)
	draw_axis(img, layer, img_width, img_height)
	
	# draw desicion area for one star
	pdb.gimp_context_set_foreground(area_colour)
	
	s = int(sqrt(min_perf_sqrt_grat_than(n))) # stars in the side of the square
	step = (sin(pi/4) * diam) / (s-1)
	
	# some ugly code
	if (n == 32):
		x = X_BASE + step * 1.5 
		y = Y_BASE - step * 1.5
	if (n == 128):
		x = X_BASE + step * 3.5
		y = Y_BASE - step * 3.5
	else: # no area drawing
		pass
	
	draw_desicion_area(img, layer, int(x), int(y), step)

	pdb.gimp_context_set_foreground(stars_colour)
	temp_stars =  min_perf_sqrt_grat_than(n)
	draw_stars_grid(img, layer, temp_stars, rad, X_BASE, Y_BASE)

	# delete some stars :)
	w = h = 32
	for (x,y) in ((70, 70), (248,70), (70,245), (245,245)):
		pdb.gimp_rect_select(img, x, y, w, h, CHANNEL_OP_ADD, 0, 0)
	pdb.gimp_edit_bucket_fill(layer, BG_BUCKET_FILL, NORMAL_MODE,100, 0, 0, 0, 0) 
	pdb.gimp_selection_none(img)

	float_text = set_text(img, layer, 270, 310, str(n)+"-QAM", 16)
	pdb.gimp_floating_sel_anchor(float_text)
	float_text = set_text(img, layer, 266, 327, "rectangular", 14)
	pdb.gimp_floating_sel_anchor(float_text)
		
	pdb.gimp_selection_none(img)
	pdb.gimp_display_new(img)

def min_perf_sqrt_grat_than(n):
	r = min(filter(lambda i: i > n, map(lambda j: j*j, range(13))))
	return float(r)
		

register(
	"gen_constellation_qam_r_ko2",
	"Generate a rectangular QAM modulation constelation",
	"Generate a rectangular QAM modulation constelation",
	"Juanjo Conti",
	"Juanjo Conti",
	"2006",
	"<Toolbox>/Xtns/Python-Fu/Constellations/rectangular-QAM-kodd2",
	"",
	[
		(PF_COLOR, "bg_colour", "Color de fondo:", (255,255,255)),
		(PF_COLOR, "stars_colour", "Color de las estrellas:", (0,0,0)),
		(PF_COLOR, "area_colour", "Color del area de desicion:", (232,255,236)),
		(PF_COLOR, "axis_colour", "Color de los ejes de coordenadas:", (232,232,232)),
        (PF_SPINNER, "power", "El numero de estrellas en la constelacion es 2^:", 7, (5,7,2))
	],
	[],
	gen_constellation_qam_r_ko2)

main()
