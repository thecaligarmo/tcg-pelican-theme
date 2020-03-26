update:
	python ./latex.py
	rm -rf ./output
	pelican


.PHONY: update
