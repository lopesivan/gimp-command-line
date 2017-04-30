#!/usr/bin/env python

import os,glob,sys,time
from gimpfu import *

def run(directory):

	pdb.progress_init("Doing stuff to ...")

	start=time.time()
	print "Running on directory \"%s\"" % directory

	if not(os.path.exists('processed')):
		os.mkdir('processed')

	outfile = "unite.jpg"
	for file_xcf in glob.glob(os.path.join(directory, '*.xcf')):
		image    = pdb.gimp_file_load(file_xcf, file_xcf)
		drawable = pdb.gimp_image_merge_visible_layers (image, CLIP_TO_IMAGE)

		pdb.file_jpeg_save (image, drawable, outfile, outfile, .9, 0, 0, 0, " ", 0, 1, 0, 1);
		pdb.gimp_image_delete (image);

	end=time.time()
	print "Finished, total processing time: %.2f seconds" % (end-start)

