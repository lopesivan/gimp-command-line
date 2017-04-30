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
# Copyright 2007 - Juan José Conti <jjconti@gnu.org>
# Copyleft :-)

from gimpfu import *

def pixels_read(img, layer):
	
    w = layer.width
    h = layer.height
    pr = layer.get_pixel_rgn(0, 0, w, h)
    
    print "Valores de los pixeles de las esquinas de la imagen"

    r,g,b = pr[0,0]
    print [ord(x) for x in r,g,b]

    r,g,b = pr[0,4]
    print [ord(x) for x in r,g,b]

    r,g,b = pr[4,0]
    print [ord(x) for x in r,g,b]

    r,g,b = pr[4,4]
    print [ord(x) for x in r,g,b]

    layer.update(0, 0, w, h)
    layer.flush()
    gimp.displays_flush()

register(
	"pixels_read",	
	"Prueba con pixels",	
	"Prueba con pixels",
	"Juanjo Conti",
	"Juanjo Conti",
	"2007",
	"<Image>/Python-Fu/Pixels/PixelsRead",
	"",
	[],
	[],
	pixels_read)

main()
