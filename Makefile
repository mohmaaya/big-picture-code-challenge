# Set the name of the virtual environment
VENV_NAME = .venv
PYTHON_VERSION = 3

venv:
	python$(PYTHON_VERSION) -m venv $(VENV_NAME)

install:
	call $(VENV_NAME)/Scripts/activate && pip install -r requirements.txt

setup: venv install	

run:
	python -m app.main
