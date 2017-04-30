#!/usr/bin/env python

import os,glob,sys,time
from gimpfu import *

def run(directory):

	gimp.progress_init("Doing stuff to ...")

	start=time.time()
	print "Running on directory \"%s\"" % directory

	if not(os.path.exists('processed')):
		os.mkdir('processed')

	for img in glob.glob(os.path.join(directory, '*.png')):
		image = pdb.gimp_file_load(img, img)
		print img, "width =", image.width
		print img, "height=", image.height

	end=time.time()
	print "Finished, total processing time: %.2f seconds" % (end-start)

