update:
	python ./latex.py
	pelican
	rm *.pyc

publish:
	pelican -s publishconf.py
	rm *.pyc


.PHONY: update
