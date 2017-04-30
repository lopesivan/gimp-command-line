#images_input  =
#images_output = $(addprefix new-, $(images_input))

SCRIPT        = script.py
GIMP          =/usr/bin/gimp
GIMP_OPT      = --batch-interpreter python-fu-eval --batch -
GIMP_QUIT     = -b "pdb.gimp_quit(1)"

TEXTURE_FILE_PATH = ${PWD}/IMG_0001.jpg

# HD1080
#width             =  1920
#height            =  1080

#HD720
#width             =  1280
#height            =  768

width             =  600
height            =  400

##############################################################################
TEXTURE_NEW_WIDTH = $(width)
ARGV              = '$(width)', '$(height)', '$(TEXTURE_FILE_PATH)', '$(TEXTURE_NEW_WIDTH)'

All: run

all: $(TARGETS)

deploy: clean run

new-imagem.png: pnggrad8rgb.png
	cat $(SCRIPT) |$(GIMP) -i $(GIMP_OPT) -b "import sys; sys.path=['.']+sys.path; import $(SCRIPT:.py=);$(SCRIPT:.py=).run($(ARGV))" $(GIMP_QUIT)

interativo:
	cat i$(SCRIPT) |$(GIMP) $(GIMP_OPT) -b "import sys; sys.path=['.']+sys.path; import i$(SCRIPT:.py=);i$(SCRIPT:.py=).run($(ARGV))"

run: new-imagem.png

OUT = $(images_input) $(images_output)  processed

show:
	eog processed/new-pnggrad8rgb.png

clean:
	@rm -rf $(TARGETS) $(OUT) script.pyc
#EOF
