images_input  = foto-1.png foto-2.png foto-3.png foto-4.png
images_output = $(addprefix new-, $(images_input))

all: run

all: $(TARGETS)

foto-1.png:
	convert -size 303x203 xc:red foto-1.png

foto-2.png:
	convert -size 303x203 xc:red foto-2.png

foto-3.png:
	convert -size 303x203 xc:red foto-3.png

foto-4.png:
	convert -size 303x203 xc:red foto-4.png

script.pyc: $(images_input)
	gimp -idf --batch-interpreter python-fu-eval -b "import sys; sys.path=['.']+sys.path;import script;script.run('.')" -b "pdb.gimp_quit(1)"

run: script.pyc

OUT = $(images_input) $(images_output)

clean:
	@rm -rf $(TARGETS) $(OUT) processed/ script.pyc
#EOF
