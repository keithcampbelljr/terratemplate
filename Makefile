PYTHON ?= python3
PIP ?= pip3

.PHONY: clean install

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install .

clean:
	rm -rf build \
		*.egg-info
