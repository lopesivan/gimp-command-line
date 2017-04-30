images_input  = exemplo.png
images_output = $(addprefix new-, $(images_input))

SCRIPT        = script.py
GIMP          =/usr/bin/gimp
GIMP_OPT      = --batch-interpreter python-fu-eval --batch -
GIMP_QUIT     = -b "pdb.gimp_quit(1)"

width   =  600
height  =  400

##############################################################################
ARGV  = '$(width)', '$(height)' , '$(images_output)'
##############################################################################

All: run

all: $(TARGETS)

deploy: clean run

$(images_output):
	cat $(SCRIPT) |$(GIMP) -i $(GIMP_OPT) -b "import sys; sys.path=['.']+sys.path; import $(SCRIPT:.py=);$(SCRIPT:.py=).run($(ARGV), False)" $(GIMP_QUIT)

interativo:
	cat $(SCRIPT) |$(GIMP) $(GIMP_OPT) -b "import sys; sys.path=['.']+sys.path; import gimpdraw; import $(SCRIPT:.py=);$(SCRIPT:.py=).run($(ARGV), True)"

run: $(images_output)

OUT = $(images_input) $(images_output)  processed

show:
	eog processed/$(images_output)

clean:
	@rm -rf $(TARGETS) $(OUT) script.pyc
#EOF
