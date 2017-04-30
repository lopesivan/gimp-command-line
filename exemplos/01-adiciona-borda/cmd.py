# -*- coding: utf-8 -*-

import os, sys, subprocess

gimp_args = ('/usr/bin/gimp',
    '-idf',
    '--batch-interpreter=python-fu-eval',
    '-b', "import sys; sys.path=['.']+sys.path;import script;script.run('./foto-1.png')",
    '-b', 'pdb.gimp_quit(True)')

environ = os.environ.copy()
environ['GIMP2_DIRECTORY'] = '/home/ivan/.gimp-2.8/'
p=subprocess.Popen(gimp_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=environ)

print p.communicate()[0]
print p.returncode


#rc = p.wait()
#rc:
#    logging.error(p.stdout.read())
