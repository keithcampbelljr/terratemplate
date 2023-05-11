PYTHON ?= python3
PIP ?= $(PYTHON) -m pip

.PHONY: clean install

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install .

clean:
	$(PIP) uninstall -y \
		click \
		terratemplate
	rm -rf build \
		*.egg-info
