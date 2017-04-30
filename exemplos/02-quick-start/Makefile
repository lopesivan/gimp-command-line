#images_input  =
images_output = unite.jpg

all: run

all: $(TARGETS)

unite.jpg: unite.xcf
	gimp -idf --batch-interpreter python-fu-eval -b "import sys; sys.path=['.']+sys.path;import script;script.run('.')" -b "pdb.gimp_quit(1)"

run: unite.jpg

OUT = $(images_input) $(images_output)

clean:
	@rm -rf $(TARGETS) $(OUT) processed/ script.pyc
#EOF
