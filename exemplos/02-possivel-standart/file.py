from gimpfu import *

def run(input_filepath):
    image = pdb.gimp_file_load(input_filepath, input_filepath)
    image.disable_undo()
    layer = image.active_layer
    if not layer.is_rgb:
        pdb.gimp_image_convert_rgb(image)

    white = gimpcolor.RGB(1.0, 1.0, 1.0, 1.0)
    bg_color = pdb.gimp_image_pick_color(image, layer, 0, 0, True, False, 0)
    if bg_color == white:
        pdb.plug_in_colortoalpha(image, layer, bg_color)
        layer_copy = layer.copy()
        image.add_layer(layer_copy)
        image.merge_visible_layers(CLIP_TO_IMAGE)

    pdb.file_png_save_defaults(image, image.active_layer, input_filepath, input_filepath)

run('%(input_filepath)s')
