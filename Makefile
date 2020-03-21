update:
	rm -rf ./output
	python ./latex/latex.py
	pelican


.PHONY: update
