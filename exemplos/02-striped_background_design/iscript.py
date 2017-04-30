#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, glob, sys, time
from math import *
import gimpfu # access constantes
from gimpfu import *
from gimpdraw import Gimpdraw

def Main(width,
         height,
         texture_file_path,
         texture_new_width,
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
        (198, 63, 86),
        (114, 34, 85),
        (230, 181, 198),
        (212, 137, 164),
        (205, 184, 217),
        (181, 142, 206)
    )

    # seta o BACKGROUND E O FOREGROUND com as cores defaults
    d.default_fg_bg()

    dpi=300
    image = d.new_image(dpi, height, width)


    # DEBUG
    # desabilitar undo
    if (not debug):
        pdb.gimp_image_undo_disable(image)

    # cria uma camada de nome `layer1'
    layer1 = d.new_layer_color(image,
                               width,
                               height,
                               "layer1",
                               d.COLOR_ONE)

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
    hcolor = d.COLOR_TWO
    hopacity = 255

    vwidth = 40
    vspace = 80
    voffset = 0
    vcolor = d.COLOR_TWO
    vopacity = 255

    iwidth = 0
    ispace = 2
    ioffset = 6
    icolor = d.COLOR_TWO
    iopacity = 255

    pdb.plug_in_grid(image,
                     layer1,
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


    # load texture
    layer2 = d.layer_texture(image, texture_file_path, texture_new_width)

    # aplicando efeito em layer2 ...
    pdb.gimp_desaturate_full(layer2, 0) # 0, 1, 2

    d.set_softlight_opacity(layer2, 70)


    # crio a camada layer3 transparente
    layer3 = d.new_layer_transparent(image, width, height, "layer3")

#
#    # Cria uma seleção em formato de retângulo
#    # mantendo uma sombra de 10 pixels de cada lado
#    X = 0
#    Y = GY2  # golden rules ...
#    s_width = width
#    s_height = (float(height) - float(height) * 1000 / 1618) * 1000 / 1618 - gimpdraw.step
#    gimpdraw.rectangle_selection(image, X, Y, s_width, s_height)
#
#    # configura a paleta de cores
#    gimpdraw.default_fg_bg()
#
#    # pinto com o baldinho a camada selecionada em layer3
#    #pdb.gimp_bucket_fill(layer3, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
#    pdb.gimp_bucket_fill(layer3,
#                         gimpfu.FG_BUCKET_FILL,
#                         gimpfu.NORMAL_MODE,
#                         100,
#                         0, 0, 0, 0)
#
#    # Aplicando Blur para dar sombra
#    # 1 RLE
#
#    radius = 15
#    horizontal = 22.0
#    vertical = 22.0
#    pdb.gimp_selection_none(image)
#    pdb.plug_in_gauss_rle(image, layer3, radius, horizontal, vertical)
#
#    gimpdraw.set_softlight_opacity(layer3, 60)
#
#    # crio a camada layer4 transparente
#    layer4 = gimpdraw.new_layer_transparent(image, width, height, "layer4")
#
#
#    # configura a paleta de cores
#    pdb.gimp_context_set_background(gimpdraw.BLACK)
#    pdb.gimp_context_set_foreground(gimpdraw.COLOR_THREE)
#
#    # pinto com o baldinho a camada selecionada em layer4
#    pdb.gimp_bucket_fill(layer4, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
#    #pdb.gimp_bucket_fill(layer4, gimpfu.BG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
#
#    # faço uma nova seleção na quarta camada ...
#    # inicio de seleção
#    pdb.gimp_selection_none(image)
#
#    # Cria uma seleção em formato de retângulo
#    X = 0
#    Y = GY2 + int(gimpdraw.step)
#    s_width = width
#    pdb.gimp_rect_select(image,
#                         X, Y,
#                         s_width,
#                         s_height - 2 * int(gimpdraw.step),
#                         0, 0, 0)
#
#    # configura a paleta de cores
#    pdb.gimp_context_set_background(gimpdraw.BLACK)
#    pdb.gimp_context_set_foreground(gimpdraw.COLOR_FOUR)
#
#    # pinto com o baldinho a camada selecionada em layer4
#    pdb.gimp_bucket_fill(layer4, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
#    #pdb.gimp_bucket_fill(layer4, gimpfu.BG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
#
#    # recupera cores da paleta
#    pdb.gimp_context_set_background(gimpdraw.WHITE)
#    pdb.gimp_context_set_foreground(gimpdraw.BLACK)
#
#    # crio a camada layer5 transparente
#    layer5 = pdb.gimp_layer_new(image, width, height, gimpfu.RGBA_IMAGE, "layer5", 100, gimpfu.NORMAL_MODE)
#
#    # adiciono alpha, para poder recortar futuramente
#    pdb.gimp_layer_add_alpha(layer5)
#
#    # adiciono layer5 na imagem
#    pdb.gimp_image_add_layer(image, layer5, 0)
#
#    blend_mode = gimpfu.FG_BG_RGB_MODE
#    paint_mode = gimpfu.NORMAL_MODE
#    gradient_type = gimpfu.GRADIENT_LINEAR
#    opacity = 100
#    offset = 0
#    repeat = gimpfu.REPEAT_NONE
#    reverse = FALSE
#    supersample = TRUE
#    max_depth = 2     # 1 à 9
#    threshold = 0.2
#    dither = TRUE
#
#    x1 = XM
#    y1 = GY2 + int(gimpdraw.step) + s_height - 2 * int(gimpdraw.step)
#
#    x2 = XM
#    y2 = GY2 + int(gimpdraw.step)
#
#    print("A(%d,%d)" % (x1, y1))
#    print("B(%d,%d)" % (x2, y2))
#
#    pdb.gimp_edit_blend(layer5, blend_mode, paint_mode, gradient_type, opacity, offset, repeat, reverse, supersample,
#                        max_depth, threshold, dither, x1, y1, x2, y2)
#
#    # The new layer combination mode
#    # ##############################
#    #
#    # NORMAL-MODE                      (0),
#    # DISSOLVE-MODE                    (1),
#    # BEHIND-MODE                      (2),
#    # MULTIPLY-MODE                    (3),
#    # SCREEN-MODE                      (4),
#    # OVERLAY-MODE                     (5),
#    # DIFFERENCE-MODE                  (6),
#    # ADDITION-MODE                    (7),
#    # SUBTRACT-MODE                    (8),
#    # DARKEN-ONLY-MODE                 (9),
#    # LIGHTEN-ONLY-MODE                (10),
#    # HUE-MODE                         (11),
#    # SATURATION-MODE                  (12),
#    # COLOR-MODE                       (13),
#    # VALUE-MODE                       (14),
#    # DIVIDE-MODE                      (15),
#    # DODGE-MODE                       (16),
#    # BURN-MODE                        (17),
#    # HARDLIGHT-MODE                   (18),
#    # SOFTLIGHT-MODE                   (19),
#    # GRAIN-EXTRACT-MODE               (20),
#    # GRAIN-MERGE-MODE                 (21),
#    # COLOR-ERASE-MODE                 (22),
#    # ERASE-MODE                       (23),
#    # REPLACE-MODE                     (24),
#    # ANTI-ERASE-MODE                  (25)
#
#    pdb.gimp_layer_set_mode(layer5, gimpfu.SOFTLIGHT_MODE)
#    pdb.gimp_layer_set_opacity(layer5, 30)
#
#    # recupera cores da paleta
#    pdb.gimp_context_set_background(gimpdraw.WHITE)
#    pdb.gimp_context_set_foreground(gimpdraw.BLACK)
#
#    # GRID
#    # ####
#
#    hwidth = 1
#    hspace = 4
#    hoffset = 0
#    hcolor = WHITE
#    hopacity = 255
#
#    vwidth = 0
#    vspace = 4
#    voffset = 0
#    vcolor = WHITE
#    vopacity = 255
#
#    iwidth = 0
#    ispace = 2
#    ioffset = 6
#    icolor = COLOR_TWO
#    iopacity = 255
#
#    #drawable = pdb.gimp_image_merge_visible_layers(image, gimpfu.CLIP_TO_IMAGE)
#    pdb.plug_in_grid(image, layer5, hwidth, hspace, hoffset, hcolor, hopacity, vwidth, vspace, voffset, vcolor,
#                     vopacity, iwidth, ispace, ioffset, icolor, iopacity)
#
#    # remove seleção
#    pdb.gimp_selection_none(image)
#
#    pdb.gimp_layer_set_mode(layer5, gimpfu.SOFTLIGHT_MODE)
#    pdb.gimp_layer_set_opacity(layer5, 38.6)
#
#    # crio a camada layer6 transparente
#    layer6 = pdb.gimp_layer_new(image, width, height, gimpfu.RGBA_IMAGE, "layer6", 100, gimpfu.NORMAL_MODE)
#
#    # adiciono alpha, para poder recortar futuramente
#    pdb.gimp_layer_add_alpha(layer6)
#
#    # adiciono layer6 na imagem
#    pdb.gimp_image_add_layer(image, layer6, 0)
#
#    raio = (GX2 - GX1) / 2
#
#    X = GX1 * 382 / 1000   # golden rules ...
#    #   X = GX1*1000/1618   # golden rules ...
#    Y = YM
#    # recupera cores da paleta
#    pdb.gimp_context_set_background(COLOR_FOUR)
#    pdb.gimp_context_set_foreground(COLOR_FOUR)
#    gimpdraw.draw_circle(image, layer6, X, Y, raio)
#
#    # crio a camada layer7 transparente
#    layer7 = pdb.gimp_layer_new(image, width, height, gimpfu.RGBA_IMAGE, "layer7", 100, gimpfu.NORMAL_MODE)
#
#    # adiciono alpha, para poder recortar futuramente
#    pdb.gimp_layer_add_alpha(layer7)
#
#    # adiciono layer7 na imagem
#    pdb.gimp_image_add_layer(image, layer7, 0)
#
#    # recupera cores da paleta
#    pdb.gimp_context_set_background(WHITE)
#    pdb.gimp_context_set_foreground(COLOR_FIVE)
#
#    # pinto com o baldinho a camada selecionada em layer7
#    pdb.gimp_bucket_fill(layer7, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
#    #   pdb.gimp_bucket_fill(layer7, gimpfu.BG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
#
#    # crio a camada layer8 transparente
#    layer8 = pdb.gimp_layer_new(image, width, height, gimpfu.RGBA_IMAGE, "layer8", 100, gimpfu.NORMAL_MODE)
#
#    # adiciono alpha, para poder recortar futuramente
#    pdb.gimp_layer_add_alpha(layer8)
#
#    # adiciono layer8 na imagem
#    pdb.gimp_image_add_layer(image, layer8, 0)
#
#    # remove seleção
#    pdb.gimp_selection_none(image)
#
#    DIAMETRO = (GX2 - GX1)
#
#    X = GX1 * 382 / 1000   # golden rules ...
#    #   X = GX1*1000/1618   # golden rules ...
#    Y = YM
#    #	pdb.gimp_ellipse_select(img, x_top_left, y_top_left, size, size, CHANNEL_OP_ADD, False, 0, 0)
#    pdb.gimp_ellipse_select(image, X, Y, DIAMETRO - 50, DIAMETRO - 50,
#                            gimpfu.CHANNEL_OP_REPLACE, True, False, 0)
#
#    # recupera cores da paleta
#    pdb.gimp_context_set_background(WHITE)
#    pdb.gimp_context_set_foreground(COLOR_SIX)
#
#    # pinto com o baldinho a camada selecionada em layer8
#    pdb.gimp_bucket_fill(layer8, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
#    #   pdb.gimp_bucket_fill(layer8, gimpfu.BG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
#
#    # remove seleção
#    pdb.gimp_selection_none(image)
#
    if debug:
        print("DEBUG is TRUE")
        display = pdb.gimp_display_new(image)

def run(width, height, texture_file_path, texture_new_width, debug):

    #gimp.progress_init("Doing stuff to ...")

    print("width             = %s\n"
          "height            = %s\n"
          "texture_file_path = %s\n"
          "texture_new_width = %s\n" % (width, height, texture_file_path, texture_new_width))

    start = time.time()


    Main(width,
         height,
         texture_file_path,
         texture_new_width,
         debug)

    end = time.time()
    print("Finished, total processing time: %.2f seconds" % (end - start))

