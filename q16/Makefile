.PHONY: check build clean

check:
	PYTHONPATH=./src pytest tests/

build:
	python3 -m build

clean:
	rm -rf dist build *.egg-info src/*.egg-info
