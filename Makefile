update:
	rm -rf ./output
	python ./latex.py
	pelican


.PHONY: update
