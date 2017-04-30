#!/usr/bin/env python

import os,glob,sys,time
from gimpfu import *


def convert_xcf_to_jpg(input, output ):

    print("Read file \"%s\"" % input)

    if not (os.path.exists('processed')):
        os.mkdir('./processed')

    outfile = output;


    image = pdb.gimp_file_load(input, input)
    drawable = pdb.gimp_image_merge_visible_layers(image, CLIP_TO_IMAGE)

    pdb.file_jpeg_save(image, drawable, "processed/"+outfile, outfile, .9, 0, 0, 0, " ", 0, 1, 0, 1)
    pdb.gimp_image_delete(image)


def run(input, output):

    gimp.progress_init("Doing stuff to ...")

    start=time.time()

    convert_xcf_to_jpg(input, output)

    end=time.time()
    print("Finished, total processing time: %.2f seconds" % (end - start))



