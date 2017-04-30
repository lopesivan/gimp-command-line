from subprocess import check_output
cmd = '(python-flip RUN-NONINTERACTIVE "/tmp/test.jpg")'
output = check_output(['/usr/bin/gimp', '-i', '-b', cmd, '-b', '(gimp-quit 0)'])
print output
