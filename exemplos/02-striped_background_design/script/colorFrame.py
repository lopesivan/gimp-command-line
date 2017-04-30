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

from gimpfu import *

def set_frame(img, layer, colour1, colour2, colour3, colour4, frame_width):
	
	w = img.width
	h = img.height
	fw = frame_width * 2

	colours = [colour1, colour2, colour3, colour4]

	rectangles = [(0,0,w,fw), # norte
		      (w-fw,0,fw,h), # oeste
		      (0,h-fw,w,fw), # sur
		      (0,fw,fw,h)] # este

	for c,r in zip(colours,rectangles):
		draw_rectangle(img, layer, c, r)

		
def draw_rectangle(img, layer, c, r):

	pdb.gimp_context_set_foreground(c)

	x_top_left = r[0]
	y_top_left = r[1]
	width = r[2]
	height = r[3]

	pdb.gimp_rect_select(img, x_top_left, y_top_left, width, height, CHANNEL_OP_ADD, 0, 0)
	pdb.gimp_edit_bucket_fill(layer, FG_BUCKET_FILL, NORMAL_MODE,100, 0, 0, 0, 0) 
	pdb.gimp_selection_none(img)
	
register(
	"color_frame",	
	"Enmarca con 4 colores",	
	"Enmarcando con colores",
	"Juanjo Conti",
	"Juanjo Conti",
	"2006",
	"<Image>/Python-Fu/ColorFrame",
	"",
	[
		(PF_COLOR, "colour1", "Norte:", (0,237,237)),
		(PF_COLOR, "colour2", "Oeste:", (237,0,237)),
		(PF_COLOR, "colour3", "Sur:", (237,237,0)),
		(PF_COLOR, "colour4", "Este:", (1,1,37)),
	        (PF_SPINNER, "frame_width", "Ancho del marco", 20, (1,100,1))
	],
	[],
	set_frame)

main()
