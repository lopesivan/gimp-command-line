#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, glob, sys, time
from math import *
from gimpfu import *
import gimpfu # access constantes

def new_image(dpi, height, width):
    # crio uma imagem
    image = pdb.gimp_image_new(width, height, gimpfu.RGB)

    # set resolution
    pdb.gimp_image_set_resolution(image, dpi, dpi)

    return image

def new_layer(image, layer_name):
    width = image.width
    height = image.height
    layer = pdb.gimp_layer_new(image, width, height, gimpfu.RGB_IMAGE, layer_name, 100, gimpfu.NORMAL_MODE)

    # adiciono alpha, para poder recortar futuramente
    pdb.gimp_layer_add_alpha(layer)

    # junto a camada a imagem
    pdb.gimp_image_add_layer(image, layer, 0)

    # pinto a camada layer1 com a cor do plano da frente
    pdb.gimp_drawable_fill(layer, gimpfu.FOREGROUND_FILL)

    return layer

def Main(width,
         height,
         oimage,
         debug):
    """
    Main
    """

    dpi = 300
    image = new_image(dpi, height, width)

    # DEBUG
    # desabilitar undo
    if not debug:
        pdb.gimp_image_undo_disable(image)

    # cria uma camada de nome `layer1'
    layer1 = new_layer(image,
                       "layer1")

    #########################################################################
    #########################################################################
    #########################################################################

    if debug:
        print("DEBUG is TRUE")
        display = pdb.gimp_display_new(image)
    else:
        # junta asd imagens
        drawable = pdb.gimp_image_merge_visible_layers(image, gimpfu.CLIP_TO_IMAGE)

        if not (os.path.exists('processed')):
            os.mkdir('processed')

        filename = "processed/" + oimage
        pdb.file_png_save2(image, drawable, filename, filename, 0, 9, 0, 0, 0, 0, 0, 0, 0)
        # clean
        pdb.gimp_image_delete(image);
    # end if

# end def Main

def run(width, height, oimage, debug):
    #gimp.progress_init("Doing stuff to ...")

    start = time.time()

    Main(width,
         height,
         oimage,
         debug)

    end = time.time()
    print("Finished, total processing time: %.2f seconds" % (end - start))

# end def run

