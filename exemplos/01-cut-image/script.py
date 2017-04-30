#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, glob, sys, time
import gimpfu # access constantes
from gimpfu import *

def add_borda(filename):

    print("Load file \"%s\"" % filename)

    if not (os.path.exists('processed')):
        os.mkdir('processed')

    if not (os.path.exists(filename)):
        sys.exit('ERROR: Database %s was not found!' % filename)

    image = pdb.gimp_file_load(filename, filename)

    width = image.width
    height = image.height

    print("A imagem %s tem dimenções iguais a %sx%s" % (filename, width, height))

    #fundo é preto e frente branca
    pdb.gimp_context_set_background((0,0,0))
    pdb.gimp_context_set_foreground((255, 255, 255))

    _width = 500
    _height = 800
    _left = 50
    _top = 10
    pdb.gimp_image_crop(image, _width, _height, _left, _top)
    drawable = pdb.gimp_image_merge_visible_layers(image, gimpfu.CLIP_TO_IMAGE)
    new_path = './processed/new-' + filename.replace("./", "")
    pdb.gimp_file_save(image, drawable, new_path, 'Saved image')
    pdb.gimp_image_delete(image);

def run(filename):

    #gimp.progress_init("Doing stuff to ...")

    start = time.time()

    add_borda(filename)

    end = time.time()
    print("Finished, total processing time: %.2f seconds" % (end - start))

#args = [(PF_STRING, 'file', 'GlobPattern', '*.*')]
#register('ivan-flip', '', '', '', '', '', '', '', args, [], run)
