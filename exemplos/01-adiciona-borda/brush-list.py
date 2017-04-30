#!/usr/bin/env python

import gimp
from gimpfu import *

import random
def make_strokes(w,h,b_w, b_h):
    i = 0.0
    stroke_list = []
    strokes = 0
    # start offset from the edge plus a bit of fudge
    # also, save some room for the one off "stamp"
    inc = b_w + b_w/2.0 + 10; 
    while i < 20:
        inc = inc + w/20.0
        stroke_list.append(inc)
        stroke_list.append((0.75*b_h)+random.random()*(b_h/2.0))
        strokes = strokes + 2;
        i = i + 1;
        # try not to spew off the edge
        if (inc + b_w) > (w - (b_w/2.0)):
            break

    print stroke_list, strokes
    return stroke_list, strokes

def make_single_stroke(w, h, b_w, b_h):
    x = (b_w/2.0)
    y = (b_h)
    stroke_list = [x,y]
    strokes = 2
    return stroke_list, strokes

def draw_brush_example(brush_name):
    """ draws a nice single brush stroke, and a random brush stroke to show the brush in use. Returns an Image"""
    gimp.pdb.gimp_context_set_brush(brush_name)
    brush_info = gimp.pdb.gimp_brush_get_info(brush_name)
    print brush_info

    pdb.gimp_context_set_opacity(100)
    w,h,mbpp,cbpp = brush_info
    # a little leeway so we can make a stroke
    image_w = (w*5)+10;
    image_h = h*2;
    img = gimp.Image(image_w, image_h, RGB)
    img.disable_undo()
    brush_layer = gimp.Layer(img, brush_name, image_w, image_h, RGBA_IMAGE, 100, NORMAL_MODE)
    img.add_layer(brush_layer, 0)

    # should make this right/black/configurable?
    pdb.gimp_edit_fill(brush_layer, BACKGROUND_FILL)

    # generate and paint a single brush stroke, and a random walk brush stroke
    stroke_list, strokes= make_strokes(image_w,image_h, w, h)
    pdb.gimp_paintbrush_default(brush_layer, strokes, stroke_list)

    stroke_list, strokes = make_single_stroke(w, h, w, h)
    pdb.gimp_paintbrush_default(brush_layer, strokes, stroke_list)
    
    img.enable_undo()
    return img, brush_layer, brush_name

# for us unix/linux folks...
def unlame_brush_name(brushname):
    # theres all sorts of better ways to do this, but this works for now for me
    brushname = brushname.replace(" ", "_")
    brushname = brushname.replace("!", "")
    brushname = brushname.replace("/", "")
    brushname = brushname.replace("?", "")
    brushname = brushname.replace("#", "")
    return brushname


def save_brush_as_png(img, drawable, brush_name):    
    path = "/tmp/test"
    filename = "%s/%s.png" % (path, unlame_brush_name(brush_name))
    pdb.file_png_save(img, drawable, filename, filename, 0,9,0,0,0,0,0)
    
def brush_list():
    img_list = []
    num_brushes, brush_list = gimp.pdb.gimp_brushes_get_list("")
    for brush_name in brush_list:
        print brush_name

        img, drawable, br_name = draw_brush_example(brush_name)
        img_list.append((img, drawable, br_name))

    html = ""
    for img, drawable, br_name in img_list:
        save_brush_as_png(img, drawable, br_name)
        html = html + """<img src="%s.png"><br>\n""" % unlame_brush_name(br_name)

    f = open("/tmp/test/index.html", "w+")
    f.write(html)
    f.close()
    return
        

register("python_fu_brush_list",
         "Draw a brush preview image",
         "Draw a brush previem image",
         "Adrian Likins",
         "Adrian Likins",
         "2005",
         "<Toolbox>/Xtns/Python-Fu/Brush List",
         "",
         [],
         [],
         brush_list)

main()
