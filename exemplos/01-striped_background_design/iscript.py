#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, glob, sys, time
from math import *
import gimpfu # access constantes
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

def template_1 (width,
                height,
                texture_file_path,
                texture_new_width,
                s_height,
                s_step1):

    WHITE      = (255, 255,  255)
    COLOR_ONE  = (198,  63,   86)
    COLOR_TWO  = (114,  34,   85)
    COLOR_THREE= (230,  181, 198)
    COLOR_FOUR = (212,  137, 164)
    COLOR_FIVE = (205,  184, 217)
    COLOR_SIX  = (181,  142, 206)
    BLACK      = (  0,   0,    0)

    GY1 = float(height)*382/1000   # golden rules ...
    GY2 = float(height)*1000/1618  # golden rules ...
    GX1 = float(width)*382/1000    # golden rules ...
    GX2 = float(width)*1000/1618   # golden rules ...

    XM  = float(width)/2
    YM  = float(height)/2

    # configura a paleta de cores
    pdb.gimp_context_set_background(BLACK)
    pdb.gimp_context_set_foreground(COLOR_ONE)

    # crio uma imagem
    image=pdb.gimp_image_new(width, height, gimpfu.RGB)

    # set resolution
    pdb.gimp_image_set_resolution(image, 300, 300)

    # DEBUG
    # desabilitar undo
    #pdb.gimp_image_undo_disable(image)

    # cria uma camada de nome `layer1'
    layer1 = pdb.gimp_layer_new(image, width, height, gimpfu.RGB_IMAGE, "layer1", 100, gimpfu.NORMAL_MODE)

    # adiciono alpha, para poder recortar futuramente
    pdb.gimp_layer_add_alpha(layer1)

    # junto a camada a imagem
    pdb.gimp_image_add_layer(image, layer1, 0)

    # pinto a camada layer1 com a cor do plano da frente
    pdb.gimp_drawable_fill(layer1, gimpfu.FOREGROUND_FILL)

    # recupera cores da paleta
    pdb.gimp_context_set_background(WHITE)
    pdb.gimp_context_set_foreground(COLOR_TWO)

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

    hwidth  = 0
    hspace  = 80
    hoffset = 0
    hcolor  = COLOR_TWO
    hopacity= 255

    vwidth   = 40
    vspace   = 80
    voffset  = 0
    vcolor   = COLOR_TWO
    vopacity = 255

    iwidth   = 0
    ispace   = 2
    ioffset  = 6
    icolor   = COLOR_TWO
    iopacity = 255

    pdb.plug_in_grid(image, layer1, hwidth, hspace, hoffset, hcolor, hopacity, vwidth, vspace, voffset, vcolor, vopacity, iwidth, ispace, ioffset, icolor, iopacity)

    filename = texture_file_path
    layer2 = pdb.gimp_file_load_layer(image, filename)

    print ("Load file: %s" %filename)
    print ("Image Resolution: w=%d,h=%d" %(layer2.width, layer2.height))

    #1443
    layer2_aspect = float(layer2.width) / float(layer2.height)
    layer2_new_width  =  float(texture_new_width)
    layer2_new_height =  layer2_new_width/layer2_aspect

    print ("New image Resolution: w=%d,h=%d" %(layer2_new_width, layer2_new_height))

    pdb.gimp_image_add_layer(image, layer2, 0)
    pdb.gimp_layer_resize(layer2, layer2_new_width, layer2_new_height, 0, 0)

    pdb.gimp_desaturate_full(layer2,0)
    #pdb.gimp_desaturate_full(layer2,1)
    #pdb.gimp_desaturate_full(layer2,2)

    # The new layer combination mode
    # ##############################
    #
    # NORMAL-MODE                      (0),
    # DISSOLVE-MODE                    (1),
    # BEHIND-MODE                      (2),
    # MULTIPLY-MODE                    (3),
    # SCREEN-MODE                      (4),
    # OVERLAY-MODE                     (5),
    # DIFFERENCE-MODE                  (6),
    # ADDITION-MODE                    (7),
    # SUBTRACT-MODE                    (8),
    # DARKEN-ONLY-MODE                 (9),
    # LIGHTEN-ONLY-MODE                (10),
    # HUE-MODE                         (11),
    # SATURATION-MODE                  (12),
    # COLOR-MODE                       (13),
    # VALUE-MODE                       (14),
    # DIVIDE-MODE                      (15),
    # DODGE-MODE                       (16),
    # BURN-MODE                        (17),
    # HARDLIGHT-MODE                   (18),
    # SOFTLIGHT-MODE                   (19),
    # GRAIN-EXTRACT-MODE               (20),
    # GRAIN-MERGE-MODE                 (21),
    # COLOR-ERASE-MODE                 (22),
    # ERASE-MODE                       (23),
    # REPLACE-MODE                     (24),
    # ANTI-ERASE-MODE                  (25)

    pdb.gimp_layer_set_mode(layer2, gimpfu.SOFTLIGHT_MODE)
    pdb.gimp_layer_set_opacity(layer2, 70)

    # crio a camada layer3 transparente
    layer3 = pdb.gimp_layer_new(image, width, height, gimpfu.RGBA_IMAGE, "layer3", 100, gimpfu.NORMAL_MODE)

    # adiciono alpha, para poder recortar futuramente
    pdb.gimp_layer_add_alpha(layer3)

    # adiciono layer3 na imagem
    pdb.gimp_image_add_layer(image, layer3, 0)

    # inicio de seleção
    pdb.gimp_selection_none (image)

    # Cria uma seleção em formato de retângulo
    # mantendo uma sombra de 10 pixels de cada lado
    X = 0
    Y = GY2  # golden rules ...
    s_width  = width
    pdb.gimp_rect_select (image, X, Y, s_width, s_height, 0, 0, 0)

    # configura a paleta de cores
    pdb.gimp_context_set_background(BLACK)
    pdb.gimp_context_set_foreground(WHITE)

    # pinto com o baldinho a camada selecionada em layer3
    #pdb.gimp_bucket_fill(layer3, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
    pdb.gimp_bucket_fill(layer3, gimpfu.BG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)

    # Aplicando Blur para dar sombra
    # 1 RLE

    # limpo a seleção para usar o blur
    radius     = 15
    horizontal = 22.0
    vertical   = 22.0
    pdb.gimp_selection_none (image)
    pdb.plug_in_gauss_rle(image, layer3, radius, horizontal, vertical)

    pdb.gimp_layer_set_mode(layer3, gimpfu.SOFTLIGHT_MODE)
    pdb.gimp_layer_set_opacity(layer3, 60)

    # crio a camada layer4 transparente
    layer4 = pdb.gimp_layer_new(image, width, height, gimpfu.RGBA_IMAGE, "layer4", 100, gimpfu.NORMAL_MODE)

    # adiciono alpha, para poder recortar futuramente
    pdb.gimp_layer_add_alpha(layer4)

    # adiciono layer4 na imagem
    pdb.gimp_image_add_layer(image, layer4, 0)

    # configura a paleta de cores
    pdb.gimp_context_set_background(BLACK)
    pdb.gimp_context_set_foreground(COLOR_THREE)

    # pinto com o baldinho a camada selecionada em layer4
    pdb.gimp_bucket_fill(layer4, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
    #pdb.gimp_bucket_fill(layer4, gimpfu.BG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)

    # faço uma nova seleção na quarta camada ...
    # inicio de seleção
    pdb.gimp_selection_none (image)

    # Cria uma seleção em formato de retângulo
    X = 0
    Y = GY2 + int(s_step1)
    s_width  = width
    pdb.gimp_rect_select (image,
                          X, Y,
                          s_width,
                          s_height - 2*int(s_step1),
                          0, 0, 0)

    # configura a paleta de cores
    pdb.gimp_context_set_background(BLACK)
    pdb.gimp_context_set_foreground(COLOR_FOUR)

    # pinto com o baldinho a camada selecionada em layer4
    pdb.gimp_bucket_fill(layer4, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
    #pdb.gimp_bucket_fill(layer4, gimpfu.BG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)

    # recupera cores da paleta
    pdb.gimp_context_set_background(WHITE)
    pdb.gimp_context_set_foreground(BLACK)

    # crio a camada layer5 transparente
    layer5 = pdb.gimp_layer_new(image, width, height, gimpfu.RGBA_IMAGE, "layer5", 100, gimpfu.NORMAL_MODE)

    # adiciono alpha, para poder recortar futuramente
    pdb.gimp_layer_add_alpha(layer5)

    # adiciono layer5 na imagem
    pdb.gimp_image_add_layer(image, layer5, 0)

    blend_mode     = gimpfu.FG_BG_RGB_MODE
    paint_mode     = gimpfu.NORMAL_MODE
    gradient_type  = gimpfu.GRADIENT_LINEAR
    opacity        = 100
    offset         = 0
    repeat         = gimpfu.REPEAT_NONE
    reverse        = FALSE
    supersample    = TRUE
    max_depth      = 2     # 1 à 9
    threshold      = 0.2
    dither         = TRUE

    x1             = XM
    y1             = GY2 + int(s_step1) + s_height - 2*int(s_step1)

    x2             = XM
    y2             = GY2 + int(s_step1)

    print ("A(%d,%d)" %(x1, y1))
    print ("B(%d,%d)" %(x2, y2))

    pdb.gimp_edit_blend(layer5, blend_mode, paint_mode, gradient_type, opacity, offset, repeat, reverse, supersample, max_depth, threshold, dither, x1, y1, x2, y2)

    # The new layer combination mode
    # ##############################
    #
    # NORMAL-MODE                      (0),
    # DISSOLVE-MODE                    (1),
    # BEHIND-MODE                      (2),
    # MULTIPLY-MODE                    (3),
    # SCREEN-MODE                      (4),
    # OVERLAY-MODE                     (5),
    # DIFFERENCE-MODE                  (6),
    # ADDITION-MODE                    (7),
    # SUBTRACT-MODE                    (8),
    # DARKEN-ONLY-MODE                 (9),
    # LIGHTEN-ONLY-MODE                (10),
    # HUE-MODE                         (11),
    # SATURATION-MODE                  (12),
    # COLOR-MODE                       (13),
    # VALUE-MODE                       (14),
    # DIVIDE-MODE                      (15),
    # DODGE-MODE                       (16),
    # BURN-MODE                        (17),
    # HARDLIGHT-MODE                   (18),
    # SOFTLIGHT-MODE                   (19),
    # GRAIN-EXTRACT-MODE               (20),
    # GRAIN-MERGE-MODE                 (21),
    # COLOR-ERASE-MODE                 (22),
    # ERASE-MODE                       (23),
    # REPLACE-MODE                     (24),
    # ANTI-ERASE-MODE                  (25)

    pdb.gimp_layer_set_mode(layer5, gimpfu.SOFTLIGHT_MODE)
    pdb.gimp_layer_set_opacity(layer5, 30)

    # recupera cores da paleta
    pdb.gimp_context_set_background(WHITE)
    pdb.gimp_context_set_foreground(BLACK)

    # GRID
    # ####

    hwidth  = 1
    hspace  = 4
    hoffset = 0
    hcolor  = WHITE
    hopacity= 255

    vwidth   = 0
    vspace   = 4
    voffset  = 0
    vcolor   = WHITE
    vopacity = 255

    iwidth   = 0
    ispace   = 2
    ioffset  = 6
    icolor   = COLOR_TWO
    iopacity = 255

    #drawable = pdb.gimp_image_merge_visible_layers(image, gimpfu.CLIP_TO_IMAGE)
    pdb.plug_in_grid(image, layer5, hwidth, hspace, hoffset, hcolor, hopacity, vwidth, vspace, voffset, vcolor, vopacity, iwidth, ispace, ioffset, icolor, iopacity)

    # remove seleção
    pdb.gimp_selection_none (image)

    pdb.gimp_layer_set_mode(layer5, gimpfu.SOFTLIGHT_MODE)
    pdb.gimp_layer_set_opacity(layer5, 38.6)

    # crio a camada layer6 transparente
    layer6 = pdb.gimp_layer_new(image, width, height, gimpfu.RGBA_IMAGE, "layer6", 100, gimpfu.NORMAL_MODE)

    # adiciono alpha, para poder recortar futuramente
    pdb.gimp_layer_add_alpha(layer6)

    # adiciono layer6 na imagem
    pdb.gimp_image_add_layer(image, layer6, 0)

    raio = (GX2-GX1)/2

    X  = GX1 *382/1000   # golden rules ...
#   X = GX1*1000/1618   # golden rules ...
    Y  =YM
    # recupera cores da paleta
    pdb.gimp_context_set_background(COLOR_FOUR)
    pdb.gimp_context_set_foreground(COLOR_FOUR)
    draw_circle(image, layer6, X, Y, raio)


    # crio a camada layer7 transparente
    layer7 = pdb.gimp_layer_new(image, width, height, gimpfu.RGBA_IMAGE, "layer7", 100, gimpfu.NORMAL_MODE)

    # adiciono alpha, para poder recortar futuramente
    pdb.gimp_layer_add_alpha(layer7)

    # adiciono layer7 na imagem
    pdb.gimp_image_add_layer(image, layer7, 0)

    # recupera cores da paleta
    pdb.gimp_context_set_background(WHITE)
    pdb.gimp_context_set_foreground(COLOR_FIVE)

    # pinto com o baldinho a camada selecionada em layer7
    pdb.gimp_bucket_fill(layer7, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
#   pdb.gimp_bucket_fill(layer7, gimpfu.BG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)

    # crio a camada layer8 transparente
    layer8 = pdb.gimp_layer_new(image, width, height, gimpfu.RGBA_IMAGE, "layer8", 100, gimpfu.NORMAL_MODE)

    # adiciono alpha, para poder recortar futuramente
    pdb.gimp_layer_add_alpha(layer8)

    # adiciono layer8 na imagem
    pdb.gimp_image_add_layer(image, layer8, 0)

    # remove seleção
    pdb.gimp_selection_none (image)

    DIAMETRO = (GX2-GX1)

    X  = GX1 *382/1000   # golden rules ...
#   X = GX1*1000/1618   # golden rules ...
    Y  =YM
#	pdb.gimp_ellipse_select(img, x_top_left, y_top_left, size, size, CHANNEL_OP_ADD, False, 0, 0)
    pdb.gimp_ellipse_select(image, X, Y, DIAMETRO-50, DIAMETRO-50,
                         gimpfu.CHANNEL_OP_REPLACE, True, False, 0)

    # recupera cores da paleta
    pdb.gimp_context_set_background(WHITE)
    pdb.gimp_context_set_foreground(COLOR_SIX)

    # pinto com o baldinho a camada selecionada em layer8
    pdb.gimp_bucket_fill(layer8, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
#   pdb.gimp_bucket_fill(layer8, gimpfu.BG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)

    # remove seleção
    pdb.gimp_selection_none (image)

    # DEBUG
    display = pdb.gimp_display_new(image)

def run(width, height, texture_file_path, texture_new_width):

    #gimp.progress_init("Doing stuff to ...")

    #sY       = int(57.25*float(height)/100)
    #s_height = 83
    s_step1  =  8
    s_height = (float(height) - float(height)*1000/1618)*1000/1618 - s_step1

    print ("s_height          = %s\n"
           "s_step1           = %s\n" %(s_height, s_step1))

    print ("width             = %s\n"
           "height            = %s\n"
           "texture_file_path = %s\n"
           "texture_new_width = %s\n" %(width, height, texture_file_path, texture_new_width))

    start = time.time()

    template_1(width,
               height,
               texture_file_path,
               texture_new_width,
               s_height,
               s_step1)

    end = time.time()
    print("Finished, total processing time: %.2f seconds" % (end - start))

