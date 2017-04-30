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

    # Criando nova camada
    layer = pdb.gimp_layer_new(image,
                               width,
                               height,
                               gimpfu.RGB_IMAGE,
                               "camada_1",
                               100,
                               gimpfu.NORMAL_MODE)

    # adiciono filtro alpha pq ao usar `pdb.gimp_selection_none (image)',
    # a imagem selecionada deve ser transparente.
    pdb.gimp_layer_add_alpha(layer)

    # junto imagem e a camada
    pdb.gimp_image_add_layer(image, layer, 0)

    # Preencho a camada com a cor de foreground que é branca
    pdb.gimp_drawable_fill(layer, gimpfu.FOREGROUND_FILL)

    # modo debug ...
    #display = pdb.gimp_display_new(image)

    # Limpa área de seleção
    pdb.gimp_selection_none (image)

    # Cria uma seleção em formato de retângulo
    # mantendo uma sombra de 10 pixels de cada lado
    x = 10
    y = 15
    pdb.gimp_rect_select (image, x, y, (width -2*x), (height-2*y), 0, 0,0)

    # remove o conteúdo da selecao ativa,
    # somente da camada branca
    pdb.gimp_edit_clear (layer)

    # retira a seleção da imagem
    pdb.gimp_selection_none (image)

    display = pdb.gimp_display_new(image)

    #drawable = pdb.gimp_image_merge_visible_layers(image, gimpfu.CLIP_TO_IMAGE)
    #new_path = './processed/new-' + filename.replace("./", "")
    #pdb.gimp_file_save(image, drawable, new_path, 'Saved image')
    #pdb.gimp_image_delete(image);

def run(filename):

    #gimp.progress_init("Doing stuff to ...")

    start = time.time()

    add_borda(filename)

    end = time.time()
    print("Finished, total processing time: %.2f seconds" % (end - start))

#args = [(PF_STRING, 'file', 'GlobPattern', '*.*')]
#register('ivan-flip', '', '', '', '', '', '', '', args, [], run)
