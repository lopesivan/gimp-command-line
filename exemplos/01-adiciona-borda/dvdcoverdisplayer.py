#!/usr/bin/python

# Gimp3Dvd -- draw 3d versions of a DVD cover. A Gimp-Python plugin.
# Copyright Stuart Langridge (http://www.kryogenix.org/code/gimp3dvd/) 2005
# Version 1.0
# License GPL

# Installation : put the photomaton.py file in your $HOME/.gimp-2.n/plug-ins.
# On Linux and Mac OSX the photomaton.py file must be executable.

import math
from gimpfu import *

def python_fu_dvdcover(img,drawable):
  cover = img.duplicate()
  pdb.gimp_image_flatten(cover)
  cover.active_layer = cover.layers[0]
  pdb.gimp_layer_add_alpha(cover.active_layer)
  
  SPINE_WIDTH = int(((784.0-704)/1490) * cover.width)
  SPINE_LEFT = (cover.width / 2) - (SPINE_WIDTH / 2)
  SPINE_RIGHT = SPINE_LEFT + SPINE_WIDTH
  
  EDGE_SPACING = 30
  UNIT = int(cover.height * (40.0 / 750) )
  
  # Columns are defined as x, (distance between y and the edge)
  COL1 = ( 2.5 * UNIT, UNIT )
  COL2 = ( int(cover.width / 2) , int(0.2 * UNIT) )
  COL3 = ( SPINE_RIGHT , 0 )
  COL4 = ( cover.width - (2 * UNIT) , 2 * UNIT )
  
  bglayer = cover.active_layer
  
  # transform left (do this first so it goes under the spine)
  pdb.gimp_rect_select(cover, 
      0 , 0, SPINE_LEFT, cover.height, 2, 0, 0)
  pdb.gimp_drawable_transform_perspective_default(cover.active_layer,
    COL1[0] + EDGE_SPACING, COL1[1] + EDGE_SPACING,
    COL2[0], COL2[1] + EDGE_SPACING + int(UNIT / 5),
    COL1[0] + EDGE_SPACING, cover.height - (COL1[1] + EDGE_SPACING),
    COL2[0], cover.height - (COL2[1] + EDGE_SPACING + int(UNIT / 5)),
    1, 0)
  pdb.gimp_floating_sel_to_layer(cover.active_layer)
  leftlayer = cover.active_layer
  pdb.gimp_layer_set_preserve_trans(cover.active_layer,0)
  pdb.gimp_layer_resize_to_image_size(cover.active_layer)
  cover.active_layer = bglayer

  # transform spine
  pdb.gimp_rect_select(cover, 
      SPINE_LEFT, 0, SPINE_WIDTH, cover.height, 2, 0, 0)
  pdb.gimp_drawable_transform_perspective_default(cover.active_layer,
    COL2[0], COL2[1] + EDGE_SPACING,
    COL3[0], COL3[1] + EDGE_SPACING,
    COL2[0], cover.height - (COL2[1] + EDGE_SPACING),
    COL3[0], cover.height - (COL3[1] + EDGE_SPACING),
    1, 0)  
  pdb.gimp_floating_sel_to_layer(cover.active_layer)
  spinelayer = cover.active_layer
  pdb.gimp_layer_set_preserve_trans(cover.active_layer,0)
  pdb.gimp_layer_resize_to_image_size(cover.active_layer)
  cover.active_layer = bglayer
  
  # transform right
  pdb.gimp_rect_select(cover, 
      SPINE_RIGHT, 0, cover.width - SPINE_RIGHT, cover.height, 2, 0, 0)
  pdb.gimp_drawable_transform_perspective_default(cover.active_layer,
    COL3[0], COL3[1] + EDGE_SPACING,
    COL4[0] - EDGE_SPACING, COL4[1] + EDGE_SPACING,
    COL3[0], cover.height - (COL3[1] + EDGE_SPACING),
    COL4[0] - EDGE_SPACING, cover.height - (COL4[1] + EDGE_SPACING),
    1, 0)
  pdb.gimp_floating_sel_to_layer(cover.active_layer)
  rightlayer = cover.active_layer
  pdb.gimp_layer_set_preserve_trans(cover.active_layer,0)
  pdb.gimp_layer_resize_to_image_size(cover.active_layer)
  cover.active_layer = bglayer

  # draw lines
  current_brush = pdb.gimp_context_get_brush()
  gimp.set_foreground(0,0,0)
  pdb.gimp_context_set_brush("Circle Fuzzy (07)")
  pdb.gimp_paintbrush(leftlayer,10000,4,[
    COL1[0] + EDGE_SPACING, COL1[1] + EDGE_SPACING,
    COL1[0] + EDGE_SPACING, cover.height - (COL1[1] + EDGE_SPACING)
    ],0,0)
  pdb.gimp_paintbrush(leftlayer,10000,4,[
    COL1[0] + EDGE_SPACING, COL1[1] + EDGE_SPACING,
    COL2[0], COL2[1] + EDGE_SPACING + int(UNIT/5)
    ],0,0)
  pdb.gimp_paintbrush(leftlayer,10000,4,[
    COL1[0] + EDGE_SPACING, cover.height - (COL1[1] + EDGE_SPACING),
    COL2[0], cover.height - (COL2[1] + EDGE_SPACING + int(UNIT / 5))
    ],0,0)

  pdb.gimp_paintbrush(spinelayer,10000,4,[
    COL2[0], COL2[1] + EDGE_SPACING,
    COL3[0], COL3[1] + EDGE_SPACING
    ],0,0)
  pdb.gimp_paintbrush(spinelayer,10000,4,[
    COL2[0], cover.height - (COL2[1] + EDGE_SPACING),
    COL3[0], cover.height - (COL3[1] + EDGE_SPACING)
    ],0,0)

  pdb.gimp_paintbrush(rightlayer,10000,4,[
    COL3[0], COL3[1] + EDGE_SPACING,
    COL4[0] - EDGE_SPACING, COL4[1] + EDGE_SPACING
    ],0,0)
  pdb.gimp_paintbrush(rightlayer,10000,4,[
    COL4[0] - EDGE_SPACING, COL4[1] + EDGE_SPACING,
    COL4[0] - EDGE_SPACING, cover.height - (COL4[1] + EDGE_SPACING)
    ],0,0)
  pdb.gimp_paintbrush(rightlayer,10000,4,[
    COL3[0], cover.height - (COL3[1] + EDGE_SPACING),
    COL4[0] - EDGE_SPACING, cover.height - (COL4[1] + EDGE_SPACING)
    ],0,0)

  pdb.gimp_context_set_brush(current_brush)

  # add drop shadow
  lastlayer = pdb.gimp_image_merge_visible_layers(cover,0)
  pdb.script_fu_drop_shadow(cover,lastlayer,0,0,70,(0,0,0),80,0)
  pdb.gimp_image_flatten(cover)

  gimp.Display(cover)
  gimp.displays_flush()

register(
   "Dvddisplay",
   "DO some DVD stuff",
   "Some help text",
   "Stuart Langridge",
   "GPL License",
   "2005",
   "<Image>/Python-Fu/DVD Cover",
   "",
   [],
   [],
   python_fu_dvdcover
   )

main()
