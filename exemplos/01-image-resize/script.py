#!/usr/bin/env python

import os, glob, sys, time
from gimpfu import *

def image_resize(directory, width, height):

    print("Running on directory \"%s\"" % directory)

    if not (os.path.exists('processed')):
        os.mkdir('processed')

    for filename in glob.glob(os.path.join(directory, '*.png')):
        image = pdb.gimp_file_load(filename, filename)
        drawable = pdb.gimp_image_merge_visible_layers(image, CLIP_TO_IMAGE)

        print("width X height = %sx%s" % (image.width, image.height))

        pdb.gimp_image_scale(image, width, height)

        new_path = './processed/new-' + filename.replace("./", "");
        pdb.gimp_file_save(image, drawable, new_path, 'Saved image')

        pdb.gimp_image_delete(image);

def run(directory, width, height):

	gimp.progress_init("Doing stuff to ...")

	start = time.time()

	image_resize(directory, width, height)

	end = time.time()
	print("Finished, total processing time: %.2f seconds" % (end - start))

