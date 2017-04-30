import os, glob, sys, time
import gimpfu # access constantes
from gimpfu import *

    WHITE      = (255, 255,  255)
    COLOR_ONE  = (198,  63,   86)
    COLOR_TWO  = (114,  34,   85)
    COLOR_THREE= (230,  181, 198)
    COLOR_FOUR = (212,  137, 164)
    BLACK      = (  0,   0,    0)

    # configura a paleta de cores
    pdb.gimp_context_set_background(BLACK)
    pdb.gimp_context_set_foreground(COLOR_ONE)

    width  = 600
    height = 400

    # crio uma imagem
    image=pdb.gimp_image_new(width, height, gimpfu.RGB)

    # desabilitar undo
    pdb.gimp_image_undo_disable(image)

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

    # DEBUG
    display = pdb.gimp_display_new(image)

    # permitindo desenhar na imagem
    drawable = pdb.gimp_image_merge_visible_layers(image, gimpfu.CLIP_TO_IMAGE)

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

    pdb.plug_in_grid(image, drawable, hwidth, hspace, hoffset, hcolor, hopacity, vwidth, vspace, voffset, vcolor, vopacity, iwidth, ispace, ioffset, icolor, iopacity)

    filename = "/home/ivan/workspace/learning/learning-gimp/scripts/exemplos/python/01-striped_background_design/IMG_0001.jpg"
    layer2 = pdb.gimp_file_load_layer(image, filename)

    print("A imagem %s tem dimenções iguais a %sx%s" % (filename, layer2.width, layer2.height))
    #1443
    layer2_aspect = float(layer2.width) / float(layer2.height)
    layer2_new_width  =  1000
    layer2_new_height =  layer2_new_width/layer2_aspect

    print ("Image Resolution: w=%d,h=%d"%(layer2_new_width, layer2_new_height))
    print("DEBUG: r=%s,  dimenções iguais a %sx%s" % (layer2_aspect, layer2_new_width, layer2_new_height))

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
    Y = 229
    s_width  = width
    s_height = 83
    pdb.gimp_rect_select (image, X, Y, s_width, s_height, 0, 0,0)

    # configura a paleta de cores
    pdb.gimp_context_set_background(BLACK)
    pdb.gimp_context_set_foreground(WHITE)

    # pinto com o baldinho a camada selecionada em layer3
    #pdb.gimp_bucket_fill(layer3, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
    pdb.gimp_bucket_fill(layer3, gimpfu.BG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)


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
    # mantendo uma sombra de 10 pixels de cada lado
    X = 0
    Y = 237
    s_width  = width
    s_height = 67
    pdb.gimp_rect_select (image, X, Y, s_width, s_height, 0, 0,0)

    # configura a paleta de cores
    pdb.gimp_context_set_background(BLACK)
    pdb.gimp_context_set_foreground(COLOR_FOUR)

    # pinto com o baldinho a camada selecionada em layer4
    pdb.gimp_bucket_fill(layer4, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
    #pdb.gimp_bucket_fill(layer4, gimpfu.BG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)

    ###

    # recupera cores da paleta
    pdb.gimp_context_set_background(WHITE)
    pdb.gimp_context_set_foreground(BLACK)

    # crio a camada layer5 transparente
    layer5 = pdb.gimp_layer_new(image, width, height, gimpfu.RGBA_IMAGE, "layer5", 100, gimpfu.NORMAL_MODE)

    # adiciono alpha, para poder recortar futuramente
    pdb.gimp_layer_add_alpha(layer5)

    # adiciono layer4 na imagem
    pdb.gimp_image_add_layer(image, layer5, 0)
