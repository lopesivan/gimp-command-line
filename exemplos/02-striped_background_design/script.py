#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, glob, sys, time
from math import *
import random
import gimpfu # access constantes
from gimpfu import *
from gimpdraw import Gimpdraw


def activity_one(draw, image, layer):
    # permitindo desenhar na imagem
    #drawable = pdb.gimp_image_merge_visible_layers(image, gimpfu.CLIP_TO_IMAGE)
    # GRID DEFAULT
    # #############
    #static Config grid_cfg =
    #{
    #  1, 16, 8, { 0.0, 0.0, 0.0, 1.0 },    /* horizontal   */
    #  1, 16, 8, { 0.0, 0.0, 0.0, 1.0 },    /* vertical     */
    #  0,  2, 6, { 0.0, 0.0, 0.0, 1.0 },    /* intersection */
    #};
    #hwidth  = 1
    #hspace  = 16
    #hoffset = 8
    #hcolor  = COLOR_TWO
    #hopacity= 255
    #
    #vwidth   = 1
    #vspace   = 16
    #voffset  = 8
    #vcolor   = COLOR_TWO
    #vopacity = 255
    #
    #iwidth   = 0
    #ispace   = 2
    #ioffset  = 6
    #icolor   = COLOR_TWO
    #iopacity = 255
    #
    #pdb.plug_in_grid(image, drawable, hwidth, hspace, hoffset, hcolor, hopacity, vwidth, vspace, voffset, vcolor, vopacity, iwidth, ispace, ioffset, icolor, iopacity)
    hwidth = 0
    hspace = 80
    hoffset = 0
    hcolor = draw.COLOR_TWO
    hopacity = 255
    vwidth = 40
    vspace = 80
    voffset = 0
    vcolor = draw.COLOR_TWO
    vopacity = 255
    iwidth = 0
    ispace = 2
    ioffset = 6
    icolor = draw.COLOR_TWO
    iopacity = 255
    pdb.plug_in_grid(image,
                     layer,
                     hwidth,
                     hspace,
                     hoffset,
                     hcolor,
                     hopacity,
                     vwidth,
                     vspace,
                     voffset,
                     vcolor,
                     vopacity,
                     iwidth,
                     ispace,
                     ioffset,
                     icolor,
                     iopacity)

# end def activity_one

def activity_two(draw, layer):
    # aplicando efeito em layer ...
    pdb.gimp_desaturate_full(layer, 0) # 0, 1, 2
    draw.set_softlight_opacity(layer, 70)

# end def activity_two

def shadown_1(draw, image, layer):
    radius = 15
    horizontal = 22.0
    vertical = 22.0

    pdb.gimp_selection_none(image)
    pdb.plug_in_gauss_rle(image, layer, radius, horizontal, vertical)

    # aplicando softlight e opacidade na camada layer3
    draw.set_softlight_opacity(layer, 60)

# end def shadown_1

def activity_three(draw, image, layer):
    GY1 = float(image.height) * 382 / 1000   # golden rules ...
    GY2 = float(image.height) * 1000 / 1618  # golden rules ...

    # Cria uma seleção em formato de retângulo
    X = 0
    #   Y = GY2 # golden rules ...
    Y = GY2 + draw.STEP
    s_width = image.width
    s_height = ( float(image.height) - GY2 ) * 1000 / 1618
    #s_height = (float(image.height) - float(image.height) * 1000 / 1618) * 1000 / 1618 + int(draw.STEP)

    draw.rectangle_selection_fill(image, layer, X, Y, s_width, s_height, draw.BLACK)

    shadown_1(draw, image, layer)

# end def activity_three

def activity_four(draw, image, layer):
    GY2 = float(image.height) * 1000 / 1618  # GY2 golden rules ...

    # Cria uma seleção em formato de retângulo
    X = 0
    Y = GY2
    s_width = image.width
    s_height = ( float(image.height) - GY2 ) * 1000 / 1618 \
               - draw.STEP

    draw.rectangle_selection_fill(image, layer, X, Y, s_width, s_height, draw.COLOR_THREE)

# end def activity_four

def activity_five(draw, image, layer):
    GY2 = float(image.height) * 1000 / 1618  # GY2 golden rules ...

    # Cria uma seleção em formato de retângulo e pinto com a cor tres
    X = 0
    Y = GY2 + int(draw.STEP)
    s_width = image.width
    s_height = ( float(image.height) - GY2 ) * 1000 / 1618 \
               - draw.STEP \
               - 2 * int(draw.STEP)

    draw.rectangle_selection_fill(image, layer, X, Y, s_width, s_height, draw.COLOR_FOUR)

# end def activity_five

def activity_six(draw, image, layer):
    GY2 = float(image.height) * 1000 / 1618  # GY2 golden rules ...

    # Cria uma seleção em formato de retângulo e pinto com a cor tres
    X = 0
    s_width = image.width

    Y = GY2 + int(draw.STEP)
    s_height = ( float(image.height) - GY2 ) * 1000 / 1618 \
               - draw.STEP \
               - 2 * int(draw.STEP)

    draw.rectangle_selection(image, X, Y, s_width, s_height)

    blend_mode = gimpfu.FG_BG_RGB_MODE
    paint_mode = gimpfu.NORMAL_MODE
    gradient_type = gimpfu.GRADIENT_LINEAR
    opacity = 100
    offset = 0
    repeat = gimpfu.REPEAT_NONE
    reverse = FALSE
    supersample = TRUE
    max_depth = 2     # 1 à 9
    threshold = 0.2
    dither = TRUE

    XM = float(image.width) / 2

    diff = s_height * 0.4
    # A
    (x1, y1) = (XM, GY2 + int(draw.STEP) + diff)

    # B
    (x2, y2) = (XM, GY2 + int(draw.STEP))

    print("A(%d,%d)" % (x1, y1))
    print("B(%d,%d)" % (x2, y2))

    draw.set_default_fg_bg()

    pdb.gimp_edit_blend(layer,
                        blend_mode,
                        paint_mode,
                        gradient_type,
                        opacity,
                        offset,
                        repeat,
                        reverse,
                        supersample,
                        max_depth,
                        threshold,
                        dither,
                        x1, y1, x2, y2)

    #   pdb.gimp_layer_set_mode(layer, gimpfu.SOFTLIGHT_MODE)
    #   pdb.gimp_layer_set_opacity(layer, 30)
    draw.set_softlight_opacity(layer, 30)

    # GRID
    # ####
    if (image.height <= 768):
        hwidth = 1
        hspace = 4
        hoffset = 0

        vwidth = 0
        vspace = 4
        voffset = 0

        iwidth = 0
        ispace = 2
        ioffset = 6
    else:
        hwidth = int(image.height / 266)
        hspace = 24
        hoffset = 8

        vwidth = 0
        vspace = 0
        voffset = 8

        iwidth = 0
        ispace = 2
        ioffset = 6

    hcolor = draw.WHITE
    vcolor = draw.WHITE
    icolor = draw.COLOR_TWO

    iopacity = 255
    vopacity = 255
    hopacity = 255

    #drawable = pdb.gimp_image_merge_visible_layers(image, gimpfu.CLIP_TO_IMAGE)
    pdb.plug_in_grid(image, layer, hwidth, hspace, hoffset, hcolor, hopacity, vwidth, vspace, voffset, vcolor, vopacity,
                     iwidth, ispace, ioffset, icolor, iopacity)

    # remove seleção
    pdb.gimp_selection_none(image)

    draw.set_softlight_opacity(layer, 38.6)

# end def activity_six

def activity_seven(draw, image, layer):
    GY2 = float(image.height) * 1000 / 1618  # GY2 golden rules ...

    GX1 = float(image.width) * 382 / 1000    # golden rules ...
    GX2 = float(image.width) * 1000 / 1618   # golden rules ...

    X = GX1 * 1000 / 1618

    s_height = ( float(image.height) - GY2 ) * 1000 / 1618 \
               - draw.STEP \
               - 2 * int(draw.STEP)

    Y = GY2 + int(draw.STEP) + s_height / 2

    radius = (GX2 - GX1) / 2

    draw.circle_selection_fill(image, layer, X, Y, radius, draw.BLACK)

# end def activity_seven

def activity_eight(draw, image, layer):
    GY2 = float(image.height) * 1000 / 1618  # GY2 golden rules ...

    GX1 = float(image.width) * 382 / 1000    # golden rules ...
    GX2 = float(image.width) * 1000 / 1618   # golden rules ...

    X = GX1 * 1000 / 1618

    s_height = ( float(image.height) - GY2 ) * 1000 / 1618 \
               - draw.STEP \
               - 2 * int(draw.STEP)

    Y = GY2 + int(draw.STEP) + s_height / 2

    radius = (GX2 - GX1) / 2

    draw.circle_selection_fill(image, layer, X, Y, radius, draw.COLOR_FIVE)

# end def activity_eight

def activity_nine(draw, image, layer):
    GY2 = float(image.height) * 1000 / 1618  # GY2 golden rules ...

    GX1 = float(image.width) * 382 / 1000    # golden rules ...
    GX2 = float(image.width) * 1000 / 1618   # golden rules ...

    X = GX1 * 1000 / 1618

    s_height = ( float(image.height) - GY2 ) * 1000 / 1618 \
               - draw.STEP \
               - 2 * int(draw.STEP)

    Y = GY2 + int(draw.STEP) + s_height / 2

    radius = (GX2 - GX1) / 2 - int(draw.STEP)

    draw.circle_selection_fill(image, layer, X, Y, radius, draw.COLOR_SIX)


def activity_ten(draw, image, layer):
    GY2 = float(image.height) * 1000 / 1618  # GY2 golden rules ...

    GX1 = float(image.width) * 382 / 1000    # golden rules ...
    GX2 = float(image.width) * 1000 / 1618   # golden rules ...

    X = GX1 * 1000 / 1618

    s_height = ( float(image.height) - GY2 ) * 1000 / 1618 \
               - draw.STEP \
               - 2 * int(draw.STEP)

    Y = GY2 + int(draw.STEP) + s_height / 2

    radius = (GX2 - GX1) / 2 - int(draw.STEP)

    draw.circle_selection(image, layer, X, Y, radius)

    draw.set_default_fg_bg()

    blend_mode = gimpfu.FG_BG_RGB_MODE
    paint_mode = gimpfu.NORMAL_MODE
    gradient_type = gimpfu.GRADIENT_LINEAR
    opacity = 100
    offset = 0
    repeat = gimpfu.REPEAT_NONE
    reverse = FALSE
    supersample = TRUE
    max_depth = 2     # 1 à 9
    threshold = 0.2
    dither = TRUE

    # A
    (x1, y1) = (X, Y + radius)

    # B
    (x2, y2) = (X, Y - radius)

    print("A(%d,%d)" % (x1, y1))
    print("B(%d,%d)" % (x2, y2))

    draw.set_default_fg_bg()

    pdb.gimp_edit_blend(layer,
                        blend_mode,
                        paint_mode,
                        gradient_type,
                        opacity,
                        offset,
                        repeat,
                        reverse,
                        supersample,
                        max_depth,
                        threshold,
                        dither,
                        x1, y1, x2, y2)

    #   pdb.gimp_layer_set_mode(layer, gimpfu.SOFTLIGHT_MODE)
    #   pdb.gimp_layer_set_opacity(layer, 30)
    draw.set_softlight_opacity(layer, 32.7)

    # remove seleção
    pdb.gimp_selection_none(image)


def activity_eleven(draw, image, layer):

    draw.set_default_fg_bg()

    pdb.gimp_desaturate_full(layer, 0) # 0, 1, 2
    draw.set_softlight_opacity(layer, 70)

    #draw.set_softlight_opacity(layer, 38.6)
    #pdb.gimp_selection_none(image)


def Main(width,
         height,
         texture_file_path,
         moon_texture_file_path,
         my_message_1,
         debug):
    """
    Main
    :param width:
    :param height:
    :param texture_file_path:
    :param texture_new_width:
    :param debug:
    """

    GY1 = float(height) * 382 / 1000   # golden rules ...
    GY2 = float(height) * 1000 / 1618  # golden rules ...
    GX1 = float(width) * 382 / 1000    # golden rules ...
    GX2 = float(width) * 1000 / 1618   # golden rules ...

    XM = float(width) / 2
    YM = float(height) / 2

    d = Gimpdraw(
        8,
        (198,  63,  86),
        (114,  34,  85),
        (230, 181, 198),
        (212, 137, 164),
        (205, 184, 217),
        (181, 142, 206),
        (224,  65, 145)
    )

    # seta o BACKGROUND E O FOREGROUND com as cores defaults
    d.set_default_fg_bg()

    dpi = 300
    image = d.new_image(dpi, height, width)

    # DEBUG
    # desabilitar undo
    if not debug:
        pdb.gimp_image_undo_disable(image)
        # end if

    # cria uma camada de nome `layer1'
    layer1 = d.new_layer_color(image,
                               "layer1",
                               d.COLOR_ONE)

    # Filtros e funções aplicadas a camada layer1
    activity_one(d, image, layer1)

    ##########
    # layer2 #
    ##########
    layer2 = d.layer_texture(image, texture_file_path)

    #x0, y0 = (0,0)
    #x1, y1 = (image.width, image.height)
    #layer2 = d.layer_texture_resaze_transpose(image, texture_file_path, x0, y0, x1, y1)

    # Filtros e funções aplicadas a camada layer2
    activity_two(d, layer2)

    ##########
    # layer3 #
    ##########
    layer3 = d.new_layer_transparent(image, "layer3")

    # Filtros e funções aplicadas a camada layer3
    activity_three(d, image, layer3)

    ##########
    # layer4 #
    ##########
    layer4 = d.new_layer_transparent(image, "layer4")

    # Filtros e funções aplicadas a camada layer4
    activity_four(d, image, layer4)

    ##########
    # layer5 #
    ##########
    layer5 = d.new_layer_transparent(image, "layer5")

    # Filtros e funções aplicadas a camada layer5
    activity_five(d, image, layer5)

    ##########
    # layer6 #
    ##########
    layer6 = d.new_layer_transparent(image, "layer6")

    # Filtros e funções aplicadas a camada layer6
    activity_six(d, image, layer6)

    ##########
    # layer7 #
    ##########
    layer7 = d.new_layer_transparent(image, "layer7")

    activity_seven(d, image, layer7)

    ##########
    # layer8 #
    ##########
    layer8 = d.new_layer_transparent(image, "layer8")

    activity_eight(d, image, layer8)

    ##########
    # layer9 #
    ##########
    layer9 = d.new_layer_transparent(image, "layer9")

    activity_nine(d, image, layer9)

    ###########
    # layer10 #
    ###########
    layer10 = d.new_layer_transparent(image, "layer10")

    activity_ten(d, image, layer10)

    ###########
    # layer11 #
    ###########
    GY2 = float(image.height) * 1000 / 1618  # GY2 golden rules ...

    GX1 = float(image.width) * 382 / 1000    # golden rules ...
    GX2 = float(image.width) * 1000 / 1618   # golden rules ...

    X = GX1 * 1000 / 1618

    s_height = ( float(image.height) - GY2 ) * 1000 / 1618 \
               - d.STEP \
               - 2 * int(d.STEP)

    Y = GY2 + int(d.STEP) + s_height / 2

    radius = (GX2 - GX1) / 2 - int(d.STEP)

    # load texture
    x0, y0 = (X-radius,Y-radius)
    x1, y1 = (X+radius,Y+radius)
    layer11 = d.layer_texture_resaze_transpose(image, moon_texture_file_path, x0, y0, x1, y1)
    activity_eleven(d, image, layer11)

    ###########
    # layer12 #
    ###########
    GY2 = float(image.height) * 1000 / 1618  # GY2 golden rules ...

    GX1 = float(image.width) * 382 / 1000    # golden rules ...
    GX2 = float(image.width) * 1000 / 1618   # golden rules ...

    X = GX1 * 1000 / 1618

    s_height = ( float(image.height) - GY2 ) * 1000 / 1618 \
               - d.STEP \
               - 2 * int(d.STEP)

    Y = GY2 + int(d.STEP) + s_height / 2

    radius = (GX2 - GX1) / 2 - int(d.STEP)


    layer12 = d.new_layer_transparent(image, "layer12")

    x, y      = (X,Y+radius/5)
    text      = my_message_1
    border    = 2    # >=-1
    antialias = True # (TRUE or FALSE)
    size      = radius
    size_type = gimpfu.PIXELS
    fontname  = "Segoe Print"

    text_layer = pdb.gimp_text_fontname(image, layer12, x, y, text, border, antialias, size, size_type, fontname)
    #pdb.gimp_image_add_layer(image, text_layer, 0)
    #activity_ten(d, image, layer10)

    #########################################################################
    #########################################################################
    #########################################################################

    if debug:
        print("DEBUG is TRUE")
        display = pdb.gimp_display_new(image)
    else:
        # permitindo desenhar na imagem
        drawable = pdb.gimp_image_merge_visible_layers(image, gimpfu.CLIP_TO_IMAGE)

        if not (os.path.exists('processed')):
            os.mkdir('processed')

        filename = "processed/new-image.png"
        pdb.file_png_save2(image, drawable, filename, filename, 0, 9, 0, 0, 0, 0, 0, 0, 0)
        # clean
        pdb.gimp_image_delete(image);
    # end if

# end def Main

def run(width, height, texture_file_path, moon_texture_file_path, my_message_1, debug):
    #gimp.progress_init("Doing stuff to ...")

    print("width                  = %s\n"
          "height                 = %s\n"
          "texture_file_path      = %s\n"
          "moon_texture_file_path = %s\n" % (width, height, texture_file_path, moon_texture_file_path)
    )

    start = time.time()

    Main(width,
         height,
         texture_file_path,
         moon_texture_file_path,
         my_message_1,
         debug)

    end = time.time()
    print("Finished, total processing time: %.2f seconds" % (end - start))

# end def run

