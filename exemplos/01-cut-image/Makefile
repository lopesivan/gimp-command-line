image_input  = NumberedColorGrid2.png
image_output = $(addprefix new-, $(image_input))

SCRIPT        = script.py
GIMP          =/usr/bin/gimp
GIMP_OPT      = --batch-interpreter python-fu-eval --batch -
GIMP_QUIT     = -b "pdb.gimp_quit(1)"

ARGV          = './$(image_input)'

all: run

deploy: clean run

processed/$(image_output): $(image_input)
	cat $(SCRIPT) |$(GIMP) -i $(GIMP_OPT) -b "import sys; sys.path=['.']+sys.path; import $(SCRIPT:.py=);$(SCRIPT:.py=).run($(ARGV))" $(GIMP_QUIT)

interativo:
	cat i$(SCRIPT) |$(GIMP) $(GIMP_OPT) -b "import sys; sys.path=['.']+sys.path; import i$(SCRIPT:.py=);i$(SCRIPT:.py=).run($(ARGV))"

run: processed/$(image_output)

OUT = $(image_output) processed

show:
	eog processed/$(image_output)

clean:
	@rm -rf $(TARGETS) $(OUT) script.pyc
#EOF
