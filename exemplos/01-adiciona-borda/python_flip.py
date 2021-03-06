# gimp -i -b '(python-flip RUN-NONINTERACTIVE "/tmp/test.jpg")' -b '(gimp-quit 0)'
#
#
#


from gimpfu import pdb, main, register, PF_STRING
from gimpenums import ORIENTATION_HORIZONTAL

def flip(file):
    image = pdb.gimp_file_load(file, file)
    drawable = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_image_flip(image, ORIENTATION_HORIZONTAL)
    pdb.gimp_file_save(image, drawable, file, file)
    pdb.gimp_context_set_brush('Circle (01)')
    pdb.gimp_brushes_get_list("")
    pdb.gimp_image_delete(image)

args = [(PF_STRING, 'file', 'GlobPattern', '*.*')]
register('python-flip3', '', '', '', '', '', '', '', args, [], flip)

main()
