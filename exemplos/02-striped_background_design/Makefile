images_input  = image.png
images_output = $(addprefix new-, $(images_input))

SCRIPT        = script.py
GIMP          =/usr/bin/gimp
GIMP_OPT      = --batch-interpreter python-fu-eval --batch -
GIMP_QUIT     = -b "pdb.gimp_quit(1)"

TEXTURE_FILE_PATH = ${PWD}/IMG_0001.jpg
MOON_TEXTURE_FILE_PATH = ${PWD}/moon.png
#MOON_TEXTURE_FILE_PATH = ${PWD}/Cat-cats-32958715-1440-900.jpg
MY_MESSAGE_1 = Ivan Carlos
#MY_MESSAGE_1 = Ivan Carlos

#HD1080
width = 1920
height= 1080

#HD720
#width   =  1280
#height  =  768

#width   =  7680
#height  =  4320

# width   =  300
# height  =  200

#width   =  2400
#height  =  1600

##############################################################################
ARGV              = '$(width)', '$(height)', '$(TEXTURE_FILE_PATH)', '$(MOON_TEXTURE_FILE_PATH)', '$(MY_MESSAGE_1)'

All: run

all: $(TARGETS)

deploy: clean run

new-image.png:
	cat $(SCRIPT) |$(GIMP) -i $(GIMP_OPT) -b "import sys; sys.path=['.']+sys.path; import $(SCRIPT:.py=);$(SCRIPT:.py=).run($(ARGV), False)" $(GIMP_QUIT)

interativo:
	cat $(SCRIPT) |$(GIMP) $(GIMP_OPT) -b "import sys; sys.path=['.']+sys.path; import gimpdraw; import $(SCRIPT:.py=);$(SCRIPT:.py=).run($(ARGV), True)"

run: new-image.png

OUT = $(images_input) $(images_output)  processed

show:
	eog processed/new-image.png

clean:
	@rm -rf $(TARGETS) $(OUT) script.pyc
#EOF
