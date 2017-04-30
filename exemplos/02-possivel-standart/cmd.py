gimp_args = ('/usr/bin/gimp',
    '-i',
    '--batch-interpreter=python-fu-eval',
    '-b', code_as_string,
    '-b', 'from gimpfu import pdb; pdb.gimp_quit(True)')

environ = os.environ.copy()
environ['GIMP2_DIRECTORY'] = '/home/ivan/.gimp-2.8/'
p = subprocess.Popen(gimp_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=environ)
rc = p.wait()
if rc:
    logging.error(p.stdout.read())

#from subprocess import check_output
#cmd = '(python-flip RUN-NONINTERACTIVE "/tmp/test.jpg")'
#output = check_output(['/usr/bin/gimp', '-i', '-b', cmd, '-b', '(gimp-quit 0)'])
#print output

