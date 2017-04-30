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
# Constellations Drawing Library

from math import *
from gimpfu import *

def draw_stars_circle(img, layer, n, rad, X_BASE, Y_BASE, off_def, total_n):

	ang = (2*pi)/n
	ang_offset = ang / off_def
	ang_sum = ang + ang_offset
	i = 1
	
	while(i <= n):
		x_offset = sin(ang_sum) * rad
		y_offset = cos(ang_sum) * rad

		draw_star(img, layer, X_BASE + x_offset, Y_BASE + y_offset, total_n)
		
		i += 1
		ang_sum += ang

def draw_stars_grid(img, layer, n, rad, X_BASE, Y_BASE):

	y = y_top_left = Y_BASE - cos(pi/4) * rad
	x = x_top_left = X_BASE - sin(pi/4) * rad
	s = int(sqrt(n)) # stars in the side of the main square
	step = ((X_BASE - x_top_left) * 2) / (s-1)
	print "DEBUG : step grid ", step


	for i in range(s):
		for j in range(s):
			draw_star(img, layer, x, y, n)
			x += step
		x = x_top_left
		y += step


def draw_stars_square(img, layer, n, rad, X_BASE, Y_BASE):

	y = y_top_left = Y_BASE - cos(pi/4) * rad
	x = x_top_left = X_BASE - sin(pi/4) * rad
	s = (n+4)/4 # stars in the side of the square
	step = ((X_BASE - x_top_left) * 2) / (s-1)

	for i in range(s):
			draw_star(img, layer, x, y, n)
			x += step
	for i in range(s-2):
		x = x_top_left
		y += step
		draw_star(img, layer, x, y, n)
		x += step * (s-1)
		draw_star(img, layer, x, y, n)
	x = x_top_left
	y += step
	for i in range(s):
		draw_star(img, layer, x, y, n)
		x += step

		
def draw_star(img, layer, x, y, n):

	if (n < 30): size = 12
	elif (n < 200): size = 6
	else: size = 3
	x_top_left = x - size/2.
	y_top_left = y - size/2.

	pdb.gimp_ellipse_select(img, x_top_left, y_top_left, size, size, CHANNEL_OP_ADD, False, 0, 0)
	pdb.gimp_edit_bucket_fill(layer, FG_BUCKET_FILL, NORMAL_MODE,100, 0, 0, 0, 0) 
	pdb.gimp_selection_none(img)


def draw_desicion_area(img, layer, x, y, size):

	x_top_left = x - size/2.
	y_top_left = y - size/2.

	pdb.gimp_ellipse_select(img, x_top_left, y_top_left, size, size, CHANNEL_OP_ADD, False, 0, 0)
	pdb.gimp_edit_bucket_fill(layer, FG_BUCKET_FILL, NORMAL_MODE,100, 0, 0, 0, 0) 
	pdb.gimp_selection_none(img)


def set_text(img, layer, x, y, text, size):
	# last parameter, font name, must be installed in the system 
	return pdb.gimp_text_fontname(img, layer, x, y, text, 1, False, size, PIXELS,"URW Gothic L")


def draw_circle(img, layer, x_center, y_center, rad):
	
	width = 2 # line width in pixels
	rad = rad + width/2.
	x_top_left = x_center - rad
	y_top_left = y_center - rad
	
	pdb.gimp_ellipse_select(img, x_top_left, y_top_left, 2*rad, 2*rad, CHANNEL_OP_ADD, False, 0, 0)
	# when gimp stable relase suport defining stroke preferences this function
	# will looks nicer
	# pdb.gimp_edit_stroke(layer)
	# meanwhile..
	pdb.gimp_edit_bucket_fill(layer, FG_BUCKET_FILL, NORMAL_MODE,100, 0, 0, 0, 0) 
	pdb.gimp_selection_none(img)
	rad = rad - width
	x_top_left = x_center - rad
	y_top_left = y_center - rad
	pdb.gimp_ellipse_select(img, x_top_left, y_top_left, 2*rad, 2*rad, CHANNEL_OP_ADD, False, 0, 0)
	pdb.gimp_edit_bucket_fill(layer, BG_BUCKET_FILL, NORMAL_MODE,100, 0, 0, 0, 0) 
	pdb.gimp_selection_none(img)


def draw_axis(img, layer, total_width, total_height):
	
	width = 3 # line width in pixels
	x_center = total_width / 2.
	y_center = total_height / 2.
	
	# y axis
	x_top_left = x_center - width/2.
	y_top_left = 0
	pdb.gimp_rect_select(img, x_top_left, y_top_left, width, total_height, CHANNEL_OP_ADD, 0, 0)

	# x axis
	x_top_left = 0
	y_top_left = y_center - width/2.
	pdb.gimp_rect_select(img, x_top_left, y_top_left, total_width, width, CHANNEL_OP_ADD, 0, 0)

	pdb.gimp_edit_bucket_fill(layer, FG_BUCKET_FILL, NORMAL_MODE,100, 0, 0, 0, 0) 
	pdb.gimp_selection_none(img)

	float_text = pdb.gimp_text_fontname(img, layer, x_center + 2, 0, "Q", 1, False, 18, PIXELS,"URW Gothic L, Bold")
	pdb.gimp_floating_sel_anchor(float_text)

	float_text = pdb.gimp_text_fontname(img, layer, x_center * 2 - 15, y_center - 30, "I", 1, False, 18, PIXELS,"URW Gothic L, Bold")
	pdb.gimp_floating_sel_anchor(float_text)
