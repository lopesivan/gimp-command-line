#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gimpfu # access constantes
from gimpfu import *
import random


class Gimpdraw:
    WHITE = (255, 255, 255)
    BLACK = (  0, 0, 0  )

    COLOR_ONE = None
    COLOR_TWO = None
    COLOR_THREE = None
    COLOR_FOUR = None
    COLOR_FIVE = None
    COLOR_SIX = None
    COLOR_SEVEN = None

    STEP = None

    def __init__(self,
                 step,
                 color_one,
                 color_two,
                 color_three,
                 color_four,
                 color_five,
                 color_six,
                 color_seven
    ):
        self.COLOR_ONE = color_one
        self.COLOR_TWO = color_two
        self.COLOR_THREE = color_three
        self.COLOR_FOUR = color_four
        self.COLOR_FIVE = color_five
        self.COLOR_SIX = color_six
        self.COLOR_SEVEN = color_seven
        self.STEP = step


    def my_brush(self, name, radius, hardness):
        print('Defining brush %s:  %d px, %5.2f' % (name, radius, hardness))

        brush = pdb.gimp_brush_new(name)

        pdb.gimp_brush_set_shape(name, gimpfu.BRUSH_GENERATED_CIRCLE)
        pdb.gimp_brush_set_radius(name, radius)
        pdb.gimp_brush_set_hardness(name, hardness)
        pdb.gimp_brush_set_spikes(name, 2)
        pdb.gimp_brush_set_spacing(name, 4)

        return brush

    def my_brush2(self, img, num_points, thickness):
        name = "myBrush2"

        brush = pdb.gimp_brush_new(name)

        #image = self.new_image_gray(300,img.height, img.width)
        image = img

        pdb.gimp_context_set_dynamics("Random Color")
        pdb.gimp_context_set_foreground(self.BLACK)
        pdb.gimp_context_set_background(self.BLACK)
        pdb.gimp_context_set_opacity(100)

        index = 0
        size = 400
        array_lenght = num_points * 2
        ctrlPoints = []

        while (index < array_lenght-1):
            ctrlPoints.append(20 + random.randint(1, size - 40))
            index += 1

        layer = self.new_layer_gray(image, "Brush")

        pdb.gimp_context_set_brush(brush)
        pdb.gimp_paintbrush_default(layer, len(ctrlPoints), ctrlPoints)

        self.smooth_threshold(image, layer, thickness)

        pdb.gimp_brush_delete('myBrush2')


    def smooth_threshold(self, image, layer, threshold):
        pdb.gimp_image_undo_group_start(image)

        low_threshold = threshold
        high_threshold = 255
        pdb.gimp_threshold(layer, low_threshold, high_threshold)

        pdb.plug_in_gauss(image, layer, 4, 4, 1);
        pdb.gimp_levels(layer, gimpfu.HISTOGRAM_VALUE, 95, 160, 1.0, 0, 255)
        pdb.gimp_image_undo_group_end(image)

    def draw_circle(img, layer, x_center, y_center, radius):
        width = 2 # line width in pixels
        radius = radius + width / 2.
        x_top_left = x_center - radius
        y_top_left = y_center - radius

        pdb.gimp_ellipse_select(img, x_top_left, y_top_left, 2 * radius, 2 * radius, gimpfu.CHANNEL_OP_ADD, False, 0, 0)
        # when gimp stable relase suport defining stroke preferences this function
        # will looks nicer
        # pdb.gimp_edit_stroke(layer)
        # meanwhile..
        pdb.gimp_edit_bucket_fill(layer, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
        pdb.gimp_selection_none(img)
        radius = radius - width
        x_top_left = x_center - radius
        y_top_left = y_center - radius
        pdb.gimp_ellipse_select(img, x_top_left, y_top_left, 2 * radius, 2 * radius, gimpfu.CHANNEL_OP_ADD, False, 0, 0)
        pdb.gimp_edit_bucket_fill(layer, gimpfu.BG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)
        pdb.gimp_selection_none(img)

    def set_default_fg_bg(self):
        # configura a paleta de cores
        pdb.gimp_context_set_background(self.WHITE)
        pdb.gimp_context_set_foreground(self.BLACK)

    def set_fg_bg(self, fg_color, bg_color):
        pdb.gimp_context_set_foreground(fg_color)
        pdb.gimp_context_set_background(bg_color)

    def new_image(self, dpi, height, width):
        # crio uma imagem
        image = pdb.gimp_image_new(width, height, gimpfu.RGB)

        # set resolution
        pdb.gimp_image_set_resolution(image, dpi, dpi)

        return image

    def new_image_gray(self, dpi, height, width):
        # crio uma imagem
        image = pdb.gimp_image_new(width, height, gimpfu.GRAY)

        # set resolution
        pdb.gimp_image_set_resolution(image, dpi, dpi)

        return image

    def new_layer_color(self, image, layer_name, color):
        width = image.width
        height = image.height
        layer = pdb.gimp_layer_new(image, width, height, gimpfu.RGB_IMAGE, layer_name, 100, gimpfu.NORMAL_MODE)

        # adiciono alpha, para poder recortar futuramente
        pdb.gimp_layer_add_alpha(layer)

        # junto a camada a imagem
        pdb.gimp_image_add_layer(image, layer, 0)

        # altero a paleta adicionando uma color_one no FG
        self.set_fg_bg(self.COLOR_ONE, self.WHITE)

        # pinto a camada layer1 com a cor do plano da frente
        pdb.gimp_drawable_fill(layer, gimpfu.FOREGROUND_FILL)

        return layer

    def new_layer(self, image, layer_name):
        width = image.width
        height = image.height

        layer = pdb.gimp_layer_new(image, width, height, gimpfu.RGB_IMAGE, layer_name, 100, gimpfu.NORMAL_MODE)

        # adiciono alpha, para poder recortar futuramente
        pdb.gimp_layer_add_alpha(layer)

        # junto a camada a imagem
        pdb.gimp_image_add_layer(image, layer, 0)

        return layer

    def new_layer_gray(self, image, layer_name):
        width = image.width
        height = image.height

        layer = pdb.gimp_layer_new(image, width, height, gimpfu.GRAY_IMAGE, layer_name, 100, gimpfu.NORMAL_MODE)

        # adiciono alpha, para poder recortar futuramente
        pdb.gimp_layer_add_alpha(layer)

        # junto a camada a imagem
        pdb.gimp_image_add_layer(image, layer, 0)

        return layer

    def new_layer_transparent(self, image, layer_name):
        width = image.width
        height = image.height

        layer = pdb.gimp_layer_new(image, width, height, gimpfu.RGBA_IMAGE, layer_name, 100, gimpfu.NORMAL_MODE)

        # adiciono alpha, para poder recortar futuramente
        pdb.gimp_layer_add_alpha(layer)

        # junto a camada a imagem
        pdb.gimp_image_add_layer(image, layer, 0)

        return layer

    def layer_texture(self, image, filename):
        layer = pdb.gimp_file_load_layer(image, filename)

        print("Load file: %s" % filename)
        print("Image Resolution: w=%d,h=%d" % (layer.width, layer.height))

        #1443
        layer_aspect = float(layer.width) / float(layer.height)
        layer_new_width = float(image.width)
        layer_new_height = layer_new_width / layer_aspect

        print("New image Resolution: w=%d,h=%d" % (layer_new_width, layer_new_height))
        pdb.gimp_image_add_layer(image, layer, 0)

        dim_border = 0
        dim_border = 0
        pdb.gimp_layer_resize(layer, layer_new_width+(dim_border*2), layer_new_height+(dim_border*2), dim_border,dim_border)

        return layer

    def layer_texture2(self, image, filename):
        layer = pdb.gimp_file_load_layer(image, filename)

        print("Load file: %s" % filename)
        print("Image Resolution: w=%d,h=%d" % (layer.width, layer.height))

        #1443
        layer_aspect = float(layer.width) / float(layer.height)
        layer_new_width = float(image.width)
        layer_new_height = layer_new_width / layer_aspect

        print("New image Resolution: w=%d,h=%d" % (layer_new_width, layer_new_height))
        pdb.gimp_image_add_layer(image, layer, 0)

        local_origin = True
        pdb.gimp_layer_scale(layer, layer_new_width, layer_new_height, local_origin)

        return layer

    def layer_texture_resaze_transpose(self, image, filename, x0, y0, x1, y1 ):

        layer = pdb.gimp_file_load_layer(image, filename)

        print("Load file: %s" % filename)
        print("Image Resolution: w=%d,h=%d" % (layer.width, layer.height))

        pdb.gimp_image_add_layer(image, layer, 0)

        pdb.gimp_item_transform_scale(layer, x0, y0, x1, y1)

        return layer

    def circle_selection(self, image, layer, x_center, y_center, radius):
        x_top_left = x_center - radius
        y_top_left = y_center - radius

        pdb.gimp_selection_none(image)

        print("Point(%d,%d)" % (x_center, y_center))

        pdb.gimp_ellipse_select(image,
                                x_top_left,
                                y_top_left,
                                2 * radius, 2 * radius,
                                gimpfu.CHANNEL_OP_REPLACE, True, False, 0)

        # baldinho
        #pdb.gimp_edit_bucket_fill(layer, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)

    def circle_selection_fill(self, image, layer, x_center, y_center, radius, color):
        self.circle_selection(image, layer, x_center, y_center, radius)

        # configura a paleta de cores
        pdb.gimp_context_set_background(self.WHITE)
        pdb.gimp_context_set_foreground(color)

        # pinto com o baldinho a camada selecionada em layer
        pdb.gimp_bucket_fill(layer, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)

        pdb.gimp_selection_none(image)


    def rectangle_selection(self, image, X, Y, width, height):
        # inicio de seleção
        pdb.gimp_selection_none(image)

        print("Point(%d,%d)" % (X, Y))

        # Cria uma seleção em formato de retângulo
        pdb.gimp_rect_select(image, X, Y, width, height, 0, 0, 0)

    def rectangle_selection_fill(self, image, layer, X, Y, width, height, color):
        self.rectangle_selection(image, X, Y, width, height)

        # configura a paleta de cores
        pdb.gimp_context_set_background(self.WHITE)
        pdb.gimp_context_set_foreground(color)

        # pinto com o baldinho a camada selecionada em layer4
        pdb.gimp_bucket_fill(layer, gimpfu.FG_BUCKET_FILL, gimpfu.NORMAL_MODE, 100, 0, 0, 0, 0)

        pdb.gimp_selection_none(image)


    def set_softlight_opacity(self, layer, opacity):
        """
        The new layer combination mode
        ##############################

     NORMAL-MODE                      (0),
     DISSOLVE-MODE                    (1),
     BEHIND-MODE                      (2),
     MULTIPLY-MODE                    (3),
     SCREEN-MODE                      (4),
     OVERLAY-MODE                     (5),
     DIFFERENCE-MODE                  (6),
     ADDITION-MODE                    (7),
     SUBTRACT-MODE                    (8),
     DARKEN-ONLY-MODE                 (9),
     LIGHTEN-ONLY-MODE                (10),
     HUE-MODE                         (11),
     SATURATION-MODE                  (12),
     COLOR-MODE                       (13),
     VALUE-MODE                       (14),
     DIVIDE-MODE                      (15),
     DODGE-MODE                       (16),
     BURN-MODE                        (17),
     HARDLIGHT-MODE                   (18),
     SOFTLIGHT-MODE                   (19),
     GRAIN-EXTRACT-MODE               (20),
     GRAIN-MERGE-MODE                 (21),
     COLOR-ERASE-MODE                 (22),
     ERASE-MODE                       (23),
     REPLACE-MODE                     (24),
     ANTI-ERASE-MODE                  (25)
    """
        pdb.gimp_layer_set_mode(layer, gimpfu.SOFTLIGHT_MODE)
        pdb.gimp_layer_set_opacity(layer, opacity)


