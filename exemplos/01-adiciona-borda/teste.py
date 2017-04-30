# -*- coding: utf-8 -*-

import os, glob, sys, time
import gimpfu # access constantes
from gimpfu import *

gettext.install("gimp20-python", gimp.locale_directory, unicode=True)

def add_borda(filename):

    print("Load file \"%s\"" % filename)

    if not (os.path.exists('processed')):
        os.mkdir('processed')

    if not (os.path.exists(filename)):
        sys.exit('ERROR: Database %s was not found!' % filename)

    image = pdb.gimp_file_load(filename, filename)

    width = image.width
    height = image.height

    print("imagem %s com dimenções iguais a %sx%s" % (filename, width, height))

    #image_aspect = float(width) / float(height)

    # Criando nova camada
    layer = pdb.gimp_layer_new(image,
                               width,
                               height,
                               gimpfu.RGB_IMAGE,
                               "base",
                               100,
                               gimpfu.NORMAL_MODE)

    # Incorpora camada na Imagem
    pdb.gimp_image_add_layer(image, layer, 0)

    # Cria uma seleção em formato de retângulo
    # mantendo uma sombra de 10 pixels de cada lado
    pdb.gimp_rect_select (image,
                          10, 10,
                          (width-2*10),
                          (height-2*10),
                          0,0,0)

    drawable = pdb.gimp_image_merge_visible_layers(image, gimpfu.CLIP_TO_IMAGE)

    new_path = './processed/new-' + filename.replace("./", "")
    pdb.gimp_file_save(image, drawable, new_path, 'Saved image')

    pdb.gimp_image_delete(image);

def teste():
    SIZE=240
    RADIO=24

    #create the image
    img=pdb.gimp_image_new(SIZE, SIZE, gimpfu.RGB)

    #add layer with 100% of opacity
    layer=pdb.gimp_layer_new(img, SIZE, SIZE, gimpfu.RGB_IMAGE, "base", 100, gimpfu.NORMAL_MODE)
    pdb.gimp_image_add_layer(img, layer, 0)

    #we need it with alpha channel
    pdb.gimp_layer_add_alpha(layer)

    #access its drawable
    drw = pdb.gimp_image_active_drawable(img)

    #set background to black, and foreground to white
    pdb.gimp_context_set_background((0,0,0))
    pdb.gimp_context_set_foreground((255, 255, 255))

    #fill the background - black
    pdb.gimp_drawable_fill(drw, gimpfu.BACKGROUND_FILL)

    #to set the brush, check first for available brushes using  pdb.gimp_brushes_get_list("")
    #Exanples of brush with width 3 is '1. Pixel', and with width 1, 'Pixel (1x1 square)'

    #set brush to simple pixel (width: 1)
    pdb.gimp_context_set_brush('Circle (01)')
    #current_brush = pdb.gimp_context_get_brush()
    #pdb.gimp_context_set_brush(current_brush)
    #pdb.gimp_context_set_brush('1. Pixel')
    #gimp.pdb.gimp_brushes_get_list("")

    #draw a square around the image
    ctrlPoints = [RADIO, RADIO, SIZE-RADIO, RADIO, SIZE-RADIO, SIZE-RADIO, RADIO, SIZE-RADIO, RADIO, RADIO]
    pdb.gimp_paintbrush_default(drw,len(ctrlPoints),ctrlPoints)

    #now we draw 9 transparent circles (3 rows x 3 columns)
    #a transparent circle means -with an alpha layer-, to select the area and cut it
    for x in (0, SIZE/2-RADIO, SIZE-2*RADIO):
        for y in (0, SIZE/2-RADIO, SIZE-2*RADIO):
            #next call was available on 2.6, not on 2.8
            #pdb.gimp_image_select_ellipse(img, gimpfu.CHANNEL_OP_REPLACE, x, y, RADIO*2, RADIO*2)
            pdb.gimp_ellipse_select(img, x, y, RADIO*2, RADIO*2, gimpfu.CHANNEL_OP_REPLACE, True, False, 0)
            pdb.gimp_edit_cut(drw)

    #remove any selection
    pdb.gimp_selection_none(img)

    #and display the image
    #display=pdb.gimp_display_new(img)
    pdb.file_png_save2(img, drw, "a.png", "a.png", 0, 9, 0, 0, 0, 0, 0, 0, 0)
    # clean
    pdb.gimp_image_delete(img);

def run(filename):

    gimp.progress_init("Doing stuff to ...")

    start = time.time()

    #add_borda(filename)
    teste()

    end = time.time()
    print("Finished, total processing time: %.2f seconds" % (end - start))

run('./testa.jpg')

#args = [(PF_STRING, 'file', 'GlobPattern', '*.*')]
#register('ivan-flip', '', '', '', '', '', '', '', args, [], run)
