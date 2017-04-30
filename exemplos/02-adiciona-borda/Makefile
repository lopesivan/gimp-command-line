images_input  = imagem.png
images_output = $(addprefix new-, $(images_input))

all: run

all: $(TARGETS)

imagem.png:
	convert -size 303x203 xc:red $@

deploy: clean run

new-imagem.png: pnggrad8rgb.png
	cat script.py |gimp -i --batch-interpreter python-fu-eval --batch - -b "import sys; sys.path=['.']+sys.path; import script;script.run('./pnggrad8rgb.png')" -b "pdb.gimp_quit(1)"

interativo:
	cat script.py |gimp --batch-interpreter python-fu-eval --batch - -b "import sys; sys.path=['.']+sys.path; import script;script.run('./pnggrad8rgb.png')"

run: new-imagem.png

OUT = $(images_input) $(images_output)

show:
	eog processed/new-pnggrad8rgb.png

clean:
	@rm -rf $(TARGETS) $(OUT) script.pyc
#EOF
