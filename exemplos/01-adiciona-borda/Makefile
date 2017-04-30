images_input  = foto-1.png
images_output = result.png
#images_output = $(addprefix new-, $(images_input))

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

deploy: clean run

script.pyc: $(images_input)
	cat script.py |gimp -i --batch-interpreter python-fu-eval --batch - -b "import sys; sys.path=['.']+sys.path; import script;script.run('result.png')" -b "pdb.gimp_quit(1)"

#gimp -i --batch-interpreter python-fu-eval --batch - -b "pdb.gimp_quit(1)" < script.py

run: script.pyc

OUT = $(images_input) $(images_output)

show:
	eog $(images_output)

clean:
	@rm -rf $(TARGETS) $(OUT) processed/ script.pyc
#EOF
